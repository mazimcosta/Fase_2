"""
ENUNCIADO — FASE 2 | SEMANA 1 | DIA 1

Objetivo:
Refatorar o projeto de conta bancária da fase 1 aplicando modularização
e separação de responsabilidades.

Neste arquivo (conta.py), implemente a entidade Conta.

A classe Conta deve representar apenas os dados e comportamentos
diretamente relacionados a uma conta bancária.

MVP (versão simples):
A conta terá inicialmente:

- titular
- numero
- saldo

Implementar os métodos:

1. depositar(valor)
   Regras:
   - valor deve ser maior que zero
   - se valor for inválido, lançar:
     raise ValueError("Valor de depósito inválido")
   - se válido, somar ao saldo

2. sacar(valor)
   Regras:
   - valor deve ser maior que zero
   - se valor for inválido, lançar:
     raise ValueError("Valor de saque inválido")
   - não permitir saque maior que o saldo
   - se saldo insuficiente:
     raise ValueError("Saldo insuficiente")
   - se válido, subtrair do saldo

Regras de arquitetura:
- NÃO usar input()
- NÃO usar print()
- NÃO usar try/except
- NÃO controlar múltiplas contas aqui
- NÃO criar menu aqui
- NÃO criar lógica de banco_service aqui

Responsabilidade deste arquivo:
Representar UMA conta bancária e suas regras internas.
"""

class  Conta:
    
    def __init__(self,titular,numero,saldo):
        
        if not isinstance(titular,str):
            raise ValueError('Titular invalido')
        
        titular=titular.strip()
        if not titular.replace(' ','').isalpha():
            raise ValueError('Titular invalido')
        
        if not isinstance(numero,int):
            raise ValueError('Numero invalido')
        
        
        if numero<=0:
            raise ValueError('Numero invalido')
        
        if not isinstance(saldo,int):
            raise ValueError('Saldo invalido')
        
        
        if  saldo<0:
            raise ValueError('Saldo invalido')
        
        self.titular=titular
        self.numero=numero
        self.__saldo=saldo

    @property
    def saldo(self):
        return self.__saldo
  


    def sacar(self,valor):
      if not isinstance(valor,int):
          raise ValueError('Valor invalido')
      
      if valor<=0:
          raise ValueError('Valor invaido')
      
      if valor>self.__saldo:
          raise ValueError('Saldo insuficiente')
      
      self.__saldo-=valor
      return f'Saque efetuado com sucesso'
    

    def depositar(self,valor):
        if not isinstance(valor, int):
            raise ValueError('Valor invalido')
        
        if valor<=0:
            raise ValueError('Valor invalido')
        
        self.__saldo+=valor
        return f'Deposito efetuado com sucesso'
      