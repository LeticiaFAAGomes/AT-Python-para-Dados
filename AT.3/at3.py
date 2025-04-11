negrito, reset = '\033[1m', '\033[0m'
azul, vermelho, verde = '\033[34m', '\x1b[38;5;9m', '\x1b[38;5;10m'


def verificar_conjunto(palavra, letras):
    '''
    Esta ``função`` verifica se **palavra** está no ``conjunto`` de **letras**.
    
    Args:
        palavra(str): Refere-se a uma palavra fornecida.
        letras(set): Refere-se a um ``conjunto`` de letras aleatórias.
    
    Returns:
        bool: Retorna ``True`` se todos os caracteres de **palavra** estiverem em **letras** caso contrário ``False``
    
    '''
    return True if (set(palavra).issubset(letras)) else False


print(f'''{azul}
 ▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓     ▓▓▓▓▓▓
 ▓▓   ▓▓     ▓▓            ▓▓
 ▓▓▓▓▓▓▓     ▓▓        ▓▓▓▓▓▓ 
 ▓▓   ▓▓     ▓▓            ▓▓
 ▓▓   ▓▓     ▓▓    ▄   ▓▓▓▓▓▓
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{reset}''') 

# Verificação se conjunto está ou não no conjunto de letras
print(f'\n🏠 {reset}{negrito}Casa está contida em "ascehgr"? {verde}{verificar_conjunto('casa', set('ascehgr'))}{reset}')
print(f'👕 {reset}{negrito}Roupa está contida em "ascehgr"? {vermelho}{verificar_conjunto('roupa', set('ascehgr'))}{reset}')
print(f'🖥️  {reset}{negrito}Python está contido em "hpgthso"? {vermelho}{verificar_conjunto('roupa', set('ascehgr'))}{reset}\n')

