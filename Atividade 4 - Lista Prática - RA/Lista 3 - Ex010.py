#Entregar número da lista que se repete mais vezes
lista=[2,4,7,2,3,3,1,0,2,6]
numMaisRep=None
contagemDeRep=1
for i in lista:
    contagemdeNum=lista.count(i)
    if contagemdeNum>contagemDeRep:
        numMaisRep=i
        contagemDeRep=contagemdeNum
print(f"O numero mais repetido é o {numMaisRep}, com um total de {contagemDeRep} repetições")