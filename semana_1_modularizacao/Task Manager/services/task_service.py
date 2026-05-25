from models.task import Task

class TaskManager:

    def __init__(self):

        self.__tarefas={}

    def buscar_tarefa(self,titulo):

        if not isinstance(titulo,str):
            raise ValueError('TItulo invalido')
        titulo=titulo.strip()
       
        if not titulo:
            raise ValueError('Titulo invalido')

        return self.__tarefas.get(titulo)
    
    def criar_tarefa(self,tarefa):
        if not isinstance(tarefa,Task):
            raise ValueError('Tarefa invalida')
        
        tarefa=self.buscar_tarefa(tarefa.titulo)
        
        if tarefa is not None:
            raise ValueError('Tarefa ja incluida')
        
        self.__tarefas[tarefa.titulo]=tarefa

    
    def _buscar_tarefa_ou_erro(self,titulo):

        tarefa=self.buscar_tarefa(titulo)
        if tarefa is None:
            raise ValueError('Tarefa inexistente')
        return tarefa
    
    def concluir_tarefa(self,tarefa):

        tarefa_existe=self._buscar_tarefa_ou_erro(tarefa.titulo)
        if tarefa_existe is not None:
            tarefa.concluir()

    def listar_tarefas(self):
        lista=[{titulo:tarefa} for titulo,tarefa in self.__tarefas.items()]
        return lista
    

    def remover_tarefa(self,tarefa):

        tarefa=self._buscar_tarefa_ou_erro(tarefa.titulo)
        del self.__tarefas[tarefa.titulo]
        
