import re
from validate_docbr import CPF

def cpf_valido(numero_do_cpf):
    """Validador do campo CPF"""
    cpf = CPF()
    return cpf.validate(numero_do_cpf)

def nome_valido(nome):
    """Validador do campo nome"""
    return nome.isalpha()

def rg_valido(numero_do_rg):
    """Validador do campo RG"""
    return len(numero_do_rg) == 9

def celular_valido(numero_do_celular):
    """Validador do campo celular"""
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resultado = re.findall(modelo, numero_do_celular)
    return resultado