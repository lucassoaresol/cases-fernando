def definicao_title(title: str, localidade="", sexo="") -> str:
    if sexo == "M":
        title += " do sexo Masculino"

    if sexo == "F":
        title += " do sexo Feminino"

    if localidade:
        title += f" por localidade"

    return f"{title}:\n"
