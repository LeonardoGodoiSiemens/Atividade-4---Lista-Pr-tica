#Pedindo 10 números e separando pares e ímpares
listadeNumeros=[]
cont=0
while cont<10:
    numeros=float(input("Escolha seus números: "))
    cont+=1
    listadeNumeros.append(numeros)
    listadeNumeros.sort
print(f"A lista de números é:\n{listadeNumeros}")
pares=[i for i in listadeNumeros if i%2==0]
impares=[i for i in listadeNumeros if i%2==1]
print(f"Seus números pares são: {pares}")
print(f"Seus números ímpares são: {impares}")