from .race import Race

class Human(Race):
    def __init__(self):
        super().__init__("Humano", "9m", "Nenhuma", "Qualquer")
        self.habilidades = ["Versatilidade", "Adaptabilidade"]
