a = float(input('Informe um valor para A: '))
b = float(input('Informe um valor para B: '))
     
if ((a > 0) and (b > 0)):
   c = 30
elif ((a > 0) and (b < 0)):
   c = 0
elif ((a < 0) and (b > 0)):
   c = -1
else:
    c = a * b * (-1)
    pol = (a * a) + (2 * a * b) + (b * b) + (c * a * c)
    print('O resultado do polinômio é: ',pol)

