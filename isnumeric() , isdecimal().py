n1=int(input('qual será o primeiro número?'))
n2=int(input('Qual será o segundo número?'))
n3=int(input('Qual será o terceiro que irá subtrair?'))
s=n1+n2-n3
print(f'O valor entre {n1} e {n2} subtraido por {n3} é {s}')
z=input('Digite o valor aqui:')
print('É um número?',z.isnumeric(),'. É um número decimal?',z.isdecimal(),'.')
