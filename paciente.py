class Paciente:
    def __init__(self, id_imagem, score):
        self.id_imagem = id_imagem
        self.score = score

    def __str__(self):
        return f"{self.id_imagem} -> {self.score:.4f}"