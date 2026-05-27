
import json
from models.task import Task
class TaskRepository:

    def __init__(self,caminho_arquivo="Task Manager/data/tarefas.json"):

        self.caminho_arquivo=caminho_arquivo

    def salvar(self,tarefas):
        dados = []
        for tarefa in tarefas:
            dados.append({
                'titulo':tarefa.titulo,
                'descricao':tarefa.descricao,
                'status':tarefa.status
            })
        with open(self.caminho_arquivo,'w', encoding='utf-8') as arquivo:
            json.dump(dados,arquivo,ensure_ascii=False, indent=4)

    def carregar(self):
        
        tarefas=[]
        try:
            with open(self.caminho_arquivo,'r') as arquivo:
                dados=json.load(arquivo)
            for dado in dados:
                tarefa=Task(titulo=dado['titulo'],descricao=dado['descricao'],status=dado['status'])
                tarefas.append(tarefa)
        except FileNotFoundError:
            return []
        return tarefas