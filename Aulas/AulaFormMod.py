"""
Formatando valores com modificadores - Aula 5

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(Número)f - Quantidade de casas decimais (float)
:(Caractere)(> ou < ou ^)(Quantidade)(Tipo - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""

#EXEMPLO 1
"""
num1 = 10
num2 = 3
divisao = num1 / num2
print(f"{divisao:.2f}")
"""

#EXEMPLO 2
nome = "Michel Rodrigues Mota"
nome_formatado = '{:@^63}'.format(nome)
nome_lower = nome.lower() #o lower() deixa todos os caracteres minusculos
nome_upper = nome.upper() #o upper() deixa todos os caracteres maiusculos
nome_title = nome_lower.title() #o title() deixa todas as iniciais maiusculas (muito util)

print(f'{nome:#^63}')
print(nome_formatado)
print(nome_lower)
print(nome_upper)
print(nome_title)