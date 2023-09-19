class Banco:
    def __init__(self, nomeBanco):
        self.nomeBanco = nomeBanco

    def criar_conta(self, nome, saldo_inicial):
        self.nome = nome
        self.saldo_inicial = saldo_inicial

    def sacar(self, conta, valor):
        self.conta = conta
        self.valor = valor

        if self.valor <= self.saldo_inicial:
            self.saldo_inicial - self.valor
            print("Saque feito")
            print(f"Valor do Saque: {self.valor}")
            print(f"Saldo restante: {self.saldo_inicial}")

        else:
            print("Saldo Insuficiente")

    def depositar(self, conta, valor):
        self.conta = conta
        self.valor = valor

        self.saldo_inicial + self.valor
        print("Depósito realizado")
        print(f"Saldo atual: {self.saldo_inicial}")

    def transferir(self, origem, destino, valor):
        self.origem = origem
        self.destino = destino
        self.valor = valor

        if self.saldo_inicial >= self.valor:
            self.saldo_inicial - self.valor
            self.origem + self.valor

            print("Tranferencia realizada")

        else:
            print("Saldo Insuficiente")

    def saldo(self, conta):
        self.conta = conta