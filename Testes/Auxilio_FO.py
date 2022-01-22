# -*- coding: cp1252 -*-
class pelotao:
    def __init__(self, ano, letra):
        self.ano = ano
        self.letra = letra
        self.efetivo = []
        
        self.pelotao_str = str(self.ano)+str(self.letra.upper())
        

    def mostrar_pel(self):
        pel = str(self.ano)+self.letra.upper()
        print(pel)

    def adicionar_aluno(self,aluno):
        self.efetivo.append(aluno)

    def adicionar_ao_efetivo(self):
        tam_efet_adicionar = input("Indique o tamanho do efetivo do "+self.pelotao_str+" que deseja inserir: ")
        for i in range(tam_efet_adicionar):
            aluno = raw_input("Aluno "+str(i+1)+": ")
            self.adicionar_aluno(aluno)

    def mostrar_efetivo(self):
        print
        print("EFETIVO DO "+self.pelotao_str+"\n")
        for i in self.efetivo:
            print(i)


class FO_format:
    def __init__(self, pelotao):
        self.pelotao = pelotao
        self.frase_salva = ""
        self.frase_separada = []
        self.primeira_palavra = ""
        self.codigo_list = ['F2','H2','D7','C1','A3','F5','G6','J8','G7','F3']
        
    def frase(self):
        self.frase_salva = raw_input("Frase que deseja formatar: ")

    def capitaliza_frase(self):
        self.frase_salva = self.frase_salva.capitalize()

    def minuscula_frase(self):
        self.frase_salva = self.frase_salva.lower()

    def maiuscula_frase(self):
        self.frase_salva = self.frase_salva.upper()

    def separa_frase(self):
        self.frase_separada = self.frase_salva.split()

    def mostra_frase(self, frase):
        print(frase)

    def primeira_palavra_func(self):
        self.primeira_palavra = self.frase_separada[0]
    
primeiro_j = pelotao(1,'j')
primeiro_j.efetivo = ['ABREU','ALISSA','BRENO WOLGA','BRITO','CINARA','COLUCCI','FERNANDO DODA','FURLANETO','GALVAO','HALISSON SOUZA','HUGO','KAWAGUCHI','KEAN','LOBO','LOMBARDI','LUAN XAVIER','MARCONDES','MARCOS EDUARDO','MARIA EDUARDA','MATHEUS NOVAES','MOTA','PELARIN','PEZZOTTI','PRESTES','URQUISA','VICENTE','WILIAM SHIMIZU','ZACHARIAS']
#'ABREU','ALISSA','BRENO WOLGA','BRITO','CINARA','COLUCCI','FERNANDO DODA','FURLANETO','GALVAO','HALISSON SOUZA','HUGO','KAWAGUCHI','KEAN','LOBO','LOMBARDI','LUAN XAVIER','MARCONDES','MARCOS EDUARDO','MARIA EDUARDA','MATHEUS NOVAES','MOTA','PELARIN','PEZZOTTI','PRESTES','URQUISA','VICENTE','WILIAM SHIMIZU','ZACHARIAS'
format1 = FO_format(primeiro_j)
format1.frase()
format1.separa_frase()
frase_separada_txt = " ".join(format1.frase_separada)
ano = '20'

aluno_list = []
for i in primeiro_j.efetivo:
    if i in format1.frase_salva:
        aluno_list.append(i)
aluno_list_str = " ".join(aluno_list)
aluno_list_separada = aluno_list_str.split()

#SEPARA O CODIGO
codigo_list = []
for i in format1.frase_separada:
    for j in format1.codigo_list:
        if i == j:
            codigo_list.append(i)
qnt_anotacoes = len(codigo_list)


#SEPARA O PERIODO
meses = ['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez']
periodo_list = []
a = 1
for i in format1.frase_separada:
    for j in meses:
        if i == j:
            periodo_list.append(format1.frase_separada[a])
    a+=1


#PEGA A FRASE MOTIVO DA ANOTACAO
frase_motivo = []
for i in format1.frase_separada:
    #and i not in aluno_list_separada
    if not i in periodo_list and i not in codigo_list and i not in meses and not i.startswith(" ") and i not in aluno_list_separada:
        frase_motivo.append(i.lower())
            
frase_motivo_str = " ".join(frase_motivo)
frase_motivo = frase_motivo_str.split(".")

for i in range(1, len(frase_motivo), 1):
    frase_motivo[i] = frase_motivo[i].replace(" ","",1)

#CRIA LISTA DE ANOTACOES PRONTA
anotacao = []
def exibe_text_pronto(param):
    if frase_separada_txt.find(codigo_list[param]):
        anotacao.append(codigo_list[param]+" - "+periodo_list[param].replace("/","").upper()+ano+" - "+frase_motivo[param].capitalize()+".")

for j in range(0, len(codigo_list), 1):
    exibe_text_pronto(j)

#EXIBE QUANTIDADES DE CADA LISTA
print("Quantidade de ALUNOS ANOTADOS: "+str(len(aluno_list)))
print("Quantidade de ANOTAÇÕES: "+str(len(anotacao)))

#PARA EXIBIR LISTA
def exibe_list(list):
    for i in list:
        print(i)
        
#EXIBICAO DAS LISTAS
print
#exibe_list(aluno_list)
#exibe_list(codigo_list)
#exibe_list(periodo_list)
#exibe_list(frase_motivo)
exibe_list(anotacao)

input("Pressione <ENTER> para continuar")

