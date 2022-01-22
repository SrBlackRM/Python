minha_string = "Michel Rodrigues Mota"
tamanho_string = len(minha_string)

c = 0
contagem_atual = 0
letra = ''

while c < tamanho_string:
    qnt_vezes_letra = minha_string.count(minha_string[c])

    if contagem_atual < qnt_vezes_letra and minha_string[c].strip():
        letra = minha_string[c]
        contagem_atual = qnt_vezes_letra

    c+=1

print(letra, contagem_atual)