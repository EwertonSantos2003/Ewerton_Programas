try:
         base=float(input("Digite a base do triângulo: "))
         altura=float(input("Digite a altura do triângulo: "))
         if ((base < 0 ) or (altura < 0)):
            print ("Digite um valor maior que 0.")
         else: 
            area = (base*altura)/2
            print ("A área do triângulo é: ", area,"cm²")

except (ValueError):
            print ("Valor com erro, por favor digite novamente!")

