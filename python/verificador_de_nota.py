try: 
    nota=float(input("Digite sua nota: "))
except (ValueError): 
    print("Digite um valor corretamente!")
else:
    if (nota > 1):
       print("Valor incorreto.")

    else: 
        if (nota >= 0.9):
           print("Nota A")
        elif (nota >= 0.8):
           print("Nota B")
        elif (nota >= 0.7):
           print("Nota C")
        elif (nota >= 0.6):
           print("Nota D")
        elif (nota < 0.6):
           print ("Nota F")               

      



