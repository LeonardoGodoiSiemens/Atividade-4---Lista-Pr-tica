#Programa para encontrar todos os pares entre 1 e 100
#Começando por encontrar todos os números em até 100
num=list(range(1,101))
print(f"A Lista de todos os números entre 1 e 100 é:\n{num}")
#Separando os Pares
pares=[i for i in range(1,101) if i%2==0]
print(f"Os Números pares são:\n{pares}")