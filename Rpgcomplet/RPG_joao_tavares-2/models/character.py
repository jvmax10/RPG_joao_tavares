class Character:
    def __init__(self, name, race=None, char_class=None, attributes=None, modo_dados=None):
        self.name = name
        self.attributes = attributes or {
            "Força": 0,
            "Destreza": 0,
            "Constituição": 0,
            "Inteligência": 0,
            "Sabedoria": 0,
            "Carisma": 0
        }
        self.race = race
        self.char_class = char_class
        self.modo_dados = modo_dados  # guarda qual modo foi usado

    def set_attributes(self, values):
        for key, value in zip(self.attributes.keys(), values):
            self.attributes[key] = value

    def choose_race(self, race):
        self.race = race

    def choose_class(self, char_class):
        self.char_class = char_class