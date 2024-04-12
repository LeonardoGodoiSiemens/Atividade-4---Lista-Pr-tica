#Calculando média de idades
quantIdades=[]
cont=0
print("Quando desejar finalizar, digite 0.")
while cont==0:
    idade=int(input("Qual a sua idade: "))
    quantIdades.append(idade)
    if idade==0:
        cont+=1
quantIdades.remove(0)
for i in range(0,len(quantIdades)):
    soma=sum(quantIdades)
    media=soma/len(quantIdades)
    print(f"As idades forcecidas foram:\n{quantIdades}")
    print(f"A média das idades fornecidas é: {media:.2f}")
    break