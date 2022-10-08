# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

num1 = int(input('Digite um número: '))

num2 = 0
while num2 <= 10:
    print(f'{num1} x {num2} = {num1*num2}')
    num2 += 1