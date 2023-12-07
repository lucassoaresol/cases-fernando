from rankings.ranking import Ranking
from scripts.arguments import arguments
from services.cache import Cache
from services.ibge import Ibge
import time


def main():
    inicio = time.perf_counter()
    args = arguments().parse_args()
    nomes = args.nomes
    localidades = args.localidades
    sexo = args.sexo
    retry = args.retry
    timeout = args.timeout
    decadas = args.decadas
    arquivo = args.arquivo
    cache = Cache()

    ranking = Ranking(
        Ibge(retry, timeout, cache, cache.verificar_conexao()),
        nomes,
        sexo,
        localidades,
        decadas,
        arquivo,
    )

    ranking.gera_ranking()
    ranking.mostra_ranking()
    ranking.exporta_json_ranking()

    fim = time.perf_counter()
    total = round(fim - inicio, 2)
    print(f"Tempo de execução: {total}")


if __name__ == "__main__":
    main()
