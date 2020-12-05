nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade >= 65:
    print("O paciente " + nome + " possui atendimento!")
else:
    print("O paciente " + nome + " não possui atendimento!")