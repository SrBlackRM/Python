def lucro(numero1, porcentagem):
    porcentagem = porcentagem/100
    lucro_obtido = numero1*porcentagem
    lucro_total = lucro_obtido + numero1
    return lucro_total


'''numero, porcent = int(input('Digite um número: ')), int(input('Digite uma porcentagem: '))
print(f'lucro total de {lucro(numero, porcent)}')
'''

