import os
os.system("cls")
from dataclasses import dataclass

# ------------------------------------
# CLASSE FUNCIONARIO
# ------------------------------------
@dataclass
class Funcionario:
    nome: str
    data_de_admissao: int
    matricula: int
    endereco: str

    def exibir_dados(self):
        print(f"\nNome: {self.nome}")
        print(f"Data de Admissão: {self.data_de_admissao}")
        print(f"Matrícula: {self.matricula}")
        print(f"Endereço: {self.endereco}")


# ------------------------------------
# CLASSE CLIENTE
# ------------------------------------
@dataclass
class Cliente:
    nome_cliente: str
    data_de_nascimento: int
    endereco_cliente: str

    def exibir_dados(self):
        print(f"\nNome: {self.nome_cliente}")
        print(f"Data de Nascimento: {self.data_de_nascimento}")
        print(f"Endereço: {self.endereco_cliente}")


# ------------------------------------
# VARIÁVEIS
# ------------------------------------
listas_de_Funcionario = []
listas_de_Cliente = []

QUANTIDADE_DE_FUNCIONARIO = 3
QUANTIDADE_DE_CLIENTE = 3

nome_do_arquivo = "funcionario.csv"
arquivo_cliente = "cliente.csv"


# ------------------------------------
# CADASTRAR FUNCIONÁRIOS
# ------------------------------------
for i in range(QUANTIDADE_DE_FUNCIONARIO):
    funcionario = Funcionario(
        nome=input("Digite o nome do funcionário: "),
        data_de_admissao=int(input("Digite a data de admissão (apenas números): ")),
        matricula=int(input("Digite a matrícula: ")),
        endereco=input("Digite o endereço do funcionário: ")
    )
    listas_de_Funcionario.append(funcionario)


# ------------------------------------
# CADASTRAR CLIENTES
# ------------------------------------
for i in range(QUANTIDADE_DE_CLIENTE):
    cliente = Cliente(
        nome_cliente=input("Digite o nome do cliente: "),
        data_de_nascimento=int(input("Digite a data de nascimento (apenas números): ")),
        endereco_cliente=input("Digite o endereço do cliente: ")
    )
    listas_de_Cliente.append(cliente)


# ------------------------------------
# SALVAR FUNCIONÁRIOS NO CSV
# ------------------------------------
with open(nome_do_arquivo, "a", encoding="utf-8") as arquivo:
    for funcionario in listas_de_Funcionario:
        arquivo.write(
            f"{funcionario.nome},{funcionario.data_de_admissao},{funcionario.matricula},{funcionario.endereco}\n"
        )
print("\nFuncionários salvos com sucesso!\n")


# ------------------------------------
# SALVAR CLIENTES NO CSV
# ------------------------------------
with open(arquivo_cliente, "a", encoding="utf-8") as arquivo:
    for cliente in listas_de_Cliente:
        arquivo.write(
            f"{cliente.nome_cliente},{cliente.data_de_nascimento},{cliente.endereco_cliente}\n"
        )
print("Clientes salvos com sucesso!\n")


# ------------------------------------
# LER E EXIBIR FUNCIONÁRIOS
# ------------------------------------
print("EXIBINDO DADOS DOS FUNCIONÁRIOS:\n")

try:
    listas_de_Funcionario = []
    with open(nome_do_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            nome, data, matricula, endereco = linha.strip().split(",")
            funcionario = Funcionario(nome, int(data), int(matricula), endereco)
            listas_de_Funcionario.append(funcionario)

    for f in listas_de_Funcionario:
        f.exibir_dados()

except FileNotFoundError:
    print("O arquivo de funcionários não foi encontrado.")


# ------------------------------------
# LER E EXIBIR CLIENTES
# ------------------------------------
print("\nEXIBINDO DADOS DOS CLIENTES:\n")

try:
    listas_de_Cliente = []
    with open(arquivo_cliente, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            nome, data, endereco = linha.strip().split(",")
            cliente = Cliente(nome, int(data), endereco)
            listas_de_Cliente.append(cliente)

    for c in listas_de_Cliente:
        c.exibir_dados()

except FileNotFoundError:
    print("O arquivo de clientes não foi encontrado.")
