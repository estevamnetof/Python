# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

real = float(input('Quanto você tem na sua carteira? R$'))
cotação = 5.20
dólar = real / cotação

print(f'Considerando que você tem R${real} em sua carteira. \nÉ possível comprar US${dólar:.2f}')