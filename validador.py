# VALIDAR UM TRIANGULO

#entrada
a=int(input('digite um valorpara o lado do triângulo'))
b=int(input('digite um valorpara o lado do triângulo'))
c=int(input('digite um valorpara o lado do triângulo'))

#processamento e saída dfhsd

if a + b < c or b + c < a or c + b < a:
    print('não é uma triangulo')
else:
    print('é um triangulo')
    if a==b and b==c and c==a:
    print('é equilátero')
    if a==b or b==c or c==a:
    print('é um triangulo Isósceles ')





