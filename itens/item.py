class Item:
    def __init__(self, nome: str, frequencia: int) -> None:
        self.nome = nome.upper()
        self.frequencia = frequencia

    def __str__(self) -> str:
        return f"{self.nome} - {self.frequencia}"
