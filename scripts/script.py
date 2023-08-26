def definicao_titulo(is_nome: bool, is_localidade: bool, sexo="") -> str:
    titulo = "Ranking geral dos nomes"

    if is_nome:
        titulo = "Ranking dos nomes"

    if sexo == "M":
        titulo += " do sexo Masculino"

    if sexo == "F":
        titulo += " do sexo Feminino"

    if is_localidade:
        titulo += f" por localidade"

    return f"{titulo}:\n"
