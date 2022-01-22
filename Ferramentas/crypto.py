def transforma_em_int(string):
    string_int = []
    for i in range(len(string)):
        string_int.append(ord(string[i]))
    return string_int

def analisa(numero):
    minimo = 65
    maximo = 123
    if numero == 32:
        numero = 123
    while numero < minimo:
        numero = maximo - (minimo - numero)
    while numero > maximo:
        numero = minimo + (numero - maximo)
    else:
        pass
    return(numero)

def criptografa(senha_int, key_int):
    cripto = []
    key = 0
    for i in range(0,len(key_int)):
        key += key_int[i]
    for i in range(len(senha_int)):
        letra = analisa(senha_int[i] + key)
        if letra == 123:
            letra = 32
        cripto.append(letra)
    return cripto

def descriptografa(senha_int, key_int):
    cripto = []
    key = 0
    for i in range(0,len(key_int)):
        key += key_int[i]
    for i in range(len(senha_int)):
        letra = analisa(senha_int[i] - key)
        if letra == 123:
            letra = 32
        cripto.append(letra)
    return cripto

def transforma_em_str(cripto):
    cripto_string = ''
    for i in range(len(cripto)):
        cripto_string += chr(cripto[i])
    return cripto_string


def main():
    key = 'michel'
    key_int = transforma_em_int(key)
    senha = input('Entre com a senha a ser criptografada: ')
    senha_int = transforma_em_int(senha)

    senha_cript_int = criptografa(senha_int,key_int)
    print(transforma_em_str(senha_cript_int))
    senha_descript_int = descriptografa(senha_cript_int,key_int)
    print(transforma_em_str(senha_descript_int))
    
