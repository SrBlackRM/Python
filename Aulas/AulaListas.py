"""
Listas python
uma lista é inicializada com []
exemplo, lista = []

pode-se inicializar também com valores dentro
exemplo, frutas = ['banana', 'maça', 'morango']

para chamar um item da lista usa-se
exemplo, frutas[1] 
retora: maça

append, insert, pop, del, clear, extend, + são algumas funções
interessantes para listas

append adiciona o item no final da lista
exemplo, frutas.append('kiwi')

com insert, é possível escolher onde quer colocar o item
exemplo, frutas.insert(0,'kiwi')
coloca no indice 0 a palavra kiwi

del deleta um item da lista, exemplo del(frutas[1])

toda lista tem um min e um max, podendo ser usado da seguinte forma:
maximo = max(frutas)
minimo = min(frutas)
"""

frutas = []

frutas.append('maça')
frutas.append('banana')
print(frutas)
frutas.insert(0,'melancia')
print(frutas)
del(frutas[1])
print(frutas)
print(min(frutas))


