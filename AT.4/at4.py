livro1, livro2, livro3, livro4  = ('Matéria Escura', 'Brake Crouch', 2016), ('Refactoring: Improving the Design of Existing Code', 'Martin Fowler', 2018), ('Clean Code', 'Robert C. Martin', 2008), ('O Pequeno Príncipe', 'Antoine de Saint-Exupéry', 1943)

biblioteca = []


negrito, reset = '\033[1m', '\033[0m'
azul, ciano = '\033[34m', '\x1b[38;5;37m'


def add_biblioteca(livros):
    '''
    Esta função adiciona cada **livro** na lista ``biblioteca``.
    
    Args:
        livros(tuple[tuple]): Refere se a uma tupla com tuplas que tem informações de livros.
    
    '''
    for livro in livros:
        biblioteca.append(livro)
    
print(f'''{azul}
 ▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓   ▓▓  ▓▓
 ▓▓   ▓▓     ▓▓      ▓▓  ▓▓
 ▓▓▓▓▓▓▓     ▓▓      ▓▓▓▓▓▓ 
 ▓▓   ▓▓     ▓▓          ▓▓
 ▓▓   ▓▓     ▓▓    ▄     ▓▓
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{reset}''')     
# Adição de livros em biblioteca    
add_biblioteca((livro1, livro2, livro3, livro4))    
print(f'\n📚 {reset}{negrito}Biblioteca: {ciano}{biblioteca}{reset}\n')
