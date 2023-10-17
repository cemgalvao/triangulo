# VALIDAR UM TRIANGULO

#entrada
a=int(input('Digite o valor de um lado do triângulo:'))
b=int(input('Digite o valor do outro lado do triângulo:'))
c=int(input('Digite o valor do último lado do triângulo:'))

#processamento e saída dfhsd

if a + b < c or b + c < a or c + b < a:
    print('não é uma triangulo')
else:
    print('é um triangulo')
    if a==b and b==c and c==a:
        print('É equilátero')
    if a==b  and a!=c and b!=c or b==c and a!=b and a!=c or c==a and a!=b and b!=c:
        print('É um triangulo Isósceles ')
    if a!=b and a!=c and b!=c:
        print('É um triângulo Escaleno')
