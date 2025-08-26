class Classe:
    def __init__(self, nome, dado_vida):
        self.nome = nome
        self.dado_vida = dado_vida
        self.habilidades = []

    def __str__(self):
        return f"Classe: {self.nome} | Dado de Vida: {self.dado_vida} | Habilidades: {', '.join(self.habilidades)}"
