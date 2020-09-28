try:     
          nota1=float(input("Digite sua nota do 1º Semestre: "))
          nota2=float(input("Digite sua nota do 2º Semestre: "))
          media = ((nota1+nota2)/2)
          if (media >=7):
           print("Você foi aprovado!")
          else:
           print("Você foi reprovado!") 

except (ValueError):
           print ("Algum valor digitado incorretamente, por favor tente novamente!")

           



