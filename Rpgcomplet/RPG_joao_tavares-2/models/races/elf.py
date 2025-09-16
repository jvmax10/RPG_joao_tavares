from .race import Race

class Elf(Race):
    def __init__(self):
        super().__init__("Elfo", "9m", "18m", "Caótico")
        self.habilidades = ["Visão na Penumbra", "Afinidade com Magia"]
