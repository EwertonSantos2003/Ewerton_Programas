numero1=int(input("Digite um 1º valor: "))
numero2=int(input("Digite um 2º valor: "))
numero3=int(input("Digite um 3º valor: "))
print (numero1,numero2,numero3)
nMaior = numero1
if (numero2 > nMaior):
    nMaior = numero2
if (numero3 > nMaior):
    nMaior = numero3
    nMenor = numero1
if (numero2 < nMenor):
    nMenor = numero2
if (numero3 < nMenor):
    nMenor = numero3
print('O Maior valor é: ', nMaior, 'O Menor valor é: ', nMenor)