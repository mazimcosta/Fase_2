# Diário Técnico — Fase 2 Backend Python

---

# Semana 1 — Modularização

---

## Dia 2 — BancoService + Integração + Testes Destrutivos

### O que construí
- Estruturei projeto modularizado:
  - `models/`
  - `services/`
  - `main.py`

- Criei a model `Conta`
- Criei a service `BancoService`
- Implementei:
  - `criar_conta()`
  - `buscar_conta()`
  - `transferir()`

- Fiz integração entre:
  - `main.py`
  - `Conta`
  - `BancoService`

---

### Conceitos aprendidos

#### Separação de responsabilidades
A classe `Conta` cuida apenas do próprio estado e comportamento:

- titular
- numero
- saldo
- depositar
- sacar

A classe `BancoService` coordena interações entre múltiplas contas:

- cadastrar conta
- buscar conta
- transferir valores
- validar existência de contas

---

#### Encapsulamento
Não devo manipular saldo diretamente.

Errado:

```python
conta._saldo -= valor
```

Correto:

```python
conta.sacar(valor)
```

---

#### Service Layer
A service funciona como coordenadora do sistema.

Ela não representa uma conta.

Ela gerencia o fluxo entre objetos.

---

#### Exceptions
Regras inválidas devem usar:

```python
raise ValueError(...)
```

Quem decide mostrar a mensagem é a interface (`main.py`).

---

### Erros que cometi (importante)

#### 1. Erro repetido da Fase 1 — tentar resolver tudo direto
Tentei modelar tudo de uma vez e fiquei mentalmente travado.

Aprendizado:
quebrar problema em partes pequenas.

---

#### 2. Confusão de responsabilidade
Quase movi regras da `Conta` para `BancoService`.

Exemplo ruim:

```python
if saldo < valor:
```

dentro da service.

Melhor:

```python
conta.sacar(valor)
```

Porque a regra pertence à `Conta`.

---

#### 3. Confusão entre método e atributo
Falei que `sacar` era uma propriedade.

Correção:
`sacar` é comportamento (método).

---

#### 4. Quase retorno textual na camada errada
Pensei em:

```python
return "Conta criada com sucesso"
```

dentro da service.

Correção:
service executa regra.
interface comunica resultado.

---

#### 5. Esqueci que erro interrompe execução
Coloquei múltiplos testes destrutivos no mesmo fluxo.

Problema:
o primeiro `ValueError` parava o programa.

Correção:
testar um cenário por vez.

---

### Testes realizados

#### Happy path
- criar conta
- buscar conta
- transferir
- sacar
- depositar

---

#### Testes destrutivos
Testei:

- conta duplicada
- saldo negativo
- titular inválido
- transferência com valor negativo
- transferência com origem inexistente
- transferência com destino inexistente
- transferência com saldo insuficiente
- busca de conta inexistente

---

### O que já errei antes e reapareceu
Padrões recorrentes:

- tentar resolver tudo de uma vez
- confusão de responsabilidade entre classes
- pensar primeiro em "fazer funcionar" antes de arquitetura
- misturar regra de negócio com interface

---

### Meu nível hoje
Ainda sou iniciante.

Mas já começo a pensar em:

- camadas
- service layer
- responsabilidade única
- encapsulamento
- coordenação entre objetos

Isso é progresso claro.

---

### Próximo foco
Semana 1 — Dia 3:

Refatoração e limpeza arquitetural.

Objetivo:
deixar código mais limpo e mais profissional.

### Semana 1 - Dia 4:
Limpeza e redesign de BancoService
Reduzi dupla validação e centralizei regra
Eliminei varias validações com self.bucar_conta() indo para self.buscar_conta_erro()
Construção de um main organizado com fluxo normal digno de profissional

### Semana 1 - Dia 5:
Refatoração completa do main.py com if __name__=='__main__'
Estruturação do gitignore com arquivos que nao devem subir ao GitHub.
# Semana 1 — Dia 7: Boss Fight Task Manager

## O que construí

Iniciei o projeto Task Manager CLI aplicando a mesma arquitetura aprendida no projeto bancário:

- models/
- services/
- main.py
- docs/

Criei a model:

Task

com responsabilidade de representar a própria entidade tarefa.

Implementei:

- validação de título
- validação de descrição
- encapsulamento de status
- método de domínio:
  concluir()

Também construí:

TaskService

seguindo o padrão de service layer aprendido no BancoService.

Implementei:

- criar_tarefa()
- buscar_tarefa()
- concluir_tarefa()
- remover_tarefa()
- listar_tarefas()
- helper privado para evitar duplicação

Também construí:

main.py

com:

- fluxo_normal()
- teste_erros()
- if __name__ == "__main__"

---

## Decisões de engenharia

### 1. Escolha de dicionário em vez de lista

Escolhi:

self.__tarefas = {}

em vez de lista.

Motivo:

tarefas precisam ser buscadas frequentemente.

Com lista eu precisaria:

for tarefa in tarefas

a cada busca.

Com dicionário:

self.__tarefas.get(titulo)

tenho lookup direto e código mais limpo.

---

### 2. Título como chave

Escolhi:

titulo -> objeto Task

porque o título funciona como identificador natural nesse projeto.

Isso facilita:

- busca
- validação de duplicidade
- recuperação direta do objeto

Tradeoff:

em sistema real, títulos poderiam repetir.

Nesse projeto, a simplificação foi aceitável.

---

### 3. Método de domínio em vez de setter de status

Decisão importante:

não permitir:

task.status = "concluida"

Porque isso quebraria regra de negócio.

Escolhi:

task.concluir()

Assim a própria model protege:

- re-conclusão inválida
- estados inconsistentes

---

### 4. Encapsulamento seletivo

Encapsulei:

status

porque ele representa estado interno sensível.

Mantive:

titulo
descricao

sem encapsulamento completo nesse estágio porque não exigem regra complexa de alteração no projeto atual.

---

## Erros que cometi

### 1. Uso errado de helper privado

Erro importante:

tentei usar helper que exige entidade existente dentro de:

criar_tarefa()

Problema:

criação de entidade nova justamente ocorre quando ela ainda não existe.

Correção mental:

operações que exigem existência -> helper privado

operações de criação -> busca permissiva

---

### 2. Naming inconsistente

Cometi erro de nomes diferentes para helper.

Exemplo:

- _buscar_tarefa_erro
- _buscar_tarefa_ou_erro
- buscar_tarefa_erro

Problema:

gerou bugs e confusão.

Aprendizado:

padronização de naming evita bugs bobos.

---

### 3. Validação redundante

Inicialmente usei:

replace()

junto com:

strip()
if not valor

Problema:

dupla validação para o mesmo caso.

Correção:

fluxo mais limpo:

- validar tipo
- normalizar
- validar vazio

---

### 4. Quase setter sem regra

Poderia ter criado:

status.setter

Mas isso permitiria alterar estado livremente.

Aprendizado:

atributos com regra de negócio devem mudar por método de domínio.

---

### 5. Aprendizado sobre return e escopo

Demorei para consolidar que variáveis criadas dentro da função morrem ao fim do escopo.

Exemplo:

banco criado dentro de fluxo_normal() não existe fora automaticamente.

Correção:

usar return para compartilhar o mesmo estado:

return banco, tarefa1, tarefa2

e depois:

banco, tarefa1, tarefa2 = fluxo_normal()

Isso evita variáveis globais e mantém design mais profissional.

---

### 6. Aprendizado sobre if __name__ == "__main__"

Inicialmente não entendi corretamente o ponto de entrada do programa.

Aprendizado:

esse bloco define o ponto controlado de execução.

Estrutura correta:

- definir funções
- organizar dependências
- executar no final

Isso evita código bagunçado e melhora testabilidade.

---

## Mental models aprendidos

### Helper privado

Regra:

se a operação exige entidade existente -> helper privado

Exemplo:

- concluir
- remover
- atualizar

---

### Métodos de domínio

Regra:

estado interno sensível não deve mudar diretamente.

Exemplo:

task.concluir()

em vez de:

task.status = ...

---

### Service layer

Service coordena múltiplas entidades.

Model protege a si mesma.

---

## Testes realizados

### Happy path

- criar tarefa
- buscar tarefa
- concluir tarefa
- listar tarefas
- remover tarefa

---

### Testes destrutivos

- tarefa duplicada
- tarefa inexistente
- objeto inválido
- concluir tarefa inexistente
- remover tarefa inexistente
- tarefa já concluída

---

## Evolução percebida

Esse projeto provou que comecei a transferir conhecimento do BancoService para outro domínio.

Não foi cópia mecânica.

Precisei tomar decisões novas de arquitetura.

Isso mostra evolução real em pensamento backend.