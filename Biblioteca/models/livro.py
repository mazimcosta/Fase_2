

class Livro:

    def __init__(self,autor,titulo,status='disponivel'):

        if not isinstance(autor,str):
            raise ValueError('Autor invalido')
        
        autor=autor.strip()

        if not autor:
            raise ValueError('Autor invalido')
        
        if not isinstance(titulo,str):
            raise ValueError('Titulo invalido')
        
        titulo=titulo.strip()

        if not titulo:
            raise ValueError('Titulo invalido')
        
        if status not in ['disponivel','emprestado']:
            raise ValueError('Status invalido')
        
        self.autor=autor
        self.titulo=titulo
        self.__status=status

    @property
    def status(self):
        return self.__status
    
    def emprestar(self):
        if self.status != 'disponivel':
            raise ValueError('O livro esta indisponivel')
        
        self.__status='emprestado'

    def devolver(self):
        if self.status != 'emprestado':
            raise ValueError('O livro esta disponivel')
        
        self.__status='disponivel'
    
    