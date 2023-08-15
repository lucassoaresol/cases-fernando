def definicao_title(
    title: str,
    is_localidade: bool,
    sexo="",
) -> str:
    if sexo == "M":
        title += " do sexo Masculino"

    if sexo == "F":
        title += " do sexo Feminino"

    if is_localidade:
        title += f" por localidade"

    return f"{title}:\n"
