# Verifica se o CPF passado é válido.   
def check_cpf(cpf):
    # Verifica número de dígitos e se são todos números.
    if len(cpf) != 11 or not cpf.isdigit():
        return False

    # Calcula dígitos verificadores (dv).
    cpf_number = cpf[:9]
    cpf_dv = cpf[9:11]

    def calcula_dv(cpf_number):
        sum = 0
        for i, digit in enumerate(cpf_number):
            sum += (len(cpf_number) + 1 - i) * int(digit)
        return 0 if (11 - sum % 11) > 9 else (11 - sum % 11)
      

    dv1 = calcula_dv(cpf_number)
    cpf_number += str(dv1)
    dv2 = calcula_dv(cpf_number)


    calculated_dv = f"{dv1}{dv2}"

    return calculated_dv == cpf_dv


# Teste
def verifica_cpf(cpf):
    if check_cpf(cpf):
         return True 
    else:
        print()
        print(" ERRO: CPF inválido.")
        return False



# Formata um CPF comprovadamente válido.
def formata_cpf(cpf):
    return f"{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}"

