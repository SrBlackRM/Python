num1 = input("Digite um número: ")
num2 = input("Digite outro número: ")

#string methods - para checar strings, todas retornam um boolean
# isnumeric - se todos os caracteres da string tem numeros positivos, pois i (-) negativo é um simbolo
# isdigit   - se todos os caracteres da string forem digitos
# isdecimal - se todos os caracteres da string forem decimais

#if num1.isdigit() and num2.isdigit():
#    num1 = int(num1)
#    num2 = int(num2)

#    print(num1 + num2)

#else:
#    print("não foi possível realizar a conta, não são numeros!")

#Podemos usar o "try: e except:" como se fosse if e else

try:
    num1 = int(num1)
    num2 = int(num2)

    print(num1 + num2)

except:
    print("não foi possível realizar a conta, não são numeros!")
