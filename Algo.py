from Classe import *
import os

def main():
    try:
        sair = False
        banco = Banco("Senai")
        countID = 0
        while sair == False:
            os.system("cls")
            print("---MENU---")
            print("[1] - Criar Conta")
            print("[2] - Sacar")
            print("[3] - Depositar")
            print("[4] - Transferir")
            print("[5] - Saldo")
            print("[6] - Clientes")
            print("[7] - Sair")
            print("")
            menu = int(input(">> "))
            os.system("pause")

            match menu:
                case 1:
                    os.system("cls")
                    print("Insira as Informações")

                    nome = input("Digite seu Nome: ")
                    saldo_inicial = float(input("Digite seu Saldo Inicial: "))

                    banco.criar_conta(nome, saldo_inicial)
                    os.system("pause")

                case 2:
                    os.system("cls")
                    print("Insira as Informações")

                    countID += 1
                    id = countID
                    conta = input("Informe sua Conta: ")
                    valor = float(input("Digite o valor a ser Retirado: "))

                    banco.sacar(id, conta, valor)
                    os.system("pause")

                case 3:
                    os.system("cls")
                    print("Insira as Informações")

                    conta2 = input("DInforme sua Conta: ")
                    valor2 = float(input("Digite o valor a ser Depositado: "))

                    banco.depositar(conta2, valor2)
                    os.system("pause")

                case 4:
                    os.system("cls")
                    print("Insira as Informações")

                    origem = input("Informe sua Conta: ")
                    destino = input("Digite o nome da conta que receberá a transferencia: ")
                    valor3 = float(input("Digite o valor da Transferencia: "))

                    banco.transferir(origem, destino, valor3)
                    os.system("pause")

                case 5:
                    os.system("cls")
                    print("Insira as Informações")

                    conta3 = input("Informe sua Conta")

                    banco.saldo(conta3)
                    os.system("pause")

                case 6:
                    banco.getClientes()

                case 7:
                    os.system("cls")
                    sair = True
                    print("Saindo...")
                    os.system("pause")

                case _:
                    os.system("cls")
                    print("Opção Inválida")
                    os.system("pause")

    except Exception as erro:
        os.system("cls")
        print("Digite corretamente a Informação")
        print(erro.__class__.__name__)
        os.system("pause")