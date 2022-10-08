# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados

larg = float(input('Digite a largura '))
alt = float(input('Digite a altura: '))
área = larg * alt
tinta = área / 2

print(f'Sua altura é {alt}m. \nSua largura é {larg}m. \nSerá necessário {tinta}l de tinta')