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