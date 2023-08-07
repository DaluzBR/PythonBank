
# Verifica se o CPF passado é válido.
def verifica_cpf(cpf):
    # Verifica número de dígitos.
    if len(cpf) != 11:
        print()
        print(" ERRO: CPF inválido.")
        return False
    
    # Verifica se dígitos são números.
    for digit in cpf:
        try:
            int(digit)
        except ValueError:
            print()
            print(" ERRO: CPF inválido.")
            return False
    
    # Calcula dígitos verificadores.
    sum = 0
  
    cpf_number = cpf[0:9]
    cpf_dv = cpf[9:11]

    # Calcula dígito verificador 1.
    for i, digit in enumerate(cpf_number):
        sum+= (10-i)*int(digit)

    dv1 = 0 if (11-sum%11)>9 else 11-sum%11

    # Acrescenta o 1º digito vcrificados ao número do CPF.
    cpf_number = f"{cpf_number}{dv1}"

    # Calcula dígito verificador 2.
    sum = 0
    for i, digit in enumerate(cpf_number):
        sum+= (11-i)*int(digit)

    dv2 = 0 if (11-sum%11)>9 else 11-sum%11

    # Acrescenta o 2º digito vcrificados ao número do CPF.
    dv = f"{dv1}{dv2}"

    # Verifica dv calculado com dv do cpf.
    if dv == cpf_dv:
        return True 
    else:
        print()
        print(" ERRO: CPF inválido.")
        return False

# Formata um CPF comprovadamente válido.
def formata_cpf(cpf):
    return f"{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}"

