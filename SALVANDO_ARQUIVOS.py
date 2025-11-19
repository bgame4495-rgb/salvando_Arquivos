import os
from dataclasses import dataclass
os.system("cls")

@dataclass
class Paciente:
    nome:str
    idade:str
    peso: int
    altura : float
    cpf: int

    def exibir_dados(self):
        print (f"nome: {self.nome} \nidade:{self.idade}, peso: {self.peso}, altura: {self.altura}, cpf: {self.cpf}")

lista_de_pacientes = []
QUANTIDADE_DE_PACIENTES = 2

for i in range (QUANTIDADE_DE_PACIENTES):

    paciente = Paciente(
        nome = input("digite seu nome:"),
        idade = int(input("digite sua idade: ")),
        peso = int(input("digite seu peso: ")),
        altura = float(input("digite sua altura: ")),
        cpf = int(input("digite seu cpf: "))
    )
    lista_de_pacientes.append(paciente)

nome = input("digite seu nome:")
idade = int(input("digite sua idade: "))
peso = int(input("digite seu peso: "))
altura = float(input("digite sua altura: "))
cpf = int(input("digite seu cpf: "))

lista_de_pacientes.append(paciente)
print()
nome_do_arquivo="dados_pacientes.csv"

with open(nome_do_arquivo, "a") as arquivo_pacientes:
    for paciente in lista_de_pacientes:
        arquivo_pacientes.write(f"Nome:{paciente.nome},\n Idade:{paciente.idade},\n Peso:{paciente.peso},\n Altura:{paciente.altura},\n CPF:{paciente.cpf}\n")

print("dados salvados com sucesso. ")

print("\nexibindo todos pacientes: ")
try:
    ...
except FileNotFoundError:
    ...
