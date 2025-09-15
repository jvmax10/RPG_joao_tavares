from .classe import Classe

class Mage(Classe):
    def __init__(self):
        super().__init__("Mago", "1d4")
        self.habilidades = ["Magias Arcanas", "Familiar"]
