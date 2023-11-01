from rankings.ranking import Ranking
from scripts.arguments import arguments
from services.ibge import Ibge


def main():
    args = arguments().parse_args()
    nomes = args.nomes
    localidades = args.localidades
    sexo = args.sexo
    retry = args.retry
    timeout = args.timeout
    decadas = args.decadas

    ranking = Ranking(Ibge(retry, timeout), nomes, sexo, localidades, decadas)

    ranking.gera_ranking()
    ranking.mostra_ranking()
    ranking.exporta_json_ranking()


if __name__ == "__main__":
    main()
