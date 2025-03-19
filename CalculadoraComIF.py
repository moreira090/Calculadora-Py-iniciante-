#calculadora
a = ((float(input('escreva um numero:'))))
op =(input('escolha uma operação'))
b = ((float(input('escolha outro numero:'))))
res = a + b 
if op == '+':
   res=a+b
elif op == '-':
   res=a-b
elif op == 'x':
   res=a*b
elif op == '/':
   res=a/b
else:
   print('Operador Invalido ')   

print(f"{a} {op} {b} = {res}")
