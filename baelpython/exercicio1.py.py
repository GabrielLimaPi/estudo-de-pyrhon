numeros = []
for i in range(5):
 numero = int(input(f"Digite o {i+1}º número inteiro: "))
 numeros.append(numero)
print("Os números digitados foram:")
for numero in numeros:
    print(numero)
