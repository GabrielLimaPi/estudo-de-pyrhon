def eh_consoante(caractere):
    consoantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    return caractere in consoantes

vetor = []

for i in range(10):
    caractere = input(f"Digite o caractere {i+1}: ")
    vetor.append(caractere)

consoantes = []

for caractere in vetor:
    if eh_consoante(caractere):
        consoantes.append(caractere)

print(f"Quantidade de consoantes lidas: {len(consoantes)}")
print("Consoantes:", consoantes)
