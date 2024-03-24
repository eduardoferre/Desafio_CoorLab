import os
import uvicorn
from pyfiglet import Figlet
from uvicorn.config import LOGGING_CONFIG
from dotenv import load_dotenv
from fastapi import FastAPI, Path, Depends, HTTPException
import json


load_dotenv()     
app = FastAPI()

with open('app/data.json') as f:
    data = json.load(f)

@app.get("/")
async def root():
    return data


@app.get("/destinos")
async def return_destinos():
    cidades_distintas = []

    for transporte in data['transport']:
        if transporte['city'] not in cidades_distintas:
            cidades_distintas.append(transporte['city'])
    return cidades_distintas



@app.get("/destinos/{destino}")
async def return_destino(destino: str):
    result = [i for i in data['transport'] if destino == i['city']]
    for transporte in result:
        transporte['price_econ'] = float(transporte['price_econ'].replace('R$ ', '').replace(',', '.'))
        transporte['duration'] = int(transporte['duration'].replace('h', ''))


    menor_preco_econ = min(transporte['price_econ'] for transporte in result)
    lista_menor_preco_econ = [transporte for transporte in result if transporte['price_econ'] == menor_preco_econ]

    menor_duracao = min(transporte['duration'] for transporte in result)

    lista_menor_duracao = [transporte for transporte in result if transporte['duration'] == menor_duracao]

    lista_final = lista_menor_preco_econ + lista_menor_duracao

    return lista_final




def display_ascii_art():
    custom_figlet = Figlet(font='slant')
    message = custom_figlet.renderText('API REST')
    print(message)

def run():
    # Format logs with timestamp
    LOGGING_CONFIG["formatters"]["default"]["fmt"] = "%(asctime)s [%(name)s] %(levelprefix)s %(message)s"
    LOGGING_CONFIG["formatters"]["default"]["datefmt"] = "%Y-%m-%d %H:%M:%S"
    LOGGING_CONFIG["formatters"]["access"]["fmt"] = '%(asctime)s %(levelprefix)s %(client_addr)s - "%(request_line)s" %(status_code)s'
    display_ascii_art()
    uvicorn.run("main:app", host="0.0.0.0", port=8000)


if __name__ == '__main__':
    run()