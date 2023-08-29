from itens import Item
from rankings import Ranking
from scripts import arguments, definicao_titulo
from .ibge import Ibge


class Dados:
    args = arguments().parse_args()
    nomes = args.nomes
    localidades = args.localidades
    sexo = args.sexo
    is_nome = not nomes == None
    is_localidade = not localidades == None
    ibge = Ibge(sexo)
    ranking = Ranking()
    titulo = definicao_titulo(is_nome, is_localidade, sexo)

    @classmethod
    def busca(cls, localidade="") -> list | None:
        if cls.nomes:
            itens = []

            for nome in cls.nomes:
                item = Item(nome, cls.ibge.busca_frequencia(nome, localidade))
                itens.append(item)

            return cls.ranking.orderna_nomes(itens)

        return cls.ibge.busca_ranking_geral(localidade)

    @classmethod
    def define(cls) -> str:
        conteudo = cls.titulo

        if cls.localidades:
            for localidade in cls.localidades:
                conteudo += f"\nLocalidade: {localidade}\n"
                conteudo += f"{cls.ranking.gera_ranking(cls.busca(localidade))}\n"
            return conteudo

        conteudo += cls.ranking.gera_ranking(cls.busca())

        return conteudo
