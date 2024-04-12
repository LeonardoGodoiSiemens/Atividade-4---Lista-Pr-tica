#Lendo números positivos e revelando todos os seus divisores
num=int(input("Escolha o seu número, inteiro e positivo: "))
if num <=0:
    print("Número inválido!!! Tente Novamente!")
else:
    listadeDivisores=[]
    for i in range(1,num+1):
        if num%i==0:
            listadeDivisores.append(i)
print(f"A lista de divisores do número {num} é:")
for lista in listadeDivisores:
    print(lista)