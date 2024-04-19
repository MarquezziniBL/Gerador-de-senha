import string
import random
import time


def senha(tamanho):
    senha = ""
    tempo = 0
    L = ["!", "@", "#", "$", "%", "&", "*", "(", ")"]
    a = list(string.ascii_lowercase)
    while len(senha) <= tamanho:
        if len(senha) == tamanho:
            break
        else:
            senha += str(random.choice(a))
            senha += str(random.choice(range(0, 9)))
            senha += random.choice(L)
    while tempo < 3:
        print(".")
        tempo += 1
        time.sleep(1)
    return senha


print("Bem vindo ao gerador de senhas")

while True:
    tamanho = int(input("\nQual o tamanho da senha( 0=sair)? "))
    if tamanho == 0:
        break
    else:
        print(f"Sua senha gerada foi: {senha(tamanho)}")

print("\nSaindo do gerador de senhas")
