numeros = []

for i in range(10):
    numero = float(input(f"Digite o número {i+1º}: "))
    numeros.append(numero)

print("Números na ordem inversa:")
for i in range(9, -1, -1):
    print(numeros[i])
