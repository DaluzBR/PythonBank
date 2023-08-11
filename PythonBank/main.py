import random
import utils
import cpf_br

# Função principal do programa
def main():
    menu_main = """
**************************************************
****************** BANCO PYTHON ******************
**************************************************
  [ 1 ] Depósito          [ 5 ] Listar contas
  [ 2 ] Saque             [ 6 ] Novo usuário
  [ 3 ] Extrato           [ 7 ] Listar usuários
  [ 4 ] Nova conta        [ 0 ] Sair
**************************************************

Operação: """

    SAQUES_LIMITE_POR_DIA = 3
    SAQUES_LIMITE_VALOR = 500.0

    agencia_numero = "0001"
    saques_numero_por_dia = 0
    saldo = 0.0
    extrato = ""
    #usuarios = []
    usuarios = lista_usuarios()
    #contas = []
    contas = lista_contas()

    # Loop principal do programa.
    while True:
        opcao = input(menu_main)

        if opcao == '1':
            saldo, extrato = operacao_deposito(saldo, extrato)
        elif opcao == '2':
            saldo, extrato, saques_numero_por_dia = operacao_saque(
                saldo=saldo,
                extrato=extrato,
                saques_numero_por_dia=saques_numero_por_dia,
                saques_limite_por_dia=SAQUES_LIMITE_POR_DIA,
                saques_limite_valor=SAQUES_LIMITE_VALOR
            )
        elif opcao == '3':
            operacao_extrato(saldo, extrato=extrato)
        elif opcao == '4':
            operacao_criar_conta(agencia_numero, usuarios, contas)
        elif opcao == '5':
            operacao_listar_contas(contas)
        elif opcao == '6':
            operacao_criar_usuario(usuarios)
        elif opcao == '7':
            operacao_listar_usuarios(usuarios)
        elif opcao == '0':
            operacao_sair()
            break
        else:
            operacao_invalida()

# Operação inválida.


def operacao_invalida():
    print()
    print("".center(50, "*"))
    print(" Operação inválida!")
    print(" Por favor, selecione novamente uma operação válida.")
    print("".center(50, "*"))
    print()


# Operação de saída do programa.
def operacao_sair():
   
    utils.banner("Saída")

    print(" Você está saindo do nosso sistema bancário.")
    print(" Obrigado por ser nosso cliente.")
    print(" Volte sempre!")
    print("".center(50, "*"))
    print()

# Operação de depósito.


def operacao_deposito(saldo, extrato, /):

    utils.banner("Depósito")

    valor = float(input(" Informe o valor do depósito: "))

    if valor > 0.0:
        saldo += valor
        extrato += f" Depósito: \t\t +R$ {valor:.2f}\n"
        print()
        print(f" Depósito: +R$ {valor:.2f}")
        print()
        print(" AVISO: Operação realizada com sucesso!")
    else:
        print()
        print(" ERRO: Operação falhou!")
        print("       Valor inserido é inválido.")
    return saldo, extrato


# Operação de saque.
def operacao_saque(*,
                   saldo,
                   extrato,
                   saques_numero_por_dia,
                   saques_limite_por_dia,
                   saques_limite_valor
                   ):

   
    utils.banner("Saque")

    valor = float(input(" Informe o valor do saque: "))
    # Verifica se existe saldo para realizar o saque.
    if valor > saldo:
        print()
        print(" ERRO: Operação não realizada!")
        print("       Saldo insuficiente.")
    # Verifica se o valor sacado é maior que o limite de saque.
    elif valor > saques_limite_valor:
        print()
        print(" ERRO: Operação não realizada!")
        print(
            f"       Saques devem ser menores ou iguais a: R$ {saques_limite_valor:.2f}.")
    # Verifica se o número de saque por dia já foi realizados.
    elif saques_numero_por_dia >= saques_limite_por_dia:
        print()
        print(" ERRO: Operação não realizada!")
        print(
            f"       Já foram realizados os {saques_limite_por_dia} saques diários.")
    # Realiza operação de saque.
    elif valor > 0.0:
        saldo -= valor
        extrato += f" Saque: \t\t -R$ {valor:.2f}\n"
        saques_numero_por_dia += 1
        print(f" Saque: -R$ {valor:.2f}")
        print()
        print(" AVISO: Operação realizada com sucesso!")
    # Outros erros.
    else:
        print()
        print(" ERRO: Operação não realizada!")
        print("       Valor inserido é inválido.")

    return saldo, extrato, saques_numero_por_dia



# Operação de extrato
def operacao_extrato(saldo, /, *, extrato):
    utils.banner("Extrato")

    print(" Operação \t\t Valor")
    print("".center(50, "-"))
    print(" Não foram realizadas movimentações." if not extrato else extrato)
    print("".center(50, "-"))
    print(f" Saldo disponível:\tR$ {saldo:.2f}")
    print("".center(50, "*"))


# Cria nova contas dos usuários
def operacao_criar_conta(agencia_numero, usuarios, contas):
    utils.banner("Nova conta")

    cpf = input(" Informe o CPF (somente digitos): ")

    if not cpf_br.verifica_cpf(cpf):
        return
    
    existe_usuario = filtrar_usuario(cpf, usuarios)
    if existe_usuario:
        conta_numero = f"{random.randint(10000,99999)}-{random.randint(0,9)}"
        contas.append({
            "agencia_numero": agencia_numero,
            "conta_numero": conta_numero,
            "usuario": existe_usuario})
        print("".center(50, "-"))
        print(f" C/C \t\t Titular")
        print("".center(50, "-"))
        print(f" {conta_numero} \t {existe_usuario['nome']}")
        print("".center(50, "-"))
        print(" AVISO: Operação realizada com sucesso!")
    else:        
        print()
        print(" ERRO: Operação não realizada!")
        print("       Não existe um usuário com este CPF.")
        


# Lista contas dos usuários
def operacao_listar_contas(contas):
    utils.banner("Lista de contas")
  
    print(f" Agência \t C/C \t\t Titular")
    print("".center(50, "-"))

    if len(contas) != 0:
        for conta in contas:            
            print(f" {conta['agencia_numero']} \t\t {conta['conta_numero']} \t {conta['usuario']['nome']}")
        print("".center(50, "*"))
    else:
        print()
        print(" ERRO: Operação não realizada!")
        print("       Não existem contas cadastradas.")



# Criar novo usuários.
def operacao_criar_usuario(usuarios):
    utils.banner("Novo Usuário")

    cpf = input(" Informe o CPF (somente digitos): ")
    
    if not cpf_br.verifica_cpf(cpf):
        return
    
    existe_usuario = filtrar_usuario(cpf, usuarios)
    if existe_usuario:
        print()
        print(" ERRO: Operação não realizada!")
        print("       Já existe um usuário com este CPF.")
        return
    nome = input(" Nome do usuário: ")
    data_nascimento = input(" Data de nascimento (dd-mm-aaa): ")
    endereco = input(
        " Informe o endereço (logradouro, nro, bairro, cidade/sigla estado): ")
    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })
    print()
    print(" AVISO: Operação realizada com sucesso!")

# Lista contas dos usuários
def operacao_listar_usuarios(usuarios):
    utils.banner("Lista de usuários")

    if len(usuarios) != 0:
        for usuario in usuarios:            
            print(f" Nome:       {usuario['nome']}")
            print(f" CPF:        {cpf_br.formata_cpf(usuario['cpf'])}")
            print(f" Nascimento: {usuario['data_nascimento']}")
            print(f" Endereço:   {usuario['endereco']}")
            print("".center(50, "-"))
        print("".center(50, "*"))
    else:
        print()
        print(" ERRO: Operação não realizada!")
        print("       Não existem usuários cadastrados.")



# Verifica se usuários já existe no sistema.
def filtrar_usuario(cpf, usuarios):
       
    usuario_filtrados = [
        usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuario_filtrados[0] if usuario_filtrados else None


def lista_usuarios():
    return [
        {"nome": "Cláudio André Mergen Taffarel", "data_nascimento": "08-04-1966","cpf":"17409488239","endereco": "Rua Nova, 28, Osasco, São Paulo/SP"},
        {"nome": "Jorge de Amorim Campos", "data_nascimento": "17-08-1964","cpf":"45517115276","endereco": "Rua Velha, 35, Osasco, São Paulo/SP"},
        {"nome": "Ricardo Roberto Barreto da Rocha", "data_nascimento": "11-09-1962","cpf":"76142322160","endereco": "Rua das Flores, 21, Osasco, São Paulo/SP"},
        {"nome": "Ronaldo Rodrigues de Jesus", "data_nascimento": "19-06-1965","cpf":"68576189259","endereco": "Rua da Paz, 08, Osasco, São Paulo/SP"},
        {"nome": "Mauro da Silva Gomes", "data_nascimento": "12-01-1968","cpf":"79543123306","endereco": "Avenida Luiz XIV, 05, Osasco, São Paulo/SP"},
        {"nome": "Cláudio Ibraim Vaz Leal", "data_nascimento": "04-04-1964","cpf":"41138742716","endereco": "Rua Nova, 28, Osasco, São Paulo/SP"},
        {"nome": "José Roberto Gama de Oliveira", "data_nascimento": "16-02-1964","cpf":"79319865043","endereco": "Rua Bahia, 45, Osasco, São Paulo/SP"},
        {"nome": "Carlos Caetano Bledorn Verri", "data_nascimento": "31-10-1963","cpf":"28602486502","endereco": "Rua PortugAl, 56, Osasco, São Paulo/SP"},
        {"nome": "Crizam César de Oliveira Filho", "data_nascimento": "17-06-1967","cpf":"09006138908","endereco": "Rua Canindé, 30, Osasco, São Paulo/SP"},
        {"nome": "Raí Souza Vieira de Oliveira", "data_nascimento": "15-05-1965","cpf":"34460661870","endereco": "Rua Padre José, 45, Osasco, São Paulo/SP"},
        {"nome": "Romário de Souza Faria", "data_nascimento": "19-01-1966","cpf":"12345678909","endereco": "Rua São João, 14, Osasco, São Paulo/SP"},
        ]

def lista_contas():
    return [
        {"agencia_numero":"0001","conta_numero":"30530-5","usuario":{"nome": "Cláudio André Mergen Taffarel", "data_nascimento": "08-04-1966","cpf":"17409488239","endereco": "Rua Nova, 28, Osasco, São Paulo/SP"}},
        {"agencia_numero":"0001","conta_numero":"66984-1","usuario":{"nome": "Jorge de Amorim Campos", "data_nascimento": "17-08-1964","cpf":"45517115276","endereco": "Rua Velha, 35, Osasco, São Paulo/SP"}},
        {"agencia_numero":"0001","conta_numero":"34907-5","usuario":{"nome": "Ricardo Roberto Barreto da Rocha", "data_nascimento": "11-09-1962","cpf":"76142322160","endereco": "Rua das Flores, 21, Osasco, São Paulo/SP"}},
        {"agencia_numero":"0001","conta_numero":"27966-3","usuario":{"nome": "Ronaldo Rodrigues de Jesus", "data_nascimento": "19-06-1965","cpf":"68576189259","endereco": "Rua da Paz, 08, Osasco, São Paulo/SP"}},
        {"agencia_numero":"0001","conta_numero":"98778-3","usuario":{"nome": "Mauro da Silva Gomes", "data_nascimento": "12-01-1968","cpf":"79543123306","endereco": "Avenida Luiz XIV, 05, Osasco, São Paulo/SP"}},
        {"agencia_numero":"0001","conta_numero":"20097-0","usuario":{"nome": "Cláudio Ibraim Vaz Leal", "data_nascimento": "04-04-1964","cpf":"41138742716","endereco": "Rua Nova, 28, Osasco, São Paulo/SP"}},
        {"agencia_numero":"0001","conta_numero":"83793-1","usuario":{"nome": "José Roberto Gama de Oliveira", "data_nascimento": "16-02-1964","cpf":"79319865043","endereco": "Rua Bahia, 45, Osasco, São Paulo/SP"}},
        {"agencia_numero":"0001","conta_numero":"73547-6","usuario":{"nome": "Carlos Caetano Bledorn Verri", "data_nascimento": "31-10-1963","cpf":"28602486502","endereco": "Rua PortugAl, 56, Osasco, São Paulo/SP"}},
        {"agencia_numero":"0001","conta_numero":"94145-4","usuario":{"nome": "Crizam César de Oliveira Filho", "data_nascimento": "17-06-1967","cpf":"09006138908","endereco": "Rua Canindé, 30, Osasco, São Paulo/SP"}},
        {"agencia_numero":"0001","conta_numero":"75650-0","usuario":{"nome": "Raí Souza Vieira de Oliveira", "data_nascimento": "15-05-1965","cpf":"34460661870","endereco": "Rua Padre José, 45, Osasco, São Paulo/SP"}},
        {"agencia_numero":"0001","conta_numero":"34233-9","usuario":{"nome": "Romário de Souza Faria", "data_nascimento": "19-01-1966","cpf":"12345678909","endereco": "Rua São João, 14, Osasco, São Paulo/SP"}},
        ]

# Inicio do programa
main()
