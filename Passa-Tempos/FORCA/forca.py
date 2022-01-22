import random
import os

lista = {'frutas':('maca','banana','kiwi','melancia','laranja','uva'),
         'nomes':('michel','jade','simone','mauro'),
         'series':('friends','vikings','game of thrones','sabrina','la casa de papel','lucifer','the walking dead')}

escolha = ''
dica = ''
placar = 0
palavra = []
tentada = ''

def limpar_tela():
    os.system('cls')

def escolhe():
    global escolha
    global lista
    global dica
    escolha = random.choice(list(lista.items()))
    dica = escolha[0]
    escolha = escolha[1][random.randrange(len(escolha[1]))]

def preenche_palavra_com_vazio():
    global palavra
    global escolha
    for i in escolha:
        if i == ' ':
            palavra.append(' ')
        else:
            palavra.append('_')

def cont_placar():
    global placar
    if(palavra_correta):
        placar += 1
    print(f'Placar: {placar}')
    print()

def inserir_letras():
    letra = input('Insira uma letra: ')
    return letra

def letras_tentadas(letra):
    global tentada
    if tentada == '':
        tentada += letra
    elif letra not in tentada:
        tentada += letra

def verificar_letras_corretas():
    global escolha
    global palavra
    global tentada
    letra = inserir_letras()
    for i in range(len(escolha)):
        if letra == escolha[i]:
            if palavra[i] == "_":
                palavra[i] = escolha[i]
                continue
            continue
        letras_tentadas(letra)


def palavra_correta():
    global palavra 
    global escolha
    for i in range(len(escolha)):
        if palavra[i] != '_':
            if palavra[i] == escolha[i]:
                continue
            else:
                print("Erro")
                exit(1)
        elif palavra[i] == '_':
            return False
    return True            

def situacao():
    limpar_tela()
    print(f'A dica eh: {dica}')
    print()
    print(f'Letras ja tentadas: {tentada}')
    print()
    print(f'Letras certas: {palavra}')
    print()
    print()

def continuar():
    print()
    print("Deseja continuar?")
    print("1 - Sim")
    print("2 - Nao")
    print()
    resposta = input('Resposta: ')
    if resposta == '1':
        return False
    if resposta == '2':
        return True



def funcionamento():
    while palavra_correta() != True:
        verificar_letras_corretas()
        situacao()
    limpar_tela()
    certa = 'Palavra certa!!'
    print('{: ^63}'.format(certa))
    print('')
    print(f'{escolha:-^63}')
    print('')


def main():
    global palavra
    global escolha
    global dica
    global tentada
    resposta = False

    while resposta != True:
        escolha = ''
        palavra = []
        tentada = ''

        limpar_tela()
        escolhe()
        preenche_palavra_com_vazio()

        print(f'A dica eh: {dica}')
        print()

        funcionamento()
        cont_placar()
        resposta = continuar()

main()