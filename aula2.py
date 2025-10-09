import random
caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
comprimento = int(input("Digite o comprimento da senha: "))
senha = ""
senha += random.choice(caracteres)

for i in range(comprimento):
    senha += random.choice(caracteres)

print("Senha gerada:", senha)
