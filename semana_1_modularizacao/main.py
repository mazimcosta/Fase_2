"""
ENUNCIADO — FASE 2 | SEMANA 1 | DIA 2

Objetivo:
Conectar todas as camadas criadas no Dia 1 e executar o sistema bancário
como um mini projeto funcional.

Até agora existem:

- models/conta.py
- services/banco_service.py

Hoje o objetivo é criar a camada de execução:

main.py

Responsabilidade do main.py:
- criar objetos
- conectar classes
- executar fluxos
- simular uso do sistema

IMPORTANTE:
main.py NÃO deve conter regra de negócio.
main.py apenas usa as classes já criadas.

ERRADO:
validar saldo no main
validar tipo no main
alterar saldo manualmente

CERTO:
usar os métodos das classes

Exemplo:

banco.criar_conta(...)
banco.transferir(...)

--------------------------------------------------
TAREFAS
--------------------------------------------------

1. Importar as classes necessárias

Importar:

- Conta
- BancoService

Objetivo:
treinar modularização e imports entre arquivos.

--------------------------------------------------

2. Criar instância do sistema bancário

Criar:

banco = BancoService()

Objetivo:
representar o sistema principal.

--------------------------------------------------

3. Criar contas para teste

Criar pelo menos 2 contas:

Exemplo:

- João
- Maria

Cada conta deve ter:

- titular
- numero
- saldo inicial

Objetivo:
simular entidades reais.

--------------------------------------------------

4. Cadastrar contas no banco

Usar:

banco.criar_conta(conta)

Objetivo:
testar integração entre model e service.

--------------------------------------------------

5. Executar operações bancárias

Testar:

- depósito
- saque
- transferência

Exemplo:

conta.depositar(...)
conta.sacar(...)
banco.transferir(...)

Objetivo:
verificar se regras funcionam corretamente.

--------------------------------------------------

6. Listar contas cadastradas

Usar:

banco.listar_contas()

Objetivo:
verificar armazenamento no dicionário.

--------------------------------------------------

7. Exibir resultados com print()

Aqui print() É permitido.

Mostrar:

- contas cadastradas
- saldo antes/depois
- resultado da transferência

Objetivo:
visualizar execução real.

--------------------------------------------------
REGRAS
--------------------------------------------------

- NÃO criar novas regras de negócio no main
- NÃO alterar saldo diretamente
- NÃO acessar atributos privados
- NÃO usar try/except ainda
- usar apenas os métodos já existentes

--------------------------------------------------
OBJETIVO DE APRENDIZADO
--------------------------------------------------

Hoje você deve aprender:

- fluxo entre camadas
- import entre módulos
- execução real de projeto organizado
- integração entre classes
- debugging básico de projeto modular

Resultado esperado:
um mini sistema bancário funcional executando corretamente.
"""
from models.conta import Conta
from services.banco_service import BancoService

