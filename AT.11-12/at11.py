from sqlalchemy import create_engine, Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base


negrito, reset = '\033[1m', '\033[0m'
azul, verde = '\033[34m', '\x1b[38;5;10m'


Base = declarative_base()


class Client(Base):
    __tablename__ = 'client'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    
    shoppings = relationship('Shopping', back_populates='clients')
    
    
class Shopping(Base):
    __tablename__ = 'shoppings'
    
    id = Column(Integer, primary_key=True)
    product = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    client_id = Column(Integer, ForeignKey('client.id', ondelete='CASCADE'), nullable=False)
    
    clients = relationship('Client', back_populates='shoppings')



engine = create_engine('sqlite:///AT.11-12/shoppings.sqlite')
Base.metadata.create_all(engine)

if __name__ == '__main__':
    print(f'''{azul}
          
    ▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓     ▓▓▓▓     ▓▓▓▓
    ▓▓   ▓▓     ▓▓          ▓▓       ▓▓
    ▓▓▓▓▓▓▓     ▓▓          ▓▓       ▓▓
    ▓▓   ▓▓     ▓▓          ▓▓       ▓▓
    ▓▓   ▓▓     ▓▓    ▄   ▓▓▓▓▓▓   ▓▓▓▓▓▓
    ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{reset}''') 
    print(f'\n{verde}{negrito}✅ A base de dados foi criada com sucesso!{reset}\n')