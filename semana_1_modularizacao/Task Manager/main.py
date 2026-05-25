from models.task import Task
from services.task_service import TaskManager


def fluxo_normal():
    gerenciador=TaskManager()

    tarefa1=Task('fazer flexoes','Oito vezes por semana')
    tarefa2=Task('estudar python','tipos,listas,dicionarios')
    tarefa3=Task('estudar para concurso','foco no banco do brasil')
    tarefa4=Task('fazer exercicios','Usar bicicleta ergometrica')

    gerenciador.criar_tarefa(tarefa1)
    gerenciador.criar_tarefa(tarefa2)
    gerenciador.criar_tarefa(tarefa3)
    gerenciador.criar_tarefa(tarefa4)
    gerenciador.listar_tarefas()
    gerenciador.concluir_tarefa(tarefa1)
    gerenciador.buscar_tarefa(tarefa2.titulo) 
    gerenciador.remover_tarefa(tarefa1)


def teste_erros():
    try:
        gerenciador.criar_tarefa(tarefa2)
    except ValueError as error:
        print(error)

    try:
        gerenciador.criar_tarefa(tarefa6)
    except ValueError as error:
        print(error)

    try:
        gerenciador.concluir_tarefa(tarefa1)
    except ValueError as error:
        print(error)

    try:
        gerenciador.remover_tarefa(tarefa1)
    except ValueError as error:
        print(error)

    
if __name__=='__main__':
    gerenciador,tarefa1,tarefa2,tarefa3,tarefa4=fluxo_normal()
    teste_erros(gerenciador,tarefa1,tarefa2,tarefa3,tarefa4)
    