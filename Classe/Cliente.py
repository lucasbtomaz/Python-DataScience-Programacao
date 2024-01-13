class Cliente:
    def __init__(self, nome, documento):

        self._nome = nome
        self._documento = documento

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome


