from functools import reduce
from itertools import chain

livros = [
    {"id": 1, "titulo": "Python Funcional", "disponivel": True},
    {"id": 2, "titulo": "Paradigmas de Programação", "disponivel": False},
    {"id": 3, "titulo": "Introdução ao Python", "disponivel": True},
    {"id": 4, "titulo": "Estruturas de Dados", "disponivel": True},
]

usuarios = [
    {"id": 101, "nome": "Alice", "emprestimos": [2]},
    {"id": 102, "nome": "Bob", "emprestimos": []},
]

def buscar_livros_disponiveis(livros):
    return list(filter(lambda livro: livro["disponivel"], livros))

def listar_titulos(livros):
    return list(map(lambda livro: livro["titulo"], livros))

def emprestar_livro(usuarios, livros, id_usuario, id_livro):
    usuario = next(filter(lambda u: u["id"] == id_usuario, usuarios), None)
    livro = next(filter(lambda l: l["id"] == id_livro, livros), None)
    if usuario and livro and livro["disponivel"]:
        novos_livros = list(map(
            lambda l: {**l, "disponivel": False} if l["id"] == id_livro else l,
            livros
        ))
        novos_usuarios = list(map(
            lambda u: {**u, "emprestimos": u["emprestimos"] + [id_livro]} if u["id"] == id_usuario else u,
            usuarios
        ))
        return novos_usuarios, novos_livros
    return usuarios, livros

def total_livros_emprestados(usuarios):
    return reduce(lambda total, u: total + len(u["emprestimos"]), usuarios, 0)


livros_disponiveis = buscar_livros_disponiveis(livros)
titulos_disponiveis = listar_titulos(livros_disponiveis)
print("Livros disponíveis:", titulos_disponiveis)

usuarios, livros = emprestar_livro(usuarios, livros, 102, 3)
print("Total de livros emprestados:", total_livros_emprestados(usuarios))


def todos_emprestados(livros):
    if not livros:
        return True
    if livros[0]["disponivel"]:
        return False
    return todos_emprestados(livros[1:])

print("Todos os livros emprestados?", todos_emprestados(livros))
