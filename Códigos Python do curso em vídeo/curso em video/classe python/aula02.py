class Conta_cliente:
    saldo = 0.0
    def __init__(self):
        print("Conta Criada")
    def depositar(self, num):
        if num>0:
            self.saldo += num
        else:
            print("\033[31mSeu deposito é muito baixo tente de novo\033[m")
    def verSaldo(self, num):
        if num <= self.saldo:
            self.saldo -= num
        else:
            print("Saldo insuficiente vc tem: ", self.saldo)
    




