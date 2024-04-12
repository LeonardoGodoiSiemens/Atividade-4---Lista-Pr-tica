#Recebendo 10 números e separando se estivem entre 10 e 20 ou não
listadeNumeros=[]
for i in range(10):
    numeros=float(input(f"Escolha seus números:"))
    listadeNumeros.append(numeros)
print(listadeNumeros)
#Separando os números que estão entre 10 e 20
numerosdentro=[]
numerosfora=[]
for numeros in listadeNumeros:
    if 10<=numeros<=20:
        numerosdentro.append(numeros)
    else:
        numerosfora.append(numeros)
print(f"Os números entre 10 e 20 são:\n{numerosdentro}\nE os números que não estão entre 10 e 20 são:\n{numerosfora}")