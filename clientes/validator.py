def cpf_valido(numero_do_cpf):
    """Validador do campo CPF"""
    return len(numero_do_cpf) == 11

def nome_valido(nome):
    """Validador do campo nome"""
    return nome.isalpha()

def rg_valido(numero_do_rg):
    """Validador do campo RG"""
    return len(numero_do_rg) == 9

def celular_valido(numero_do_celular):
    """Validador do campo celular"""
    return len(numero_do_celular) >= 11