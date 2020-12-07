equipamentos = []
valores = []
seriais = []
departamento = []
resposta = []

while resposta == "S":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Número Serial: ")))
    departamento.append(input("Departamento: "))
    resposta = input("Digite \"S\" para continuar: ").upper()

for indice in range(0,len(equipamentos)):
    print("\nEquipamento..:", (indice+1))
    print("\nNome..:", equipamentos[indice])
    print("\nEquipamento..:", valores[indice])
    print("\nEquipamento..:", seriais[indice])
    print("\nEquipamento..:", departamento[indice])
