from services.ibge import Ibge


def define_localidade(ibge: Ibge, localidade=""):
    if not localidade or localidade == "BR":
        return "BR"

    resposta = ibge.busca_localidade(localidade)

    if resposta:
        return resposta["id"]
    else:
        raise ValueError(f"Localidade: {localidade} não é válida.")
