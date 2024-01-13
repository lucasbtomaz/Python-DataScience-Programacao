class Conta:
    def __init__(self, titular, numero, saldo):
        self.titular = titular
        self.numero = numero
        self.saldo = 0

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        if (saldo < 0):
            print('Saldo deve ser positivo')
        else:
            self._saldo = saldo