idade=int(input("Digite sua idade: "))
if (idade >= 18):
    print("Você pode tirar a CNH!")
elif (idade < 15):
    print("Você não pode tirar sua CNH!")
elif (idade >= 16) and (idade <18):
    print("Você precisa de autorização dos seu pais!")    