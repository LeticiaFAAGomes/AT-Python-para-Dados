import pandas as pd


negrito, reset = '\033[1m', '\033[0m'
azul, vermelho, verde = '\033[34m', '\x1b[38;5;9m', '\x1b[38;5;10m'


def criar_excel(caminho):
    '''
    Esta ``função`` cria um arquivo ``.XLSX`` com base no **caminho** do arquivo.
    
    Args:
        caminho(str): Refere-se ao **caminho** onde o arquivo ``Excel`` será criado.
    '''
    dados = {'nome':['Letícia', 'Andrew', 'Jeniffer'], 'idade':[19, 30, 30]}
    df = pd.DataFrame(dados)
    try:
        df.to_excel(caminho, index=False)
        
    except OSError:
        print(f'\n{vermelho}{negrito}❌ [Erro] Não foi possivel criar o arquivo, pois o caminho "{caminho}" não foi encontrado.{reset}\n')
        
    except Exception as ex:
        print(ex)


def ler_excel(caminho):
    '''
    Esta ``função`` lê arquivos ``.XLSX`` com base no **caminho** especificado.
    
    Args:
        caminho(str): Refere-se ao caminho onde o arquivo ``Excel`` foi criado.
    
    Returns:
        list[list]: Retorna os dados em formato de ``lista``
    '''
    try:
        return pd.read_excel(caminho).values.tolist()
    
    except FileNotFoundError:
        print(f'\n{vermelho}{negrito}❌ [Erro] Não foi possivel realizar a leitura do arquivo, pois o caminho "{caminho}" não foi encontrado.{reset}\n')
    
    except Exception as ex:
        print(ex)


def calcular_media_idades(dados):
    '''
    Esta ``função`` calcula a media das idades da ``lista`` de pessoas.
    
    Args: 
        dados(list[list]): Refere-se aos dados de pessoas em formato de ``s``.
    
    Returns:
        float/str: Retorna a **média de idade** das pessoas ou uma **mensagem de erro**.
    '''
    if (dados):
        soma = 0
        for dado in dados:
            soma += dado[1]
        
        try:    
            return f'\n{verde}{negrito}✅ A média de idade do grupo de pessoas foi de {round(soma / len(dados), 1)} anos.{reset}\n'
        
        except ZeroDivisionError:
            print(f'\n{vermelho}{negrito}[Erro] Não foi possível realizar a média, pois não é possível dividir um número por zero.\n')

    return f'\n{vermelho}{negrito}❌ [Erro] Não foi possível fazer a média, pois os valores são nulos.{reset}\n'
    

print(f'''{azul}
 ▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓  
 ▓▓   ▓▓     ▓▓       ▓▓  
 ▓▓▓▓▓▓▓     ▓▓       ▓▓▓▓▓▓ 
 ▓▓   ▓▓     ▓▓       ▓▓  ▓▓
 ▓▓   ▓▓     ▓▓    ▄  ▓▓▓▓▓▓   
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{reset}''')   
# Criação de arquivo Excel
criar_excel('AT.6-7/people.xlsx')

# Calculo de média do arquivo criado.
media = calcular_media_idades(ler_excel('AT.6-7/people.xlsx'))
print(media)
