import pandas as pd


negrito, reset = '\033[1m', '\033[0m'
azul, vermelho, verde = '\033[34m', '\x1b[38;5;9m', '\x1b[38;5;10m'


def create_excel(path, data):
    '''
    Esta função cria arquivos com base no caminho e do ``dicionário`` passada como ``parâmetro``.
    
    Args:
        path(str): Refere-se ao caminho onde o arquivo ``Excel`` será armazenado
        data(dict[list]): Refere-se ao ``dicionário`` que será passada para o arquivo ``Excel``.
    '''
    try:
        df = pd.DataFrame(data)
        df.to_excel(path, index=False)
        
    except OSError:
        print(f'\n{vermelho}❌ [Erro] Não foi possivel criar o arquivo, pois o caminho "{path}" não foi encontrado.{reset}\n')
        
    except (pd.errors.ParserError, pd.errors.EmptyDataError) as ex:
        print(f'\n{vermelho}❌ [Erro] {ex}{reset}\n')
        
    except Exception as ex: 
        print(f'\n{vermelho}❌ {ex}{reset}\n')

    
def open_excel(path):
    '''
    Esta ``função`` **lê** arquivos ``.XLSX`` com base no **caminho** especificado.
    
    Args:
        path(str): Refere-se ao caminho do arquivo ``Excel``
    
    Returns:
        pandas.core.frame.DataFrame: Retorna os dados em formato de dataframe.
    '''
    try:
        return pd.read_excel(path)
    
    except FileNotFoundError:
        print(f'\n{vermelho}❌ [Erro] Não foi possivel realizar a leitura do arquivo, pois o caminho "{path}" não foi encontrado.{reset}\n')
    
    except Exception as ex:
        print(f'\n{vermelho}❌ {ex}{reset}\n')


def merge_files(df1, df2, column):
    '''
    Esta ``função`` **junta** dois ``dataframes`` com base no ``id``.
    
    Args:
        df1(pandas.core.frame.DataFrame): Refere ao ``dataframe`` que será **juntado** com o **segundo**.
        df2(pandas.core.frame.DataFrame): Refere ao ``dataframe`` que será **juntado** com o **primeiro**.
        column(str): Refere-se ao nome da coluna que irá ser alvo da junção.
    
    Returns: 
        pandas.core.frame.DataFrame: Retorna os dois ``dataframes`` juntos com base no ``id``.   
    '''
    try:
        merged_files = df1.merge(df2, how='left', on=column)
        print(f'\n{negrito}{verde}✅ Os arquivos foram combinados com sucesso!{reset}\n')
        return merged_files
    
    except KeyError as ex:
        print(f'\n{vermelho}❌ [Erro] Não foi possível combinar os arquivos, pois a coluna "{column}" é inválida.{reset}\n')
        
    except TypeError as ex:
        print(f'\n{vermelho}❌ [Erro] Não foi possível combinar os arquivos, pois um ou mais arquivos estão nulos.{reset}\n')
    
    except Exception as ex:
        print(f'\n{vermelho}❌ {ex}{reset}\n')
    

print(f'''{azul}
 ▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓  
 ▓▓   ▓▓     ▓▓       ▓▓   ▓▓  
 ▓▓▓▓▓▓▓     ▓▓       ▓▓▓▓▓▓▓ 
 ▓▓   ▓▓     ▓▓            ▓▓
 ▓▓   ▓▓     ▓▓    ▄  ▓▓▓▓▓▓▓    
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{reset}''')      
# Criação dos arquivos Excel    
create_excel('AT.9/clients.xlsx', {'client_id':[1, 2, 3],'name':['Jonathan', 'Barbara', 'Mary']})
create_excel('AT.9/shopping_list.xlsx', {'product_id':[1, 2, 3, 4, 5], 'product':['Laptop', 'Headset', 'Keyboard', 'Videogame', 'Cellphone'], 'client_id':[1, 1, 1, 2, 3]})

# Leitura dos arquivos Excel
clients_excel = open_excel('AT.9/clients.xlsx')
shopping_list_excel = open_excel('AT.9/shopping_list.xlsx')

# Arquivos Excel combinados em um dataframe
merged_df = merge_files(clients_excel, shopping_list_excel, 'client_id')

# Dataframe dos arquivos combinados salvos em um arquivo Excel
create_excel('AT.9/clients_shopping.xlsx', merged_df)
