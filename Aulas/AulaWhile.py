"""
While em Python - Aula 7
utilizado para realizar ações enquanto uma condição for verdadeira
"""

"""
while True: # loop infinito
    nome = input("Qual o seu nome? ")
    print(f"Olá {nome}!")

x = 0
while x < 10:

    print(x)
    x+=1

print(f"{x} ACABOU")

"""

"""
Podemos controlar os laços de repetição ou condição com continue e break 
quando colocamos continue, o laço continua em execução, com break para
"""

x = 0
while x < 10:
    if x == 3:
        x+=1
        continue #faz pular o 3 e ir direto pro 4
    print(x)
    x+=1

print(f"{x} ACABOU")
