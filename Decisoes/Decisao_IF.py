nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
tipo_Doencas = input("Suspeita de doenças infectocontagiosa?")

if idade >= 65:
    print("O paciente " + nome + " possui atendimento!")

elif tipo_Doencas == "SIM":
    print("O paciente " + nome + " deve ser direcionado para sala de espera reservada.")

else:
    print("O paciente " + nome + " não possui atendimento!")