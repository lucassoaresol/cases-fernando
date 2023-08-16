def params(localidade="", sexo="", decada="") -> dict | None:
    payload = {}

    if localidade:
        payload["localidade"] = localidade

    if sexo:
        payload["sexo"] = sexo

    if decada:
        payload["decada"] = decada

    if payload:
        return payload
