from dataclasses import dataclass

@dataclass
class Funcionario:
    nome: str
    data_nascimento: str
    rg: int
    cpf: int

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Data de Nascimento: {self.data_nascimento}")
        print(f"RG: {self.rg}")
        print(f"CPF: {self.cpf}")
        print("-" * 30)

lista_de_funcionarios = []
quantidade_de_funcionarios = 5
nome_do_arquivo = "Funcionarios.csv"

# Entrada de dados
for i in range(quantidade_de_funcionarios):
    funcionario = Funcionario(
        nome=input("Digite seu nome: "),
        data_nascimento=input("Digite sua data de nascimento: "),
        rg=int(input("Digite seu RG: ")),
        cpf=int(input("Digite seu CPF: "))
    )
    lista_de_funcionarios.append(funcionario)

# Salvando no arquivo
with open(nome_do_arquivo, "a", encoding="utf-8") as arquivo:
    for funcionario in lista_de_funcionarios:
        arquivo.write(f"{funcionario.nome},{funcionario.data_nascimento},{funcionario.rg},{funcionario.cpf}\n")

print("Dados salvos com sucesso.\n")

# Lendo o arquivo
print("Exibindo todos os funcionarios:\n")
try:
    lista_todos_funcionarios = []
    with open(nome_do_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            nome, data_nascimento, rg, cpf = linha.strip().split(",")
            funcionario = Funcionario(nome, data_nascimento, int(rg), int(cpf))
            lista_todos_funcionarios.append(funcionario)

    for f in lista_todos_funcionarios:
        f.exibir_dados()

except FileNotFoundError:
    print("O arquivo nao foi encontrado.")
