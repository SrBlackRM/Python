import random
import os

lista = {
        'frutas':('maca','banana','kiwi','melancia','laranja','uva','morango','abacate','abacaxi','limao','tangerina','acai','acerola','carambola','cereja','goiaba','jabuticaba'),
        'nomes':('Michel','Jade','Simone','Mauro','Isis','Seth','Helena','Miguel','Alice','Arthur','Laura','Heitor','Manoela','Bernardo','Valentina','Davi','Sophia','Theo','Isabella','Lorenzo'),
        'series':('friends','vikings','game of thrones','sabrina','la casa de papel','lucifer','the walking dead','stranger things','the witcher','greys anathomy','narcos','elite','breaking bad','sobrenatural','riverdale'),
        'paises':('China','Brasil','Estados Unidos','Italia','Russia','Bolivia','Suecia','Franca','Angola','Reino Unido','Alemanha','Noruega','Dinamarca','Suica','Australia','Japao','Portugal','Espanha','Grecia','Argentina','Turquia','India','Islandia'),
        'super-heroi':('Batman','Flash','Super Homem','Mulher Maravilha','Homem Aranha','Homem de Ferro','Hulk','Thor','Wolverine','Capitao America','Lanterna Verde','Aquaman','Doutor Estranho','Arqueiro Verde','Feiticeira Escarlate','Viuva Negra','Pantera Negra'),
        'animais':('abelha','arara','aranha','borboleta','coelho','girafa','pato','pavao','tatu','vaca','zebra','touro','sapo','aguia','asno','anta','baleia','barata','rato','bufalo','cobra','cabra','cachorro','gato','capivara','carrapato','cavalo','macaco','coala','jacare','crocodilo','elefante','esquilo','galinha','foca','gamba','leao','lobo','lumbriga','onça','peixe','urso','porco','ornitorrinco')
        }

escolha = ''
dica = ''
placar = 0
palavra = []
tentada = ''
erros = 0
const_max_erros = 16

def limpar_tela():
    os.system('clear')

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
    
def Dica():
    global dica
    print(f'A dica eh: {dica}\n')
            
def cont_placar():
    global placar
    if palavra_correta() and perda_por_erros() == False:
        placar += 1
    
    elif perda_por_erros() == True:
        placar = 0
    
def cont_erros(letra):
    global erros
    global escolha
    if letra not in escolha:
        erros += 1

def inserir_letras():
    letra = input('Insira uma letra: ')
    return letra
    
def join(string):
    string_pura = ''
    for letra in string:
        string_pura += letra + '  '
    return string_pura.upper()


def letras_tentadas(letra):
    global tentada
    if letra not in tentada:
        tentada += letra

def verificar_letras_corretas():
    global escolha
    global palavra
    global tentada
    letra = inserir_letras()
    for i in range(len(escolha)):
        if letra == escolha[i] or letra.upper() == escolha[i]:
            if palavra[i] == "_":
                palavra[i] = escolha[i]
                continue
            continue
        if letra not in tentada:
            letras_tentadas(letra)
    
    cont_erros(letra)


def palavra_correta():
    global palavra 
    global escolha
    for i in range(len(escolha)):
        if palavra[i] != '_':
            if palavra[i] == escolha[i]:
                continue
            elif palavra[i] == " ":
                continue
            else:
                print("Erro")
                exit(1)
        elif palavra[i] == '_':
            return False
    return True

def contagem_regressiva():
    global erros
    global const_max_erros

    qnt_restante = const_max_erros - erros
    return qnt_restante

def situacao():
    global palavra
    limpar_tela()
    Dica()
    
    palavra_joined = join(palavra)

    print(f"Letras ja tentadas > {tentada.upper()+' '}\n")
    print(f'Quantidade de erros > {erros} < faltam > {contagem_regressiva()} < tentativas\n')
    print(f'Letras certas: {palavra_joined}\n\n')

def numeros_finais():
    global placar
    global erros

    if erros < 4:
        mensagem = 'Parabéns, você foi muito bem!!'
    elif erros <= 6:
        mensagem = 'Parabéns, você foi bem'
    elif erros < 12:
        mensagem = 'Precisa melhorar um pouco :/'
    elif erros <= 14:
        mensagem = 'Acertou a palavra chutando?'
    elif erros < 16:
        mensagem = 'Chutou tudo, que feio'
    else:
        mensagem = 'Tente de novo'
    
    print(f'Placar > {placar} <\n')
    print(f"Quantidade de Erros > {erros} < \n\n{mensagem}")


def continuar():
    print(f"\n{'Deseja continuar?': ^63}")
    print(f"{'1 - Sim': ^63}")
    print(f"{'2 - Nao': ^63}\n")
    resposta = input('Resposta: ')
    if resposta == '1':
        return False
    if resposta == '2':
        limpar_tela()
        return True

def perda_por_erros():
    global erros
    global const_max_erros
    if erros >= const_max_erros:
        return True
    else:
        return False

def funcionamento():
    while palavra_correta() != True:
        verificar_letras_corretas()
        situacao()
        if perda_por_erros() == True:
            limpar_tela()
            break
            
    limpar_tela()
    
def mostra_resultado():
    global escolha
    certa = 'Palavra certa!!'
    errada = 'Chutar tudo não vale, tenta de novo!!'
    
    if perda_por_erros() == True:
        print(f'{errada: ^63}\n')
    
    else:        
        print('{: ^63}\n'.format(certa))
        print(f'{escolha.upper():-^63}\n')

def zera_variaveis():
    global escolha
    global palavra
    global tentada
    global erros

    escolha = ''
    palavra = []
    tentada = ''
    erros = 0

def main():
    resposta = False

    while resposta != True:
        
        zera_variaveis()
        limpar_tela()
        escolhe()
        preenche_palavra_com_vazio()
        Dica()
        funcionamento()
        cont_placar()
        mostra_resultado()
        numeros_finais()
        resposta = continuar()

    exit(0)

main()
