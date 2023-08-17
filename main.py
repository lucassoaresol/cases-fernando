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
    is_localidade = not localidades == None
    api = Api(retry, timeout)
    ranking = Ranking(api, is_localidade, sexo)

    if not nomes:
        try:
            return print(ranking.geral(localidades))
        except MaxRetryError:
            return print("Número de tentativas excedido")

    try:
        nomes_frequencia = Item(api, nomes, sexo).frequencia(localidades)
        return print(ranking.nomes(nomes_frequencia))
    except MaxRetryError:
        return print("Número de tentativas excedido")


if __name__ == "__main__":
    main()
