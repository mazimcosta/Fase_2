

class Task:

    def  __init__(self,titulo,descricao,status='pendente'):

        if not isinstance(titulo,str):
            raise ValueError('Titulo invalido')
        
        titulo=titulo.strip()

        if not titulo:
            raise ValueError(' Titulo invalido')

        if not isinstance(descricao,str):
            raise ValueError('Descricao invalida')
        
        descricao=descricao.strip()

        if not descricao:
            raise ValueError('Descricao invalida')

        if status not in ['pendente','concluida']:
            raise ValueError('Status invalido')



        self.titulo=titulo
        self.descricao=descricao
        self.__status=status


    @property
    def status(self):
        return self.__status


    def concluir(self):
        if not self.__status=='pendente':
            raise ValueError('Tarefa ja concluida')
        
        self.__status='concluida'