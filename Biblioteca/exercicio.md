"Boss Fight Final — Fase 2

Objetivo:
Provar capacidade de aplicar arquitetura modular + persistência JSON sem copiar o Task Manager.

Projeto:
Biblioteca Persistente

Estrutura obrigatória:

biblioteca_persistente/
├── models/
│   └── livro.py
├── services/
│   └── biblioteca_service.py
├── repositories/
│   └── livro_repository.py
├── data/
│   └── livros.json
├── main.py
└── docs/

========================
MODEL
========================

Classe:
Livro

Atributos obrigatórios:

- titulo
- autor
- status

Status permitidos:

- disponivel
- emprestado

Responsabilidades da model:

- validar titulo
- validar autor
- validar status
- proteger estado interno

Métodos de domínio obrigatórios:

emprestar()
devolver()

Regras:

emprestar():
- só pode emprestar se status == disponivel
- se já estiver emprestado -> ValueError

devolver():
- só pode devolver se status == emprestado
- se já estiver disponível -> ValueError

========================
REPOSITORY
========================

Classe:
LivroRepository

Responsabilidade EXCLUSIVA:

persistência

Métodos obrigatórios:

salvar(livros)
carregar()

Contrato:

salvar():
- recebe lista de objetos Livro
- converte Livro -> dict
- salva em JSON

Formato esperado:

{
    'titulo': ...,
    'autor': ...,
    'status': ...
}

carregar():
- abre JSON
- converte dict -> Livro
- retorna lista de Livro

Se arquivo não existir:

return []

Regras:

Repository NÃO conhece service.
Repository NÃO aplica regra de negócio.
Repository NÃO usa input/print.

========================
SERVICE
========================

Classe:
BibliotecaService

Responsabilidades:

- CRUD
- regras de negócio
- integração com repository

Métodos obrigatórios:

criar_livro()
buscar_livro()
_buscar_livro_ou_erro()
emprestar_livro()
devolver_livro()
remover_livro()
listar_livros()
carregar()

Regras:

buscar_livro():
- retorna Livro ou None

_buscar_livro_ou_erro():
- retorna Livro ou levanta ValueError

Persistência obrigatória:

Depois de qualquer mutação:

- criar
- emprestar
- devolver
- remover

executar:

self._repositorio.salvar(self.listar_livros())

Regras arquiteturais:

Service usa repository.
Repository NÃO usa service.

Storage interno:

livros organizados por chave:

titulo -> objeto Livro

========================
MAIN
========================

Responsabilidade:

montar dependências

Fluxo:

instanciar LivroRepository
instanciar BibliotecaService(repository)

Criar fluxo de testes.

========================
TESTES OBRIGATÓRIOS
========================

Happy path:

- criar livro
- listar livros
- emprestar livro
- devolver livro
- remover livro

Persistência:

- criar livro
- fechar programa
- abrir programa
- verificar se carregou automaticamente

Testes destrutivos:

- livro duplicado
- livro inexistente
- emprestar livro já emprestado
- devolver livro disponível
- objeto inválido
- título inválido

========================
RESTRIÇÕES
========================

NÃO usar dataclass
NÃO usar custom exceptions
NÃO usar SQLite
NÃO usar FastAPI
NÃO usar ORM

Foco:

POO
arquitetura
repository pattern
persistência
serialização
desserialização
dependency injection simples

========================
CRITÉRIO DE APROVAÇÃO
========================

Só aprova se:

- arquitetura correta
- persistência funcionando
- responsabilidades separadas
- regras de negócio corretas
- JSON funcionando
- carregamento automático funcionando

Dificuldade:
9/10

Objetivo final:
encerrar oficialmente a Fase 2."