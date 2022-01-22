usuario = input('Digite seu usuário: ')
qnt_caracteres = len(usuario)

if qnt_caracteres < 6:
    print("Não foram digitados caracteres suficientes!!")

else:
    print("Você foi cadastrado no sistema")

string1 = input("Digite alguma coisa: ")
string2 = input("Digite outra coisa: ")

print(f"A quantidade total de caracteres digitados foi {len(string1) + len(string2)}")