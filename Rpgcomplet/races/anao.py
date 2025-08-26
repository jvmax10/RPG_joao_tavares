from .race import Race

class Anao(Race):
    def __init__(self):
        super().__init__("Anão", "6m", "18m", "Leal")
        self.habilidades = ["Resistência a Veneno", "Conhecimento em Pedras"]
