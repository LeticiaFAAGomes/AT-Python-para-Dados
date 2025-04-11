negrito, reset = '\033[1m', '\033[0m'
azul, vermelho, verde = '\033[34m', '\x1b[38;5;9m', '\x1b[38;5;10m'


def verificar_antonimos(opostos, oposto1, oposto2):
    '''
    Esta ``função`` verifica se **duas palavras** são **opostas** ou **não** com base em um ``dicionário`` fornecido.
    
    Args:
        opostos(dict[str]): Refere-se ao ``dicionário`` de strings opostas.
        oposto1(str): Refere-se a primeira palavra a ser verificada.
        oposto2(str): Refere-se a segunda palavra a ser verificada.
    
    Returns:
        bool: Retorna ``True`` se  forem opostos caso contrário ``False``.
    '''
    return True if (opostos.get(oposto1) == oposto2 or opostos.get(oposto2) == oposto1) else False

print(f'''{azul}
 ▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓     ▓▓▓▓▓▓
 ▓▓   ▓▓     ▓▓            ▓▓
 ▓▓▓▓▓▓▓     ▓▓        ▓▓▓▓▓▓ 
 ▓▓   ▓▓     ▓▓        ▓▓
 ▓▓   ▓▓     ▓▓    ▄   ▓▓▓▓▓▓
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{reset}''')  
# Verificação de antônimos
print(f'\n💭 {negrito}Baixo é oposto de Alto? {verde}{verificar_antonimos({'muito':'pouco', 'alto': 'baixo', 'exagero':'escassez'}, 'baixo', 'alto')}')
print(f'💭 {reset}{negrito}Pouco é oposto de alto? {vermelho}{verificar_antonimos({'muito':'pouco', 'alto': 'baixo', 'exagero':'escassez'}, 'pouco', 'alto')}')
print(f'💭 {reset}{negrito}Pouco é oposto de muito? {verde}{verificar_antonimos({'muito':'pouco', 'alto': 'baixo', 'exagero':'escassez'}, 'pouco', 'muito')}{reset}\n')
