from models.livro import Livro
class  LivroService:


    def __init__(self,repositorio):

        self.__livros={}
        self.repositorio=repositorio
        self.carregar()

    def buscar_livro(self,titulo):
        if not isinstance(titulo,str):
            raise ValueError('Titulo invalido')
        titulo=titulo.strip()

        if not titulo:
            raise ValueError('Titulo invalido')
        
        return self.__livros.get(titulo)
    
    def buscar_livro_ou_erro(self,titulo):

        livro=self.buscar_livro(titulo)
        
        if livro is None:
            raise ValueError('Livro nao encontrado')
        return livro
    
    def criar_livro(self,livro):
        if not isinstance(livro,Livro):
            raise ValueError('Livro invalido')
        
        livro_existe= self.buscar_livro(livro.titulo)
        if livro_existe is not None:
            raise ValueError('Livro ja cadastrado')
        self.__livros[livro.titulo]=livro
        self.repositorio.salvar(self.listar_livros())

    
    def emprestar_livro(self,titulo):

        livro=self.buscar_livro_ou_erro(titulo)
        livro.emprestar()
        self.repositorio.salvar(self.listar_livros())

    
    
    def devolver_livro(self,titulo):

        livro=self.buscar_livro_ou_erro(titulo)
        livro.devolver()
        self.repositorio.salvar(self.listar_livros())

    
    def remover_livro(self,titulo):

       livro=  self.buscar_livro_ou_erro(titulo)

         del self.__livros[livro.titulo]
         self.repositorio.salvar(self.listar_livros())
    
    
    def listar_livros(self):
        return list(self.__livros.values())
    
    def carregar(self):
        livros=self.repositorio.carregar()

        for livro in livros:
            self.__livros[livro.titulo]=livro