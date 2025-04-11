import pandas as pd


negrito, reset = '\033[1m', '\033[0m'
azul, vermelho, verde = '\033[34m', '\x1b[38;5;9m', '\x1b[38;5;10m'


def salvar_livros_via_json(livros, arquivo_json):
    '''
    Esta função salva a ``lista`` livros em um arquivo ``JSON``.
    
    Args:
        livros(list[tuple]): Refere-se a uma ``lista`` de ``tuplas`` quem contém informações de livros.
        arquivo_json(str): Refere-se ao caminho onde o arquivo ``JSON`` será armazenado.
        
    '''
    try:
        df = pd.DataFrame(livros, columns=['Livro', 'Autor', 'Ano'])
        df.to_json(arquivo_json, orient='records', force_ascii=False)
        print(f'\n{verde}{negrito}✅ Os livros foram salvos no caminho "{arquivo_json}" com sucesso!{reset}\n')
        
    except OSError as ex:
        print(f'\n{vermelho}{negrito}❌ [Erro] Caminho não encontrado: {ex}{reset}\n')
        
    except Exception as ex:
        print(f'\n{vermelho}{negrito}❌ [Erro] {ex}{reset}\n')
        
print(f'''{azul}
 ▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓  
 ▓▓   ▓▓     ▓▓       ▓▓  
 ▓▓▓▓▓▓▓     ▓▓       ▓▓▓▓▓▓ 
 ▓▓   ▓▓     ▓▓           ▓▓
 ▓▓   ▓▓     ▓▓    ▄  ▓▓▓▓▓▓   
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{reset}''')           
# Salvamento de arquivos via JSON        
salvar_livros_via_json([('Matéria Escura', 'Brake Crouch', 2016), ('Refactoring: Improving the Design of Existing Code', 'Martin Fowler', 2018), ('Clean Code', 'Robert C. Martin', 2008), ('O Pequeno Príncipe', 'Antoine de Saint-Exupéry', 1943)], 'AT.5/livros.json')
