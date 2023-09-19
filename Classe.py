class Banco:
    def __init__(self, nomeBanco):
        self.nomeBanco = nomeBanco
        self.lista_clientes = []

    def criar_conta(self, id, nome, saldo_inicial):
        self.id = id
        self.nome = nome
        self.saldo_inicial = saldo_inicial
        self.lista_clientes [self.id] = [self.nome, self.saldo_inicial]

    def getClientes(self):
        for chave, valor in self.lista_clientes.items():
            print(f"ID: {chave} - Nome: {valor[0]} - Saldo: {valor[1]}")

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
            self.destino + self.valor

            print("Tranferencia realizada")

        else:
            print("Saldo Insuficiente")

    def saldo(self, conta):
        self.conta = conta