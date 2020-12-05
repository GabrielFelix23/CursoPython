numero = int(input("Digite um número qualquer para iniciar a tabuada: "))

#Valor inicial 1, o ultimo valor de parada do incremento 11=10, vai pular em 1 em 1
for valor in range(1, 11, 1):
    print(str(numero) + " x " + str(valor) + " = " + str((numero*valor)))