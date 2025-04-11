negrito, reset = '\033[1m', '\033[0m'
azul, ciano = '\033[34m', '\x1b[38;5;37m'


def contar_strings(lista_compras):
    '''
    Esta função conta quantas vezes cada ``string`` de uma lista aparece.
    
    Args: 
        lista_compras(list[str]): Refere-se a uma ``lista`` de compras.

    Returns:
        dict: Retorna um ``dicionário`` com as quantidades de cada caracteres.
    '''
    strings = {}
    
    for item in lista_compras:
        for string in item:
            if string.upper() not in strings:
                strings[string.upper()] = 0
            strings[string.upper()] += 1
            
    return strings
    
    
print(f'''{azul}
 ▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓     ▓▓▓▓
 ▓▓   ▓▓     ▓▓          ▓▓
 ▓▓▓▓▓▓▓     ▓▓          ▓▓
 ▓▓   ▓▓     ▓▓          ▓▓
 ▓▓   ▓▓     ▓▓    ▄   ▓▓▓▓▓▓
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{reset}''')    
# Contagem de strings
contagem = contar_strings(['Arroz', 'Feijão', 'Macarrão'])
print(f'\n📋 {negrito}Contagem: {ciano}{contagem}{reset}\n')
