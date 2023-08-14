from itens import Item
from rankings import Ranking
from scripts import arguments
from services import Api
from urllib3.exceptions import MaxRetryError


def main():
    args = arguments().parse_args()
    nomes = args.nomes
    localidades = args.localidades
    sexo = args.sexo
    retry = args.retry
    timeout = args.timeout
    api = Api(retry, timeout)

    if not nomes:
        try:
            return print(Ranking(api).geral(localidades, sexo))
        except MaxRetryError:
            return print("Número de tentativas excedido")

    if localidades:
        try:
            return print(
                Ranking(
                    api,
                    nomes_frequencia_localidade=Item(
                        api, nomes, sexo
                    ).frequencia_localidades(localidades),
                ).nomes(sexo)
            )
        except MaxRetryError:
            return print("Número de tentativas excedido")

    try:
        return print(Ranking(api, Item(api, nomes, sexo).frequencia_nome()).nomes(sexo))
    except MaxRetryError:
        return print("Número de tentativas excedido")


if __name__ == "__main__":
    main()
