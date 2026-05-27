from models.task import Task

class TaskManager:

    def __init__(self,repositorio):

        self.__tarefas={}
        self.repositorio=repositorio
        self.carregar()

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
        
        tarefa_existe=self.buscar_tarefa(tarefa.titulo)
        
        
        if tarefa_existe is not None:
            raise ValueError('Tarefa ja incluida')
        
        self.__tarefas[tarefa.titulo]=tarefa
        self.repositorio.salvar(self.listar_tarefas())

    
    def _buscar_tarefa_ou_erro(self,titulo):

        tarefa=self.buscar_tarefa(titulo)
        if tarefa is None:
            raise ValueError('Tarefa inexistente')
        return tarefa
    
    def concluir_tarefa(self,titulo):
        tarefa=self._buscar_tarefa_ou_erro(titulo)
        tarefa.concluir()
        self.repositorio.salvar(self.listar_tarefas())

        
    def listar_tarefas(self):
        return list(self.__tarefas.values())

    def remover_tarefa(self,titulo):

        self._buscar_tarefa_ou_erro(titulo)
        del self.__tarefas[titulo]
        self.repositorio.salvar(self.listar_tarefas())
    
    def carregar(self):
        tarefas=self.repositorio.carregar()
        for tarefa in tarefas:
            self.__tarefas[tarefa.titulo]=tarefa
        
