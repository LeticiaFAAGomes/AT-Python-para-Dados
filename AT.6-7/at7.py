import pandas as pd


negrito, reset = '\033[1m', '\033[0m'
azul, vermelho, verde = '\033[34m', '\x1b[38;5;9m', '\x1b[38;5;10m'


def open_excel(path):
    '''
    Esta ``função`` **lê** arquivos ``.XLSX`` com base no **caminho** especificado.
    
    Args:
        path(str): Refere-se ao caminho do arquivo ``Excel``
    
    Returns:
        list[list]: Retorna os dados em formato de ``lista``
    '''
    try:
        return pd.read_excel(path).values.tolist()
    
    except FileNotFoundError:
        print(f'\n❌ {vermelho}[Erro] Não foi possivel realizar a leitura do arquivo, pois o caminho "{path}" não foi encontrado.{reset}\n')
    
    except Exception as ex:
        print(f'\n❌ {vermelho}{ex}\n')
    

def atualizar_idade(people, name, new_age, path):
    '''
    Esta ``função`` atualiza a **idade** de uma pessoa com base em seu **nome**.
    
    Args:
        people(list[list]): Refere-se a ``lista`` de pessoas.
        name(str): Refere-se ao **nome** da uma pessoa que terá a **idade** atualizada.
        new_age(int): Refere-se a **idade** a ser atualizada.
        path(str): Refere-se ao caminho onde o arquivo ``Excel`` será criado.
    '''
    found = False
    try:
        if (people):
            for index, person in enumerate(people):
                    if (name in person):
                        people[index][1] = new_age
                        found = True
                        saved = save_to_xlsx(path, people)
                        if (saved):
                            print(f'\n{verde}{negrito}✅ A idade de {name} foi atualizada com sucesso!{reset}\n')
                        break
            
            if not found:
                raise IndexError(f'\n{vermelho}❌ [Erro] {name} não foi encontrado na lista.{reset}\n')
            
    except (IndexError, TypeError, Exception) as ex:
        print(f'{vermelho}❌ {ex}{reset}')


def save_to_xlsx(path, update):
    '''
    Esta ``função`` cria um arquivo ``.XLSX`` com base no caminho do arquivo.
    
    Args:
        path(str): Refere-se ao caminho onde o arquivo ``Excel`` será criado.    
        update(list[list]): Refere-se a uma lista com a idade das pessoas atualizada.
    '''
    try:
        df = pd.DataFrame(update)
        df.to_excel(path, header=['name','age'], index=False)
        
        return True
    
    except OSError:
        print(f'\n{vermelho}❌ [Erro] Não foi possivel criar o arquivo, pois o caminho "{path}" não foi encontrado.{reset}\n')
        
    except Exception as ex:
        print(f'\n{vermelho}❌ [Erro] {ex}{reset}\n')
    
    
print(f'''{azul}
 ▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓   ▓▓▓▓▓▓  
 ▓▓   ▓▓     ▓▓          ▓▓  
 ▓▓▓▓▓▓▓     ▓▓         ▓▓ 
 ▓▓   ▓▓     ▓▓        ▓▓
 ▓▓   ▓▓     ▓▓    ▄   ▓▓   
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{reset}''')       
# Atualização da idade de uma pessoa e criação de um novo arquivo Excel    
atualizar_idade(open_excel('AT.6-7/people.xlsx'), 'Andrew', 40, 'AT.6-7/people_new.xlsx')
