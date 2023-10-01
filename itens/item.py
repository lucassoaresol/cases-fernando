from services.ibge import Ibge


class Item:
    def __init__(
        self, ibge: Ibge, nome: str, frequencia: int, sexo="", localidade="", decada=""
    ) -> None:
        self.nome = nome.upper()
        self.frequencia = (
            frequencia
            if frequencia != 0
            else ibge.busca_frequencia(nome, sexo, localidade, decada)
        )

    def __str__(self) -> str:
        return f"{self.nome} - {self.frequencia}"
