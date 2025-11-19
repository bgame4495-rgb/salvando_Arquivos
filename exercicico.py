from dataclasses import dataclass
import os
os.system("cls") 

@dataclass
class Funcionario:
    nome: str 
    data_nascimento: str 
    rg: int
    cpf: int

    def exibir_dados(self):
        print(f"Nome: {self.nome} \nData de Nascimento: {self.data_nascimento}\nRG: {self.rg}\nCPF: {self.cpf}")

lista_de_funcionarios = []
quantidade_de_funcionarios = 5

for i in range(quantidade_de_funcionarios):
    Funcionario= Funcionario(
        nome = input("Digite seu nome: "),data_nascimento = input("Digite sua data de nascimento: "),
        rg = int(input("Digite seu RG: ")), cpf = int(input("Digite seu CPF: "))
    )
    lista_de_funcionarios.append(Funcionario) 
    nome_do_arquivo = "Funcionarios.csv"

with open(nome_do_arquivo, "a") as arquivo_funcionarios:
    for Funcionario in lista_de_funcionarios:
        arquivo_funcionarios.write(f"Nome:{Funcionario.nome},\n Data de Nascimento:{Funcionario.data_nascimento},\n RG:{Funcionario.rg},\n CPF:{Funcionario.cpf}\n")
print("Dados salvos com sucesso.")
print("\nExibindo todos os funcionarios: ")
try:
    with open("nome_do_arquivo", "r", encoding="utf-8") as arquivo:
        lista_todos_funcionarios = arquivo.readlines()
        for Funcionario in lista_todos_funcionarios:
            nome, data_nascimento, rg, cpf = Funcionario.strip().split(", ")
            Funcionario = Funcionario(nome, data_nascimento, rg, cpf)
            lista_todos_funcionarios.append(Funcionario)
        for Funcionario in lista_todos_funcionarios:
            Funcionario.exibir_dados()
except FileNotFoundError:
    print("O arquivo nao foi encontrado.")  
