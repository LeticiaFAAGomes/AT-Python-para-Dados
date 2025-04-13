import re
import urllib.request

from bs4 import BeautifulSoup

url = 'http://quotes.toscrape.com/'

response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')

soup = BeautifulSoup(html, 'html.parser')

quotes = soup.find_all('div', class_= 'quote')

padrao_limpeza = re.compile(r'[^\\s]')

palavra_chave = "life"

texts = [quote.get_text() for quote in soup.find_all('span', class_='text')]
authors = [author.get_text() for author in soup.find_all('small', class_='author')]
keywords = [key['content'] for key in soup.find_all('meta', class_='keywords')]


print(f'''\033[34m
 ▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓     ▓▓▓▓    ▓▓▓▓▓▓  
 ▓▓   ▓▓     ▓▓          ▓▓    ▓▓
 ▓▓▓▓▓▓▓     ▓▓          ▓▓    ▓▓▓▓▓▓
 ▓▓   ▓▓     ▓▓          ▓▓        ▓▓
 ▓▓   ▓▓     ▓▓    ▄   ▓▓▓▓▓▓  ▓▓▓▓▓▓
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m\n''') 

c = 0
for text in texts:
    if palavra_chave in keywords[c]:
        print(f"Citação (filtrada por palavra-chave '{palavra_chave}'): {text}\nAutor: {authors[c]}\n")
    c += 1
