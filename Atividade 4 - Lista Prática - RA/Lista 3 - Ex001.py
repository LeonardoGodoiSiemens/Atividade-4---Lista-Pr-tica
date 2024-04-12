#Exibindo números de 1 a 50
def create_list(n):
    num=[]
    for i in range(n+1):
        num.append(i)
    return num
print(create_list(50))