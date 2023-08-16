def definicao_title(title: str, is_localidade: bool, is_decada: bool, sexo="") -> str:
    if sexo == "M":
        title += " do sexo Masculino"

    if sexo == "F":
        title += " do sexo Feminino"

    if is_localidade:
        title += " por localidade"

    if is_decada:
        if is_localidade:
            title += " e década"
        else:
            title += " por década"

    return f"{title}:\n"
