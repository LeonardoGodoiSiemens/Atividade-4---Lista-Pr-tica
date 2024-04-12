#Escolhendo um número inteiro, entre 1 e 10, e fazendo uma tábuada com o mesmo
num=int(input("Escolha um número inteiro, entre 1 e 10: "))
if num>10:
    print("Número inválido")
elif num<1:
    print("Número inválido")
else:
    print(f"Tábuada de 1 a 10: ")
    for i in range(1,11):
        print(f"{num} x {i} = {num*i}")