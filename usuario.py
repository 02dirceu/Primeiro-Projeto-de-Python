

class Usuario:
    def __init__(self, usuario, espaco):
        self.usuario = usuario.title()
        self.espaco = float(espaco) / 1024 ** 2

