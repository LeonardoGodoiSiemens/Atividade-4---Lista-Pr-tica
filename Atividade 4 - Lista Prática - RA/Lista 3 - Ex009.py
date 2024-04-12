#Lendo 10 números inteiros entregue pelo usuário e os entregue em ordem crescente
listadeNumeros=[]
for i in range(10):
    num=int(input("Escolha seus números:"))
    listadeNumeros.append(num)
listadeNumeros.sort()
print(listadeNumeros)