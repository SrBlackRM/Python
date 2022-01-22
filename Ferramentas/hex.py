string2 = []
def convert_to_int(string):
    for i in range(len(string)):
        string2.append(ord(string[i])+13)

string3 = []
def convert_to_hex():
    for i in range(len(string2)):
        string3.append(hex(string2[i]))

def convert_to_str():
    string = ''
    for i in range(len(string2)):
        string += chr(string2[i])
    return string

def criptografar():
    entrada = input('Criptografar: ')
    convert_to_int(entrada)
    saida = convert_to_str()
    print(f'Criptografado: {saida}')

