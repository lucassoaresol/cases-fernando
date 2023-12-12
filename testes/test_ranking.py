from itens.item import Item
from rankings.ranking import Ranking, processar_combinacao
from services.ibge import Ibge
from testes import constantes
from unittest.mock import patch, Mock
import json
import os
import unittest


class TesteRanking(unittest.TestCase):
    def setUp(self):
        ibge = Mock(Ibge)
        ibge.busca_localidade.return_value = constantes.siglas_estados
        ibge.busca_ranking.return_value = constantes.nome_sem_parametros
        self.ibge = ibge

    def teste_processar_combinacao(self):
        itens = processar_combinacao((self.ibge, "fernando", None, None, 2010))

        self.assertEqual(len(itens), 1)

    def teste_processar_combinacao_geral(self):
        ibge = Mock(Ibge)
        ibge.busca_ranking.return_value = constantes.ranking_geral
        itens = processar_combinacao((ibge, None, None, None, None))

        self.assertEqual(len(itens), 20)

    def teste_titulo_sem_nomes(self):
        ranking = Ranking(self.ibge)
        ranking.define_titulo()

        self.assertEqual(
            ranking.titulo,
            "Ranking geral dos nomes:\n",
        )

    def teste_titulo_sem_nomes_com_localidades(self):
        ranking = Ranking(self.ibge, localidades=[43])
        ranking.define_titulo()

        self.assertEqual(
            ranking.titulo,
            "Ranking geral dos nomes por localidade:\n",
        )

    def teste_titulo_sem_nomes_com_localidades_e_sexo(self):
        ranking = Ranking(self.ibge, localidades=[43], sexo="M")
        ranking.define_titulo()

        self.assertEqual(
            ranking.titulo,
            "Ranking geral dos nomes do sexo Masculino por localidade:\n",
        )

    def teste_titulo_sem_nomes_com_localidades_e_decadas(self):
        ranking = Ranking(
            self.ibge,
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
            self.ibge,
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
        ranking = Ranking(self.ibge, sexo="M")
        ranking.define_titulo()

        self.assertEqual(
            ranking.titulo,
            "Ranking geral dos nomes do sexo Masculino:\n",
        )

    def teste_titulo_sem_nomes_com_sexo_e_decadas(self):
        ranking = Ranking(self.ibge, sexo="F", decadas=[1930])
        ranking.define_titulo()

        self.assertEqual(
            ranking.titulo,
            "Ranking geral dos nomes do sexo Feminino por década:\n",
        )

    def teste_titulo_sem_nomes_com_decadas(self):
        ranking = Ranking(self.ibge, decadas=[1930])
        ranking.define_titulo()

        self.assertEqual(
            ranking.titulo,
            "Ranking geral dos nomes por década:\n",
        )

    def teste_titulo_com_nomes(self):
        ranking = Ranking(self.ibge, ["FERNANDO"])
        ranking.define_titulo()

        self.assertEqual(
            ranking.titulo,
            "Ranking dos nomes:\n",
        )

    def teste_titulo_com_nomes_e_localidades(self):
        ranking = Ranking(self.ibge, ["FERNANDO"], localidades=[43])
        ranking.define_titulo()

        self.assertEqual(
            ranking.titulo,
            "Ranking dos nomes por localidade:\n",
        )

    def teste_titulo_com_nomes_localidades_e_sexo(self):
        ranking = Ranking(self.ibge, ["FERNANDO"], "M", [43])
        ranking.define_titulo()

        self.assertEqual(
            ranking.titulo,
            "Ranking dos nomes do sexo Masculino por localidade:\n",
        )

    def teste_titulo_com_nomes_localidades_sexo_e_decadas(self):
        ranking = Ranking(
            self.ibge,
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
        ranking = Ranking(self.ibge, ["FERNANDO"], "M")
        ranking.define_titulo()

        self.assertEqual(
            ranking.titulo,
            "Ranking dos nomes do sexo Masculino:\n",
        )

    def teste_titulo_com_nomes_sexo_e_decadas(self):
        ranking = Ranking(
            self.ibge,
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
        ranking = Ranking(self.ibge, ["FERNANDO"], decadas=[1930])
        ranking.define_titulo()

        self.assertEqual(
            ranking.titulo,
            "Ranking dos nomes por década:\n",
        )

    def teste_adiciona_item(self):
        ranking = Ranking(self.ibge)
        item = Item(self.ibge, "fernando", 556346)
        ranking.adiciona_item(item)

        self.assertEqual(len(ranking.itens), 1)

    def teste_instacia_item(self):
        ranking = Ranking(self.ibge)
        ranking.instancia_item("fernando", 556346)

        self.assertEqual(len(ranking.itens), 1)

    def teste_orderna_ranking(self):
        ranking = Ranking(self.ibge)
        item1 = Item(self.ibge, "fernando", 556346)
        item2 = Item(self.ibge, "maria", 1111301)

        self.assertListEqual(
            ranking.orderna_ranking([item1, item2]),
            [item2, item1],
        )

    def teste_busca_ranking(self):
        ibge = Mock(Ibge)
        ibge.busca_ranking.return_value = constantes.ranking_geral
        ranking = Ranking(ibge)
        ranking.busca_ranking()

        self.assertEqual(len(ranking.itens), 20)

    def teste_gera_combinacoes_arquivo(self):
        itens_json = ["FERNANDO", "MARIA", "LUCAS", "CARLOS"]

        with open("nomes.json", "w") as json_file:
            json.dump(itens_json, json_file)

        ranking = Ranking(self.ibge, arquivo="nomes")
        combinacoes = ranking.gera_combinacoes()

        self.assertEqual(len(combinacoes), 4)
        self.assertListEqual(itens_json, ranking.nomes)

        os.remove("nomes.json")

    def teste_gera_combinacoes_nomes_e_localidades(self):
        ranking = Ranking(
            self.ibge, nomes=["FERNANDO", "MARIA", "LUCAS", "CARLOS"], localidades=[43]
        )
        combinacoes = ranking.gera_combinacoes()

        self.assertEqual(len(combinacoes), 4)

    def teste_gera_combinacoes_nomes_localidades_e_decadas(self):
        ranking = Ranking(
            self.ibge,
            nomes=["FERNANDO", "MARIA", "LUCAS", "CARLOS"],
            localidades=[43],
            decadas=[2000],
        )
        combinacoes = ranking.gera_combinacoes()

        self.assertEqual(len(combinacoes), 4)

    def teste_gera_combinacoes_nomes_e_decadas(self):
        ranking = Ranking(
            self.ibge, nomes=["FERNANDO", "MARIA", "LUCAS", "CARLOS"], decadas=[2000]
        )
        combinacoes = ranking.gera_combinacoes()

        self.assertEqual(len(combinacoes), 4)

    def teste_gera_combinacoes_localidades(self):
        ranking = Ranking(self.ibge, localidades=[43])
        combinacoes = ranking.gera_combinacoes()

        self.assertEqual(len(combinacoes), 1)

    def teste_gera_combinacoes_localidades_e_decadas(self):
        ranking = Ranking(self.ibge, localidades=[43], decadas=[2000])
        combinacoes = ranking.gera_combinacoes()

        self.assertEqual(len(combinacoes), 1)

    def teste_gera_combinacoes_decadas(self):
        ranking = Ranking(self.ibge, decadas=[2000])
        combinacoes = ranking.gera_combinacoes()

        self.assertEqual(len(combinacoes), 1)

    def teste_gera_ranking(self):
        ibge = Mock(Ibge)
        ibge.busca_ranking.return_value = constantes.ranking_geral
        ranking = Ranking(ibge)
        ranking.gera_ranking()

        self.assertEqual(len(ranking.itens), 20)

    def teste_monta_ranking(self):
        ranking = Ranking(self.ibge, ["FERNANDO"])
        item = Item(self.ibge, "fernando")
        ranking.adiciona_item(item)
        ranking.monta_ranking(ranking.itens)

        self.assertEqual(
            ranking.monta_ranking(ranking.itens),
            "1º - FERNANDO - 556346\n",
        )

    def teste_monta_ranking_com_localidades(self):
        ranking = Ranking(self.ibge, ["FERNANDO"], localidades=[43])
        item = Item(self.ibge, "fernando", 556346, localidade=43)
        ranking.adiciona_item(item)
        ranking.monta_ranking(ranking.itens)

        self.assertEqual(
            ranking.monta_ranking(ranking.itens),
            "\nLocalidade: 43\n1º - FERNANDO - 556346\n",
        )

    def teste_monta_ranking_com_localidades_e_decadas(self):
        ranking = Ranking(self.ibge, ["FERNANDO"], localidades=[43], decadas=[2010])
        item = Item(self.ibge, "fernando", 556346, localidade=43, decada=2010)
        ranking.adiciona_item(item)
        ranking.monta_ranking(ranking.itens)

        self.assertEqual(
            ranking.monta_ranking(ranking.itens),
            "\nDécada: 2010\n\nLocalidade: 43\n1º - FERNANDO - 556346\n",
        )

    def teste_monta_ranking_com_decadas(self):
        ranking = Ranking(self.ibge, ["FERNANDO"], decadas=[2010])
        item = Item(self.ibge, "fernando", decada=2010)
        ranking.adiciona_item(item)
        ranking.monta_ranking(ranking.itens)

        self.assertEqual(
            ranking.monta_ranking(ranking.itens),
            "\nDécada: 2010\n1º - FERNANDO - 61551\n",
        )

    def teste_define_ranking(self):
        ranking = Ranking(self.ibge)
        item = Item(self.ibge, "fernando", 556346)

        self.assertEqual(
            ranking.define_ranking([item]),
            "1º - FERNANDO - 556346\n",
        )

    def teste_define_ranking_none(self):
        ranking = Ranking(self.ibge)

        self.assertEqual(
            ranking.define_ranking([]),
            "Nenhum ranking disponível",
        )

    def teste_mostra_ranking(self):
        ranking = Ranking(self.ibge, ["FERNANDO"])
        item = Item(self.ibge, "fernando", 556346)
        ranking.adiciona_item(item)
        ranking.mostra_ranking()

        self.assertEqual(
            ranking.mostra_ranking(),
            print(ranking.titulo + ranking.monta_ranking(ranking.itens)),
        )

    def teste_exporta_json_ranking(self):
        ranking = Ranking(self.ibge, ["FERNANDO"], "M", decadas=[1990])
        item = Item(
            self.ibge, "fernando", 169079, sexo="M", decada=1990, localidade="BR"
        )
        ranking.adiciona_item(item)
        nome_arquivo = ranking.exporta_json_ranking()

        self.assertTrue(os.path.exists(nome_arquivo))

        with open(nome_arquivo, "r") as arquivo:
            dados = json.load(arquivo)
            self.assertEqual(len(dados), 1)
            self.assertEqual(dados[0]["nome"], "FERNANDO")
            self.assertEqual(dados[0]["sexo"], "M")
            self.assertEqual(dados[0]["localidade"], "BR")
            self.assertEqual(dados[0]["decada"], 1990)
            self.assertEqual(dados[0]["frequencia"], 169079)

        os.remove(nome_arquivo)

    def teste_importa_json_nomes(self):
        itens_json = ["FERNANDO", "MARIA", "LUCAS", "CARLOS"]

        with open("nomes.json", "w") as json_file:
            json.dump(itens_json, json_file)

        ranking = Ranking(self.ibge, arquivo="nomes")
        ranking.importa_json_nomes()

        self.assertListEqual(itens_json, ranking.nomes)

        os.remove("nomes.json")


if __name__ == "__main__":
    unittest.main()
