import json

with open('app/data.json') as f:
    data = json.load(f)

destino = str(input("Digite um destino: "))

result = [i for i in data['transport'] if destino == i['city']]


for transporte in result:
    transporte['price_econ'] = float(transporte['price_econ'].replace('R$ ', '').replace(',', '.'))
    transporte['duration'] = int(transporte['duration'].replace('h', ''))


menor_preco_econ = min(transporte['price_econ'] for transporte in result)
lista_menor_preco_econ = [transporte for transporte in result if transporte['price_econ'] == menor_preco_econ]

menor_duracao = min(transporte['duration'] for transporte in result)
lista_menor_duracao = [transporte for transporte in result if transporte['duration'] == menor_duracao]




print(menor_preco_econ)
print(lista_menor_preco_econ)

print("----------------")

print(menor_duracao)
print(lista_menor_duracao)


cidades_distintas = []

for transporte in data['transport']:
    if transporte['city'] not in cidades_distintas:
        cidades_distintas.append(transporte['city'])

print(cidades_distintas)