from models.conta import Conta
from services.banco_service import BancoService

if __name__=='__main__':
            



        conta1=Conta('Antonio',455,2000)
        conta2=Conta('Maria',788,4500)
        conta3=Conta('Carlos',712,1620)
        conta4=Conta('Marta',457,8000)
        banco=BancoService()



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

        def teste_erros():
            try:
                banco.depositar(conta1.numero,-4500)
            except Exception as error:
                print(str(error))

            try:
                banco.sacar(conta2.numero,9999999)
            except Exception as error:
                print(str(error))

            try:
                banco.transferir(conta3.numero,conta1.numero,-4500000)
            except Exception as error:
                print(str(error))

            
            try:
                banco.criar_conta(conta5)
            except Exception as error:
                print(str(error))

            try:
                banco.remover_conta(conta6.numero)

            except Exception as error:
                print(str(error))