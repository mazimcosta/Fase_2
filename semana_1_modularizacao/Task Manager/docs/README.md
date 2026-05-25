"""
FASE 2 | SEMANA 2 | BOSS FIGHT — TASK MANAGER CLI

OBJETIVO:
Provar transferencia real de conhecimento.

Neste projeto, voce NAO deve copiar mecanicamente o projeto bancario.
Voce deve aplicar os mesmos principios arquiteturais em um dominio diferente.

ARQUITETURA OBRIGATORIA:

task_manager/
├── models/
│   └── task.py
├── services/
│   └── task_service.py
├── docs/
└── main.py

DOMINIO:
Agora nao existe conta bancaria.
Agora existe tarefa.

ENTIDADE:
Task

ATRIBUTOS MINIMOS:
- titulo
- descricao
- status

STATUS POSSIVEIS:
- pendente
- concluida

MODEL (task.py):
Voce deve decidir quais comportamentos pertencem a propria tarefa.

Pergunta obrigatoria:
Uma tarefa deve saber se concluir sozinha?

Se a resposta for sim, implemente comportamento coerente.

SERVICE (task_service.py):
Responsavel por coordenar multiplas tarefas.

IMPLEMENTAR:

1. criar_tarefa(task)
Regras:
- aceitar apenas objetos Task
- rejeitar objetos invalidos
- raise ValueError em caso invalido
- nao permitir duplicidade (voce decide a chave)

2. buscar_tarefa(...)
Regras:
- retornar objeto Task se existir
- retornar None se nao existir

3. helper privado
Regras:
- obrigatorio usar helper privado para operacoes que exigem existencia da tarefa
- evitar duplicacao de validacao

4. concluir_tarefa(...)
Regras:
- localizar tarefa
- chamar comportamento da model
- NAO alterar atributos diretamente na service

ERRADO:
self.__tarefas[chave].status = 'concluida'

CERTO:
tarefa.concluir()

5. listar_tarefas()
Regras:
- retornar colecao com tarefas cadastradas

6. remover_tarefa(...)
Regras:
- remover tarefa existente
- levantar erro se nao existir

STORAGE:
Voce deve decidir entre:
- lista
OU
- dicionario

Mas precisa justificar tecnicamente.

MAIN.PY:
Estrutura obrigatoria:

- fluxo_normal()
- teste_erros()
- if __name__ == '__main__'

TESTES HAPPY PATH:
- criar tarefas
- listar
- concluir
- buscar
- remover

TESTES DESTRUTIVOS:
- tarefa duplicada
- tarefa inexistente
- objeto invalido
- concluir tarefa inexistente
- remover tarefa inexistente

REGRAS DE ARQUITETURA:
- sem input()
- sem print() dentro de model/service
- sem try/except dentro de model/service
- exceptions com ValueError
- separacao clara de responsabilidade
- evitar duplicacao
- aplicar helper privado corretamente

CRITERIO DE APROVACAO:
Projeto aprovado se houver:
- arquitetura correta
- model limpa
- service limpa
- helper privado coerente
- testes felizes
- testes destrutivos
- diario tecnico atualizado

DIFICULDADE:
8.5/10

PERGUNTA OBRIGATORIA ANTES DE CODAR:
Voce vai usar lista ou dicionario para armazenar tarefas?
Justifique tecnicamente.
"""