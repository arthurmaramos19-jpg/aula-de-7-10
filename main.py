import random

CARACTERES = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

psw_length = int(input("Insira o comprimento da sua senha"))

new_password = ""

for i in range(psw_length):
    new_password += random.choice(CARACTERES)

print("Nova senha gerada" + new_password)
 