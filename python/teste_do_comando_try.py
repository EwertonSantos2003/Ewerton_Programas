try:
       produto = int(input("Digite o preço do arroz: "))
       resultado = (produto-(produto*0.10))
       print("O novo valor do arroz com 10% de desconto é: ", resultado)
except (ValueError, TypeError): 
       print("Foi encontrado um problema nos tipos de dados que você digitou, tente novamente.")
except (KeyboardInterrupt):
       print('O usuário preferiu não digitar um valor.')              
finally:
       print("Volte sempre, muito obrigado! :) ")  
       
       
       
