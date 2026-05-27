from models.task import Task
from services.task_service import TaskManager
from repositories.task_repository import TaskRepository

def fluxo_normal():
    repositorio=TaskRepository()
    
    gerenciador = TaskManager(repositorio)

    return gerenciador

