# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com desconto

preço = float(input('Digite o preço do produto: R$'))
desconto = int(input('Digite o desconto: '))
novo = preço - (preço * desconto / 100)

print(f'O valor do produto: R${preço:.2f}')
print(f'O desconto: {desconto:.2f}%')
print(f'O valor com desconto: R${novo:.2f}')