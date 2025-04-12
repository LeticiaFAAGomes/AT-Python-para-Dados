from bs4 import BeautifulSoup
import requests


negrito, reset = '\033[1m', '\033[0m'
azul, ciano, vermelho  = '\033[34m', '\x1b[38;5;37m', '\x1b[38;5;9m'


def find_url(url):
    '''
    Esta função permite que o Python acesse o HTML da página e esteja apto a manipulá-lo com BeautifulSoup.
    
    Args:
        url(str): Refere-se a URL a ser acessada.
    
    Returns:
        bs4.BeautifulSoup: Retorna o objeto BeautifulSoup que torna o HTML apto a ser manipulado.
    '''
    try:
        html = requests.get(url).content
        return BeautifulSoup(html, 'html.parser')
    
    except requests.exceptions.ConnectionError:
        print(f'{vermelho}❌ [Erro] Não foi possível estabelecer a conexão com o servidor.')
        
    except AttributeError as ex:
        print(f'{vermelho}❌ [Erro] {ex}')


def find_tags(tag):
    '''
    Esta função encontra tags HTML com base no nome da tag.
    
    Args:
        tag(str): Refere-se ao nome da tag.
    
    Returns:
        list(str): Retorna uma lista com o texto das tags HTML.
    ''' 
    try:
        return [tag.get_text() for tag in soup.find_all(tag)]
    
    except AttributeError as ex:
        print(f'{vermelho}❌ [Erro] {ex}')


def format_table(headers, datas):
    '''
    Esta ``função`` formata e ``imprime`` os cabeçalhos e dados da tabela.
    
    Args:
        headers(list[str]): Refere-se ao cabeçalho da tabela.
        datas(list[str]): Refere-se aos dados da tabela.
    '''
    if (headers and datas):
        return f'┏{'┅'*42}┓\n' + '┃ ' + '┃ '.join(f'{header:12}' for header in headers)  + ' ┃\n' + f'┠{'━'*42}┨\n' + '┃ ' + '┃ '.join(f'{data:12}' for data in datas) + ' ┃\n' + f'┗{'━'*42}┛\n'


print(f'''{azul}
 ▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓     ▓▓▓▓     ▓▓▓▓▓▓
 ▓▓   ▓▓     ▓▓          ▓▓         ▓▓
 ▓▓▓▓▓▓▓     ▓▓          ▓▓     ▓▓▓▓▓▓
 ▓▓   ▓▓     ▓▓          ▓▓         ▓▓
 ▓▓   ▓▓     ▓▓    ▄   ▓▓▓▓▓▓   ▓▓▓▓▓▓
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{reset}''') 

# HTML apto a ser manipulado
soup = find_url('https://www.gutenberg.org/browse/scores/top')

# Tabela formatada
formated = format_table(find_tags('th'), find_tags('td'))
if (formated): print(f'\n{negrito}{ciano}{formated}{reset}')
