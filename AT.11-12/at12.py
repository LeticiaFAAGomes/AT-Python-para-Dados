from at11 import *
from sqlalchemy import update
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker


negrito, reset = '\033[1m', '\033[0m'
vermelho, verde = '\x1b[38;5;9m', '\x1b[38;5;10m'


Session = sessionmaker(bind=engine)
session = Session()


def add_client(id, name, email):
    '''
    Esta ``função`` insere um novo cliente na tabela ``Clients``.
    
    Args:
        id(int): Refere-se ao ``id`` do cliente.
        name(str): Refere-se ao nome do cliente.
        email(str): Refere-se ao email do cliente.
    '''
    try:
        session.add(Client(id=id, name=name, email=email))
        session.commit()
        print(f'\n✅ {verde}{negrito}Cliente {name} foi adicionado(a) com sucesso!{reset}\n')
        
    except IntegrityError as ex:
        session.rollback()
        print(f'\n❌ {vermelho}[Erro de Integridade] {ex.orig}{reset}\n')
        
    finally:
        session.close()


def add_shopping(id, product, price, client_id):
    '''
    Esta ``função`` insere um novo produto na tabela ``Shopping``.
    
    Args:
        id(int): Refere-se ao ``id`` do produto.
        product(str): Refere-se ao nome do produto.
        price(float): Refere-se ao preco do produto.
        client_id(int): Refere-se ao id do cliente que comprou o produto.
    '''
    try:
        session.add(Shopping(id=id, product=product, price=price, client_id=client_id))
        session.commit()
        print(f'\n✅ {verde}{negrito}Compra de {product} do(a) cliente {session.get(Client, client_id).name} foi adicionada com sucesso!{reset}\n')
        
    except IntegrityError as ex:
        session.rollback()
        print(f'\n❌ {vermelho}[Erro de Integridade] {ex.orig}{reset}\n')
    
    finally:
        session.close()
        

def update_price(id, price):
    '''
    Esta função atualiza o valor de uma compra de produto com base no id do cliente.
    
    Args:
        id(int): Refere-se ao id do cliente.
        price(float): Refere-se ao preço a ser atualizado.
    '''
    try:
        session.execute(update(Shopping).where(Shopping.client_id == id).values(price=price))
        session.commit()
        print(f'\n✅ {verde}{negrito}Cliente {session.get(Client, id).name} teve sua compra atualizada para o preço de R$ {price:.2f}.{reset}\n')
        
    except IntegrityError as ex:
        session.rollback()
        print(f'\n❌ {vermelho}[Erro de Integridade] {ex.orig}{reset}\n')
        
    finally:
        session.close()


print(f'''{azul}
 ▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓     ▓▓▓▓     ▓▓▓▓▓▓
 ▓▓   ▓▓     ▓▓          ▓▓         ▓▓
 ▓▓▓▓▓▓▓     ▓▓          ▓▓     ▓▓▓▓▓▓
 ▓▓   ▓▓     ▓▓          ▓▓     ▓▓
 ▓▓   ▓▓     ▓▓    ▄   ▓▓▓▓▓▓   ▓▓▓▓▓▓
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{reset}''') 
# Adição de clientes
add_client(1, 'Letícia Gomes', 'leticia.gomes@email.com')
add_client(2, 'Maria Silva', 'maria.silva@email.com')
add_client(3, 'Edgar Ferraz', 'edgar.ferraz@email.com')
add_client(4, 'Débora Cedro', 'debora.cedro@email.com')
add_client(5, 'Caio Lopez', 'caio.lopez@email.com')

# Adição de compras
add_shopping(1, 'Laptop', 5000, 1)
add_shopping(2, 'LapTop', 7000, 2) # Compra de laptop de Maria Silva
add_shopping(3, 'Headset', 200, 3)
add_shopping(4, 'Camera', 5000, 3)
add_shopping(5, 'Headset', 100, 4)
add_shopping(6, 'PS4', 2400, 5)
add_shopping(7, 'God of War Ragnarök PS4', 170, 5)
add_shopping(8, "Resident Evil 7: Biohazard PS4", 130, 5)
add_shopping(9, "The Last of Us Part II PS4", 160, 5)

# Atualização de Maria Silva
update_price(2, 7500)
