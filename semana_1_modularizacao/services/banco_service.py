"""
ENUNCIADO — FASE 2 | SEMANA 1 | DIA 1

Objetivo:
Implementar a camada de serviço (BancoService) aplicando separação
de responsabilidades.

Este arquivo NÃO representa uma conta bancária.
Ele representa o sistema bancário que coordena múltiplas contas.

Responsabilidades do BancoService:
- armazenar contas
- cadastrar novas contas
- buscar contas existentes
- transferir dinheiro entre contas
- listar contas cadastradas

Estrutura interna:
As contas devem ser armazenadas em um dicionário.

Formato:

{
    numero_conta: objeto_conta
}

Exemplo:

{
    1001: conta_joao,
    1002: conta_maria
}

Implementar os métodos:

1. criar_conta(conta)
   Regras:
   - receber apenas objetos do tipo Conta
   - se receber objeto inválido:
     raise ValueError("Conta invalida")
   - não permitir número de conta duplicado
   - se conta já existir:
     raise ValueError("Conta ja cadastrada")
   - se válido:
     armazenar no dicionário

2. buscar_conta(numero)
   Regras:
   - receber número da conta
   - validar tipo
   - se conta não existir:
     retornar None
   - se existir:
     retornar objeto Conta

3. transferir(numero_origem, numero_destino, valor)
   Regras:
   - localizar conta de origem
   - localizar conta de destino
   - se alguma não existir:
     raise ValueError("Conta nao encontrada")
   - usar:
     conta_origem.sacar(valor)
     conta_destino.depositar(valor)

IMPORTANTE:
BancoService coordena.
BancoService NÃO altera saldo diretamente.

ERRADO:

conta.saldo += valor

CERTO:

conta.depositar(valor)

4. listar_contas()
   Regras:
   - retornar lista com todas as contas cadastradas

Regras de arquitetura:
- NÃO usar input()
- NÃO usar print()
- NÃO usar try/except
- NÃO duplicar regras que já pertencem à Conta
- NÃO alterar __saldo diretamente

Responsabilidade deste arquivo:
Coordenar múltiplas contas do sistema.
"""
from models.conta import Conta



class  BancoService:
    

    def __init__(self):
        self.__contas={}


    
    
    def buscar_conta(self,numero):
        if not isinstance(numero,int):
            raise ValueError('Numero invalido')
        
        if numero<=0:
            raise ValueError('Numero invalido')
        
        if self.__contas.get(numero):
            return self.__contas[numero]
        
        return None
    
    @property
    def contas(self):
        return self.__contas.copy()
    
    
    
    def  criar_conta(self,conta):
        if not isinstance(conta,Conta):
            raise ValueError('Conta invalida')
        
        conta_existe=self.buscar_conta(conta.numero)
        if conta_existe is not None:
            raise ValueError('Conta ja cadastrada')
        
        self.__contas[conta.numero]=conta
        return 'Conta cadastrada com sucesso'
    
    
    
    
    
    
    
    def  transferir(self,numero_origem,numero_destino,valor):
            
        
        if not isinstance(valor,(int,float)):
            raise ValueError('Valor invalido')
        
        
        conta_origem=self.buscar_conta(numero_origem)
        if conta_origem is None:
            raise ValueError('Conta não encontrada')
        
        conta_destino=self.buscar_conta(numero_destino)
        if conta_destino is None:
            raise ValueError('Conta nao encontrada')
        
        conta_origem.sacar(valor)
        conta_destino.depositar(valor)
        return 'Transferencia efetuada com sucesso'
    

    def listar_contas(self):
        lista=[]
        for chave,valor in self.__contas.items():
            lista.append({chave:valor})

        return lista