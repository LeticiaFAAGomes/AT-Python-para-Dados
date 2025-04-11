import pandas as pd
from time import sleep


negrito, reset = '\033[1m', '\033[0m'
azul, vermelho, verde = '\033[34m', '\x1b[38;5;9m', '\x1b[38;5;10m'


measurements = {'data_medicao': ['2025-02-25', '2025-01-25', '2025-03-25'], 
                  'nivel_pm2.5': ['37µg/m³', '32µg/m³', '36µg/m³'],
                  'nivel_pm10': ['54µg/m³', '43µg/m³', '52µg/m³'],
                  'qualidade_ar': [160, 150, 100]
}


def create_excel(path, data):
    '''
    Esta função cria arquivos com base no caminho e do ``dicionário`` passada como ``parâmetro``.
    
    Args:
        path(str): Refere-se ao caminho onde o arquivo ``Excel`` será armazenado
        data(dict[list]): Refere-se ao ``dicionário`` que será passada para o arquivo ``Excel``.
    '''
    try:
        df = pd.DataFrame(data)
        df.to_excel(f'AT.10/{path}', index=False)
        
    except OSError:
        print(f'\n{vermelho}❌ [Erro] Não foi possivel criar o arquivo, pois o caminho "{path}" não foi encontrado.{reset}\n')
        
    except (pd.errors.ParserError, pd.errors.EmptyDataError) as ex:
        print(f'\n{vermelho}❌ [Erro] {ex}{reset}\n')
        
    except Exception as ex: 
        print(f'\n{vermelho}❌ [Erro] {ex}{reset}\n')
    
    
def open_excel(path):
    '''
    Esta ``função`` **lê** arquivos ``.XLSX`` com base no **caminho** especificado.
    
    Args:
        path(str): Refere-se ao caminho do arquivo ``Excel``
    
    Returns:
        dict: Retorna os dados em formato de ``dicionário``
    '''
    try:
        return pd.read_excel(path).to_dict(orient='records')
    
    except FileNotFoundError:
        print(f'\n{vermelho}❌ [Erro] Não foi possivel realizar a leitura do arquivo, pois o caminho "{path}" não foi encontrado.{negrito}{reset}\n')
    
    except Exception as ex:
        print(f'\n{vermelho}❌ [Erro] {ex}{reset}\n')

    
    
def check_air(data):
    '''
    Esta função identifica falhas em medições de qualidade do ar e adiciona uma nova coluna para as falhas.
    
    Args:
        data(dict): Refere-se aos dados das medições de qualidade do ar.

    '''
    fail = []
    
    if (data):
        print(f'\n{reset}{negrito}⏳ Verificando por falhas...{reset}')
        for row in data:
            if (int(row['nivel_pm2.5'][:2]) and int(row['nivel_pm10'][:2]) > 50):
                row['motivo_falha'] = 'Níveis de poluição elevados.'
                    
            if (row['qualidade_ar'] > 150):
                row['motivo_falha'] = 'Poluição não saudável.'
                
            if ('motivo_falha' in row):
                fail.append(row)
                
        create_excel('falhas_medicao.xlsx', fail)
        sleep(3)
        print(f'\n{verde}{negrito}✅ Arquivo Excel criado com sucesso!{reset}\n')


print(f'''{azul}
 ▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓     ▓▓▓▓    ▓▓▓▓▓▓▓
 ▓▓   ▓▓     ▓▓          ▓▓    ▓▓   ▓▓
 ▓▓▓▓▓▓▓     ▓▓          ▓▓    ▓▓   ▓▓
 ▓▓   ▓▓     ▓▓          ▓▓    ▓▓   ▓▓
 ▓▓   ▓▓     ▓▓    ▄   ▓▓▓▓▓▓  ▓▓▓▓▓▓▓
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{reset}''')  
# Criação de arquivo Excel
create_excel('medicao.xlsx', measurements)

# Leitura de arquivo Excel
measurement = open_excel('AT.10/medicao.xlsx')

# Resultado das falhas na medição
check_air(measurement)
