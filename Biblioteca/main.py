from models.livro import Livro
from services.biblioteca_service import LivroService
from repositories.livro_repository import LivroRepository


def fluxo_normal():
    repositorio=LivroRepository()
    livraria=LivroService(repositorio)
    livro1=Livro('JRR Tolkien','Senhor dos Aneis')
    livro2=Livro('Dostoievski','O idiota')
    livraria.criar_livro(livro1)
    livraria.criar_livro(livro2)
    livraria.emprestar_livro(livro1.titulo)
    livraria.devolver_livro(livro1.titulo)
    livraria.remover_livro(livro2.titulo)

fluxo_normal()
