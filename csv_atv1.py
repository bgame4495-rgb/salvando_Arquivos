import os
os.system ("cls")
from dataclasses import dataclass

@dataclass
class Funcionario:
    nome: str 
    data_de_admissao: int
    matricula: int 
    endereco : str

def exibir_dados_funcionario(self):
    print(f"nome: {self.nome}, \nData de Admissão: {self.data_de_admissao}, \nMatricula: {self.matricula}, \n Endereço: {self.endereco}  ")

@dataclass
class Cliente:
    nome_cliente: str
    data_de_nascimento: int
    endereco_cliente: str

def exibir_dados_cliente(self):
    print(f"Nome: {self.nome_cliente}, Data de Nascimento: {self.data_de_nascimento}, \nEndereço: {self.endereco_cliente}")

listas_de_Funcionario = []
listas_de_Cliente = []

QUANTIDADE_DE_Cliente= 3
QUANTIDADE_DE_FUNCIONARIO = 3 

nome_do_arquivo = "funcionario.csv"
arquivo_cliente= "Cliente.csv"


for i in range(QUANTIDADE_DE_FUNCIONARIO):
    funcionario= Funcionario(
        nome = input("Digite o seu nome: "),
        data_de_admissao= int(input("Digite sua Data de Admissão: ")),
        matricula= int(input("Digite sua Matricula: ")),
        endereco= input("Digite seu endereço: ")
    )
    listas_de_Funcionario.append(funcionario)

for i in range(QUANTIDADE_DE_Cliente):
    cliente= Cliente(
        nome_cliente= input("Digite o nome do Cliente: ",
        data_de_nascimeto= int(input("Digite sua data de nascimento: ")),
        endereco_cliente=input("Digite o endereço do clinte: "))
    )
    listas_de_Cliente.append(cliente)

#salvando os dados
with open(nome_do_arquivo, "a", encoding="utf-8") as arquivo:
    for funcionario in listas_de_Funcionario:
        arquivo.write(
            f"{funcionario.nome},{funcionario.data_de_admissao},{funcionario.endereco}, {funcionario.matricula}\n"
            )
print("SALVO COM SUCESSO. \n")

with open(arquivo_cliente, "a", encoding="utf-8")as arquivo:
    for c in listas_de_Cliente:
        arquivo.write(f"{cliente.nome_cliente},{Cliente.data_de_nascimento},{Cliente.endereco_cliente}")
print("Dados do cliente Salvos com Sucesso!")

#lendo dados
print("Exibindo dados do funcionarios: \n")
try:
    listas_de_Funcionario = []
    with open(nome_do_arquivo, "r", encoding="utf-8")as arquivo:
         for linha in arquivo:
            nome, data,matricula,endereco = linha.strip().split(",")
            funcionario = Funcionario(nome, int(data), int(matricula), endereco)
            listas_de_Funcionario.append(funcionario)
    
    for f in listas_de_Funcionario:
        f.exibir_dados_funcionario()
except FileNotFoundError:
    print("O arquivo não foi encontrado.")

print("Dados Do cliente: \n")
try: 
    listas_de_Cliente= []
    with open(arquivo_cliente, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            nome,data, endereco= linha.strip().split(",")
            cliente= Cliente(nome,int(data),endereco)
            listas_de_Cliente.append(cliente)
        for c in listas_de_Cliente:
            c.exibir_dados_cliente()
except FileNotFoundError:
    print("Arquivo Cliente não encontrado!")
