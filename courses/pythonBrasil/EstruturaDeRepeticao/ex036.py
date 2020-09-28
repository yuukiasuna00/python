'''Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será 
digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar 
em 10, o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo'''


num = int(input("Digite um número inteiro para ver sua tabuada: "))
ini = int(input("Digite o valor inicial: "))
fin = int(input("Digite o valor final: "))

mul = 1
for val in range(ini, fin+1):
    mul = num * val
    print(f'{num} x {val} = {mul}')



