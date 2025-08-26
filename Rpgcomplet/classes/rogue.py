from .classe import Classe

class Rogue(Classe):
    def __init__(self):
        super().__init__("Ladino", "1d6")
        self.habilidades = ["Ataque Furtivo", "Evasão"]
