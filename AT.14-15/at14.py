from bs4 import BeautifulSoup
import requests


negrito, reset = '\033[1m', '\033[0m'
azul, vermelho, verde = '\033[34m', '\x1b[38;5;9m', '\x1b[38;5;10m'


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
        print(f'\n{vermelho}❌ [Erro] Não foi possível estabelecer a conexão com o servidor.{reset}\n')
        
    except AttributeError as ex:
        print(f'\n{vermelho}❌ [Erro] {ex}{reset}\n')


def find_tags(tag):
    '''
    Esta função encontra tags HTML com base no nome da tag.
    
    Args:
        tag(str): Refere-se ao nome da tag.
    
    Returns:
        tuple[list]:
            html(bs4.BeautifulSoup): Retorna uma lista com html manipulável.
            texto(str): Retorna uma lista com o texto das tags HTML.
    '''
    try:
        
        html, texto = [tag for tag in soup.find_all(tag)], [tag.get_text() for tag in soup.find_all(tag)]
        
        if (not html or not texto):
            raise AttributeError(f'\n{vermelho}❌ [Erro] Não foi possível realizar a captura dos dados, pois a tag "{tag}" é inválida.{reset}\n')
        
        return html[25:125], texto[25:125]

    except (AttributeError, Exception) as ex:
        print(f'\n{vermelho}❌ [Erro] {ex}{reset}\n')


def find_tag(url, links):
    '''
    Esta função encontra o href das tags âncoras.
    
    Args:
        url(str): Refere-se a URL a ser acessada.
        links(str): Refere-se a uma lista com html manipulável.
    
    Returns:
        list: Retorna uma lista com os links de cada livro.
    '''
    try:
        if (url and links):
            return [f'{url}{li.find('a')['href']}' for li in links]

    except AttributeError as ex:
        print(f'\n{vermelho}❌ [Erro] {ex}{reset}\n')
        
    except KeyError as ex:
        print(f'\n{vermelho}❌ [Erro] A chave {ex} é inválida.{reset}\n')


def format_list(titles, links):
    '''
    Esta ``função`` formata e ``imprime`` textos no formato **"[index]. [titulo] - Downloads: [qtd] Link: [url]"**
    
    Args:
        titles(list[str]): Refere-se aos titulos de cada livro
        links(list[str]): Refere-se aos links de cada livro.
    
    '''
    lista = []
    c = 0
    for title in titles:
        c += 1
        if title not in lista:
            lista.append(title)
            print(f'{c:4}. {title[:title.find('(')]}- Downloads: {title[title.find('(')+1:title.find(')')]}\n      Link: {links[c-1]}')


print(f'''{azul}
 ▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓     ▓▓▓▓    ▓▓  ▓▓
 ▓▓   ▓▓     ▓▓          ▓▓    ▓▓  ▓▓
 ▓▓▓▓▓▓▓     ▓▓          ▓▓    ▓▓▓▓▓▓
 ▓▓   ▓▓     ▓▓          ▓▓        ▓▓
 ▓▓   ▓▓     ▓▓    ▄   ▓▓▓▓▓▓      ▓▓
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{reset}\n''')             
          
# HTML apto a ser manipulado
soup = find_url('https://www.gutenberg.org/browse/scores/top')  

# Lista com html manipulável e lista com texto das tags HTML
listas = find_tags('li')
if (listas):
    formated, formated_text = listas

    # Lista com os links de cada livro
    links = find_tag('https://www.gutenberg.org/', formated)
    
    # Lista formatada
    format_list(formated_text, links)
