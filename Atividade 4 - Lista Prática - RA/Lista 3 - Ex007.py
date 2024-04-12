#Calculando a soma de todos os 50 primeiros números pares
listadeNumeros=list(range(1,101))
print(listadeNumeros)
pares=[i for i in range(1,101) if i%2==0]
print(f"Os números pares são:\n{pares}")
print(f"A soma dos 50 primeiros números pares é:\n{sum(pares)}")