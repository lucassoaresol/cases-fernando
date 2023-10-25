from itens.item import Item
from rankings.ranking import Ranking
from testes import constantes
import unittest


class TesteRanking(unittest.TestCase):
    def teste_titulo_sem_nomes(self):
        ranking = Ranking(constantes.ibge)
        ranking.define_titulo()

        self.assertEqual(
            ranking.titulo,
            "Ranking geral dos nomes:\n",
        )

    def teste_titulo_sem_nomes_com_localidades(self):
        ranking = Ranking(constantes.ibge, localidades=[43])
        ranking.define_titulo()

        self.assertEqual(
            ranking.titulo,
            "Ranking geral dos nomes por localidade:\n",
        )

    def teste_titulo_sem_nomes_com_localidades_e_sexo(self):
        ranking = Ranking(constantes.ibge, localidades=[43], sexo="M")
        ranking.define_titulo()

        self.assertEqual(
            ranking.titulo,
            "Ranking geral dos nomes do sexo Masculino por localidade:\n",
        )

    def teste_titulo_sem_nomes_com_localidades_e_decadas(self):
        ranking = Ranking(
            constantes.ibge,
            localidades=[43],
            decadas=[1930],
        )
        ranking.define_titulo()

        self.assertEqual(
            ranking.titulo,
            "Ranking geral dos nomes por localidade e década:\n",
        )

    def teste_titulo_sem_nomes_com_localidades_sexo_e_decadas(self):
        ranking = Ranking(
            constantes.ibge,
            localidades=[43],
            sexo="M",
            decadas=[1930],
        )
        ranking.define_titulo()

        self.assertEqual(
            ranking.titulo,
            "Ranking geral dos nomes do sexo Masculino por localidade e década:\n",
        )

    def teste_titulo_sem_nomes_com_sexo(self):
        ranking = Ranking(constantes.ibge, sexo="M")
        ranking.define_titulo()

        self.assertEqual(
            ranking.titulo,
            "Ranking geral dos nomes do sexo Masculino:\n",
        )

    def teste_titulo_sem_nomes_com_sexo_e_decadas(self):
        ranking = Ranking(constantes.ibge, sexo="M", decadas=[1930])
        ranking.define_titulo()

        self.assertEqual(
            ranking.titulo,
            "Ranking geral dos nomes do sexo Masculino por década:\n",
        )

    def teste_titulo_sem_nomes_com_decadas(self):
        ranking = Ranking(constantes.ibge, decadas=[1930])
        ranking.define_titulo()

        self.assertEqual(
            ranking.titulo,
            "Ranking geral dos nomes por década:\n",
        )

    def teste_titulo_com_nomes(self):
        ranking = Ranking(constantes.ibge, ["FERNANDO"])
        ranking.define_titulo()

        self.assertEqual(
            ranking.titulo,
            "Ranking dos nomes:\n",
        )

    def teste_titulo_com_nomes_e_localidades(self):
        ranking = Ranking(constantes.ibge, ["FERNANDO"], localidades=[43])
        ranking.define_titulo()

        self.assertEqual(
            ranking.titulo,
            "Ranking dos nomes por localidade:\n",
        )

    def teste_titulo_com_nomes_localidades_e_sexo(self):
        ranking = Ranking(constantes.ibge, ["FERNANDO"], "M", [43])
        ranking.define_titulo()

        self.assertEqual(
            ranking.titulo,
            "Ranking dos nomes do sexo Masculino por localidade:\n",
        )

    def teste_titulo_com_nomes_localidades_sexo_e_decadas(self):
        ranking = Ranking(
            constantes.ibge,
            ["FERNANDO"],
            "M",
            [43],
            [1930],
        )
        ranking.define_titulo()

        self.assertEqual(
            ranking.titulo,
            "Ranking dos nomes do sexo Masculino por localidade e década:\n",
        )

    def teste_titulo_com_nomes_e_sexo(self):
        ranking = Ranking(constantes.ibge, ["FERNANDO"], "M")
        ranking.define_titulo()

        self.assertEqual(
            ranking.titulo,
            "Ranking dos nomes do sexo Masculino:\n",
        )

    def teste_titulo_com_nomes_sexo_e_decadas(self):
        ranking = Ranking(
            constantes.ibge,
            ["FERNANDO"],
            "M",
            decadas=[1930],
        )
        ranking.define_titulo()

        self.assertEqual(
            ranking.titulo,
            "Ranking dos nomes do sexo Masculino por década:\n",
        )

    def teste_titulo_com_nomes_e_decadas(self):
        ranking = Ranking(constantes.ibge, ["FERNANDO"], decadas=[1930])
        ranking.define_titulo()

        self.assertEqual(
            ranking.titulo,
            "Ranking dos nomes por década:\n",
        )

    def teste_instancia_item(self):
        ranking = Ranking(constantes.ibge)

        self.assertIsInstance(ranking.instancia_item("FERNANDO", 61551), Item)

    def teste_orderna_ranking(self):
        ranking = Ranking(constantes.ibge)

        self.assertListEqual(
            ranking.orderna_ranking([constantes.fernandoItem, constantes.mariaItem]),
            [constantes.mariaItem, constantes.fernandoItem],
        )

    def teste_busca_ranking(self):
        ranking = Ranking(constantes.ibge, ["FERNDANDO"])

        self.assertEqual(len(ranking.busca_ranking()), 1)

    def teste_busca_ranking_sem_nomes(self):
        ranking = Ranking(constantes.ibge_ranking_geral)

        itens = []

        ranking.adiciona_item(itens, constantes.ranking_geral)

        self.assertEqual(len(ranking.busca_ranking()), len(itens))

    def teste_busca_ranking_com_decada_invalida(self):
        ranking = Ranking(constantes.ibge)
        with self.assertRaises(ValueError):
            ranking.busca_ranking(decada=1900)

    def teste_busca_ranking_com_decada_invalida_texto(self):
        ranking = Ranking(constantes.ibge)
        with self.assertRaises(ValueError):
            ranking.busca_ranking(decada="rsrs")

    def teste_define_ranking(self):
        ranking = Ranking(constantes.ibge)
        ranking.define_ranking([constantes.fernandoItem])

        self.assertEqual(
            ranking.ranking,
            "1º - FERNANDO - 556346\n",
        )

    def teste_gera_ranking(self):
        ranking = Ranking(constantes.ibge, ["FERNANDO"])
        ranking.gera_ranking()

        self.assertEqual(
            ranking.ranking,
            "1º - FERNANDO - 556346\n",
        )

    def teste_gera_ranking_json(self):
        ranking = Ranking(constantes.ibge, ["FERNANDO"])
        ranking.gera_ranking()

        self.assertListEqual(
            ranking.ranking_json,
            [
                {
                    "localidade": "BR",
                    "sexo": ranking.sexo,
                    "res": ranking.define_ranking([constantes.fernandoItem]),
                }
            ],
        )

    def teste_gera_ranking_com_localidades(self):
        ranking = Ranking(constantes.ibge, ["FERNANDO"], localidades=[43])
        ranking.gera_ranking()

        self.assertEqual(
            ranking.ranking,
            "\nLocalidade: 43\n1º - FERNANDO - 556346\n",
        )

    def teste_gera_ranking_com_localidades_e_decadas(self):
        ranking = Ranking(
            constantes.ibge, ["FERNANDO"], localidades=[43], decadas=[2010]
        )
        ranking.gera_ranking()

        self.assertEqual(
            ranking.ranking,
            "\nDécada: 2010\n\nLocalidade: 43\n1º - FERNANDO - 61551\n",
        )

    def teste_gera_ranking_com_sexo_invalido(self):
        with self.assertRaises(ValueError):
            Ranking(constantes.ibge, sexo="bk")

    def teste_gera_ranking_com_decada_invalida(self):
        ranking = Ranking(constantes.ibge, decadas=[1900])
        with self.assertRaises(ValueError):
            ranking.gera_ranking()

    def teste_gera_ranking_com_decada_invalida_texto(self):
        ranking = Ranking(constantes.ibge, decadas=["rsrs"])
        with self.assertRaises(ValueError):
            ranking.gera_ranking()

    def teste_mostra_ranking(self):
        ranking = Ranking(constantes.ibge, ["FERNANDO"])
        ranking.define_titulo()
        ranking.gera_ranking()

        self.assertEqual(
            ranking.mostra_ranking(),
            print(ranking.titulo + ranking.ranking),
        )


if __name__ == "__main__":
    unittest.main()
