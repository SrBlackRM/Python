def wowpper(string):
    letras = 'abcdefghijklmnopqrstuvwxyz éãóàíôõ'
    LETRAS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ ÉÃÓÀÍÔÔ'
    nova_string = ''
    for letra in string:
        c = 0
        while c < len(letras):
            if letra == letras[c]:
                nova_string += LETRAS[c]
                break
            c+=1
    return nova_string

def nonupper(string):
    letras = 'abcdefghijklmnopqrstuvwxyz éãóàíôõ'
    LETRAS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ ÉÃÓÀÍÔÔ'
    nova_string = ''
    for letra in string:
        c = 0
        while c < len(letras):
            if letra == LETRAS[c]:
                nova_string += letras[c]
                break
            c+=1
    return nova_string

TEXTO = "O RATO ROEU"
texto = nonupper(TEXTO)
print(texto)