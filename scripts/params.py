def params(localidade="", sexo="") -> dict | None:
    payload = {}

    if localidade:
        payload["localidade"] = localidade

    if sexo:
        payload["sexo"] = sexo

    if payload:
        return payload
