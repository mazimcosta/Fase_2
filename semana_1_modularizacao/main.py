from models.conta import Conta
from services.banco_service import BancoService

def fluxo_normal():

    conta1=Conta('Antonio',455,2000)
    conta2=Conta('Maria',788,4500)
    conta3=Conta('Carlos',712,1620)
    conta4=Conta('Marta',457,8000)
    banco=BancoService()
    banco.criar_conta(conta1)
    banco.criar_conta(conta2)
    banco.criar_conta(conta3)

    banco.depositar(conta1.numero,450)
    banco.sacar(conta2.numero,1500)
    banco.transferir(conta3.numero,conta1.numero,450)

    return banco, conta1, conta2, conta3, conta4

def teste_erros(banco,conta1,conta2,conta3,conta4):
    try:
        banco.depositar(conta1.numero,-4500)
    except ValueError as error:
        print(str(error))

    try:
        banco.sacar(conta2.numero,9999999)
    except ValueError as error:
        print(str(error))

    try:
        banco.transferir(conta3.numero,conta1.numero,-4500000)
    except ValueError as error:
        print(str(error))

    
    try:
        banco.criar_conta(conta1)
    except ValueError as error:
        print(str(error))

    try:
        banco.remover_conta(conta2.numero)

    except ValueError as error:
        print(str(error))

    
    



if __name__ == "__main__":
    banco, conta1, conta2, conta3, conta4 = fluxo_normal()
    teste_erros(banco, conta1, conta2, conta3, conta4)

