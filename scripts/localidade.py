from services.ibge import Ibge


def define_localidade(ibge: Ibge, localidade="") -> str:
    if not localidade or localidade == "BR":
        return "BR"

    resposta = ibge.busca_localidade(localidade)

    if resposta:
        return resposta["id"]
    else:
        print(f"Localidade: {localidade} não encontrada.")
