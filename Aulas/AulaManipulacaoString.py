"""
Manipulando strings - Aula 6
* String indices
* Fatiamento de strings [inicio:fim:passo]
* Funções built-in len, abs, type, print, etc ...
Essas funções podem ser usadas diretamente em cada tipo.
"""

#positivos [0123456789]
#para acessar algum indice de uma string, coloca entre [] o numero do indice, exmp

texto = "Michel Rodrigues Mota"
print(texto[2]) #vai retornar o "c"

#para pegar uma fatia coloca entre [ : ] onde o primeiro espaço é onde vai começar e o segundo onde vai terminar
print(texto[7:16]) #vai retornar rodrigues

#para pegar a ultima letra, por exmp, é possivel usar negativos da seguinte forma :
print(texto[-1]) #de traz para frente começa no menos 1

#outros exemplos
print(texto[:-1]) #no caso, vai desde o começo até a ultima letra, excluindo-a

#da para pegar pedaços a cada tantas letras, exemplo:
print(texto[0:7:2]) #vai retornar M(0) c(2) e(4), pois vai até o 6 pulando uma letra
