class Race:
    def __init__(self, nome, movimento, infravisao, alinhamento):
        self.nome = nome
        self.movimento = movimento
        self.infravisao = infravisao
        self.alinhamento = alinhamento
        self.habilidades = []

    def __str__(self):
        return f"Raça: {self.nome} | Movimento: {self.movimento} | Infravisão: {self.infravisao} | Alinhamento: {self.alinhamento} | Habilidades: {', '.join(self.habilidades)}"
