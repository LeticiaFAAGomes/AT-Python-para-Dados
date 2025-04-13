from bs4 import BeautifulSoup
import requests


negrito, reset = '\033[1m', '\033[0m'
azul, vermelho, verde = '\033[34m', '\x1b[38;5;9m', '\x1b[38;5;10m'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkit/537.36 (HTML. like Gako) Chrome/91.0.4472.124 Safari/537.36'}


def find_url(url):
    '''
    Esta função permite que o Python acesse o HTML da página e esteja apto a manipulá-lo com BeautifulSoup.
    
    Args:
        url(str): Refere-se a URL a ser acessada.
    
    Returns:
        bs4.BeautifulSoup: Retorna o objeto BeautifulSoup que torna o HTML apto a ser manipulado.
    '''
    html = requests.get(url, headers=headers).content
    return BeautifulSoup(html, 'html.parser')


def web_scraping(tag, attr_type, attr, slicing=None):
    '''
    Esta função encontra o texto elemento HTML com base em sua tag, seu tipo de atributo e seu nome de atributo.
    
    Args:
        tag(str): Refere-se ao nome da tag a ser encontrada.
        attr_type(str): Refere-se ao tipo de atributo da tag a ser encontrada.
        attr(str): Refere-se ao nome do atributo da tag a ser encontrada.
        slicing(None/int): Refere-se a decisão entre a necessidade de realizar slicing no texto de um elemento.
    
    Returns:
        str: Retorna o texto da tag mencionada. 
    '''
    try:
        return soup.find(tag, {attr_type:attr}).get_text(strip=True)[slicing:]
    
    except AttributeError as ex:
        print(f'\n{vermelho}❌ [Erro] O elemento {tag} não foi encontrado.{reset}\n')

print(f'''{azul}
 ▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓     ▓▓▓▓    ▓▓▓▓▓▓  
 ▓▓   ▓▓     ▓▓          ▓▓    ▓▓
 ▓▓▓▓▓▓▓     ▓▓          ▓▓    ▓▓▓▓▓▓
 ▓▓   ▓▓     ▓▓          ▓▓    ▓▓  ▓▓
 ▓▓   ▓▓     ▓▓    ▄   ▓▓▓▓▓▓  ▓▓▓▓▓▓
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{reset}''') 

print(f"\n{negrito}{'-'*35} TENTATIVA DE WEBSCRAPING {'-'*35}{reset}\n")

# HTML apto a ser manipulado
soup = find_url('https://www.amazon.com.br/Web-Scraping-Python-Ryan-Mitchell/product-reviews/1491985577/ref=cm_cr_unknown?ie=UTF8&reviewerType=all_reviews&pageNumber=1&filterByStar=five_star')
print('HTML da Amazon:\n')
print(soup.prettify(formatter='minimal'))

# Captura do nome do livro
title = web_scraping('div', 'class', 'a-row product-title')
print(f'📕 Titulo: {vermelho}{negrito}{title}{reset}')

# Captura do autor do livro
author = web_scraping('div', 'class', 'a-row product-by-line', 3)
print(f'👤 Autor: {vermelho}{negrito}{author}{reset}')

print(f"\n{negrito}{'-'*35} SIMULAÇÃO {'-'*35}")
# Simulação do webscraping caso o html não estivesse bloqueado
html_amazon = '''
<div class="a-fixed-left-grid-col product-info a-col-right" style="padding-left:2%;float:left;">
    <div class="a-row product-title">
        <h1 class="a-size-large a-text-ellipsis product-info-title">
            <a data-hook="product-link" class="a-link-normal" href="/Web-Scraping-Python-Ryan-Mitchell/dp/1491985577/ref=cm_cr_arp_d_product_top?ie=UTF8">Web Scraping with Python: Collecting More Data from the Modern Web</a>
        </h1>
    </div>
    <div class="a-row product-by-line">
        <div data-hook="cr-product-byline" class="a-section">
            <span id="cr-arp-byline" class="a-size-base">
                por<span class="a-letter-space"></span>
                <a class="a-size-base a-link-normal" href="/s?ie=UTF8&amp;field-author=Ryan+Mitchell&amp;search-alias=books">Ryan Mitchell</a>
            </span>
        </div>
    </div>
</div>
'''

# HTML apto a ser manipulado
soup = BeautifulSoup(html_amazon, 'html.parser')

# Captura do nome do livro
title = web_scraping('div', 'class', 'a-row product-title')
print(f'\n📕 Titulo: {verde}{title}{reset}\n')

# Captura do autor do livro
author = web_scraping('div', 'class', 'a-row product-by-line', 3)
print(f'{negrito}👤 Autor: {verde}{author}{reset}\n')

'''
Não foi possível realizar o web scraping, pois a Amazon bloqueia o acesso com métodos como CAPTCHA e a utilização do JavaScript 
para o carregamento dinâmico da página, além disso, a Amazon alerta os desenvolvedores com a seguinte mensagem no html:

<!--
    To discuss automated access to Amazon data please contact api-services-support@amazon.com.
    For information about migrating to our APIs refer to our Marketplace APIs at https://developer.amazonservices.com/ref=rm_c_sv, 
    or our Product Advertising API at https://affiliate-program.amazon.com/gp/advertising/api/detail/main.html/ref=rm_c_ac for advertising use cases.
-->

O que significa que a Amazon não permite a realização de raspagem de dados em sua página sem sua autorização.
'''
