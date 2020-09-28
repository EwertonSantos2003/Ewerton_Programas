try:
       numero1=float(input("Digite um valor: "))
       numero2=float(input("Digite um outro valor: "))
       print (numero1, numero2)
except (ValueError):
       print ("Valor com problemas, por favor digite novamente um valor.")           