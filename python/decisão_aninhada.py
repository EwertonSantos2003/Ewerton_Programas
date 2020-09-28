numero=50
chute=int(input("Digite um número: "))

if (chute==numero):
    print("Você acertou!!")
else:
    if (chute>numero):
        print("Você quase acertou!! Seu número é maior que o desejado.")

    else:
        if (chute<numero):
            print("Você quase acertou!! Seu número é menor que o desejado.")

