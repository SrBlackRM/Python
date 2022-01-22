"""
Faça um programa que peça ao usuário digitar um número inteiro, informe se esse número é par ou impar.
Caso o usuário não digite um número, informe que não é um inteiro.
"""

"""
#Resolução
num1 = input("Digite um numero: ")

if num1.isdigit():
    if int(num1)%2 == 0:
        print("O número é par!!")
    else:
        print("O número é impar!!")

else:
    print("Não é um número inteiro positivo!")
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a 
saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""

#Resolução

"""
hora = input("Digite o horário de agora: ")

if hora.isnumeric():
    hora = int(hora)

    if hora >= 8 and hora < 12:
        print("Bom dia!!")

    elif hora >= 12 and hora < 18:
        print("Boa tarde!!")

    elif hora >= 18 and hora < 24:
        print("Boa noite!!")

    elif hora >= 0 and hora < 8:
        print("VAI DORMIR!!")

else:
    print("ERRO")
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos
escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, esreva "Seu nome é normal";
se maior que 6 escreva "Seu nome é muito grande!".
"""

#Resolução

nome = input("Digite seu nome: ")
qnt_letras = len(nome)

if qnt_letras <= 4:
    print("Seu nome é curto!")

elif qnt_letras <= 6:
    print("Seu nome é normal!")

else:
    print("Seu nome é grande!!")