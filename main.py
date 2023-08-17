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
    decadas = args.decadas
    is_localidade = not localidades == None
    is_decada = not decadas == None
    api = Api(retry, timeout)
    ranking = Ranking(api, is_localidade, is_decada, sexo)

    if not nomes:
        try:
            return print(ranking.geral(localidades, decadas))
        except MaxRetryError:
            return print("Número de tentativas excedido")

    try:
        nomes_frequencia = Item(api, nomes, sexo).frequencia(localidades, decadas)
        return print(ranking.nomes(nomes_frequencia))
    except MaxRetryError:
        return print("Número de tentativas excedido")


if __name__ == "__main__":
    main()
