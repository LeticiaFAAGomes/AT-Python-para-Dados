import pandas as pd


negrito, reset = '\033[1m', '\033[0m'
azul, vermelho, verde = '\033[34m', '\x1b[38;5;9m', '\x1b[38;5;10m'


turma = {'id':[1, 2, 3, 4], 'student':['Letícia', 'Arthur', 'Lucas', 'Augusto']}


def show_class(key):
    '''
    Esta ``função`` ``imprime`` o nome de todos os **estudantes** do ``dicionário`` **turma**.
    
    Args:
        key(str): Refere-se ao nome da chave do dicionário.
    '''
    try:
        students = 'Turma: '
        for student in turma[key]:
            students += f'{student}, '
        print(f'\n✏️  {negrito}{students[0:len(students)-2]}')
    except KeyError:
        print(f'\n{vermelho}❌ [Erro] Não foi possível localizar a chave "{key}" para listar a turma.{reset}\n')


def save_to_csv(path):
    '''
    Esta ``função`` **cria** um arquivo ``.CSV`` com base no **caminho** e ``dicionário`` da **turma**
    
    Args:
        path(str): Refere-se ao **caminho** onde o arquivo ``.CSV`` será criado.  
    '''
    try:
        df = pd.DataFrame(turma)
        df.to_csv(path, index=False)
        print(f'\n{verde}{negrito}✅ O arquivo CSV foi criado com sucesso!{reset}\n')
        
    except (pd.errors.ParserError, pd.errors.EmptyDataError, Exception) as ex:
        print(f'\n{vermelho}❌ [Erro] {ex}{reset}\n')

print(f'''{azul}
 ▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓  
 ▓▓   ▓▓     ▓▓       ▓▓   ▓▓  
 ▓▓▓▓▓▓▓     ▓▓       ▓▓▓▓▓▓▓ 
 ▓▓   ▓▓     ▓▓       ▓▓   ▓▓
 ▓▓   ▓▓     ▓▓    ▄  ▓▓▓▓▓▓▓    
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{reset}''')   
# Listagem de turma
show_class('student')

# Criação de arquivo CSV
save_to_csv('AT.8/class.csv')
