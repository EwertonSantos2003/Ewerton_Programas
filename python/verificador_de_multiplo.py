numero1=float(input("Digite um valor: "))
numero2=float(input("Digite um segundo valor: "))
if ((numero1 >= numero2 and numero1%numero2 == 0) or (numero2 >= numero1 and numero2%numero1 == 0)):
    print("São multiplos.")
else:
    print("Não são multiplos.")    