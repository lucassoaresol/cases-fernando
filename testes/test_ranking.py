from rankings.ranking import Ranking
from services.ibge import Ibge
from testes import constantes
from unittest.mock import Mock
import json
import os
import unittest


class TesteRanking(unittest.TestCase):
    def setUp(self):
        ibge = Mock(Ibge)
        ibge.busca_localidade.return_value = constantes.siglas_estados
        ibge.busca_ranking.return_value = constantes.nome_sem_parametros
        self.ibge = ibge

    def teste_ranking_geral(self):
        ibge = Mock(Ibge)
        ibge.busca_ranking.return_value = constantes.ranking_geral
        ranking = Ranking(ibge)
        ranking.gera_ranking()

        self.assertEqual(len(ranking.itens), 20)

    def teste_ranking_geral_sexo(self):
        ibge = Mock(Ibge)
        ibge.busca_ranking.return_value = constantes.ranking_geral_sexo
        ranking = Ranking(ibge, sexo="F")
        ranking.gera_ranking()

        self.assertEqual(len(ranking.itens), 20)

    def teste_ranking_geral_localidade(self):
        ibge = Mock(Ibge)
        ibge.busca_ranking.return_value = constantes.ranking_geral_localidade
        ibge.busca_localidade.return_value = constantes.siglas_estados
        ranking = Ranking(ibge, localidades=[43])
        ranking.gera_ranking()

        self.assertEqual(
            ranking.mostra_ranking(),
            print(ranking.titulo + ranking.monta_ranking(ranking.itens)),
        )

    def teste_ranking_geral_localidade_decada(self):
        ibge = Mock(Ibge)
        ibge.busca_ranking.return_value = constantes.ranking_com_localidade_decada
        ibge.busca_localidade.return_value = constantes.siglas_estados
        ranking = Ranking(ibge, localidades=[43], decadas=[2010])
        ranking.gera_ranking()

        self.assertEqual(len(ranking.itens), 20)

    def teste_ranking_geral_decada(self):
        ibge = Mock(Ibge)
        ibge.busca_ranking.return_value = constantes.ranking_com_decada
        ranking = Ranking(ibge, decadas=[2000])
        ranking.gera_ranking()

        self.assertEqual(len(ranking.itens), 20)

    def teste_ranking_invalido(self):
        ibge = Mock(Ibge)
        ibge.busca_ranking.return_value = constantes.nome_invalido
        ranking = Ranking(ibge)
        ranking.gera_ranking()

        self.assertEqual(
            ranking.mostra_ranking(),
            print(ranking.titulo + ranking.monta_ranking(ranking.itens)),
        )

    def teste_ranking_nomes_localidades(self):
        ranking = Ranking(self.ibge, ["FERNANDO"], localidades=[43])
        ranking.gera_ranking()

        self.assertEqual(
            ranking.monta_ranking(ranking.itens),
            "\nLocalidade: 43\n1º - FERNANDO - 556346\n",
        )

    def teste_ranking_nomes_decadas(self):
        ranking = Ranking(self.ibge, ["FERNANDO"], decadas=[1980])
        ranking.gera_ranking()

        self.assertEqual(
            ranking.monta_ranking(ranking.itens),
            "\nDécada: 1980\n1º - FERNANDO - 88046\n",
        )

    def teste_ranking_nomes_sexo_localidades_decadas(self):
        ranking = Ranking(self.ibge, ["FERNANDO"], "M", [43], [1990, 2000, 2010])
        ranking.gera_ranking()

        self.assertEqual(
            ranking.mostra_ranking(),
            print(ranking.titulo + ranking.monta_ranking(ranking.itens)),
        )

    def teste_ranking_arquivo(self):
        itens_json = ["FERNANDO"]

        with open("nomes.json", "w") as json_file:
            json.dump(itens_json, json_file)

        ranking = Ranking(self.ibge, arquivo="nomes")
        ranking.gera_ranking()

        os.remove("nomes.json")

        self.assertEqual(len(ranking.itens), 1)

    def teste_exporta_json_ranking(self):
        ibge = Mock(Ibge)
        ibge.busca_ranking.return_value = constantes.nome_com_sexo
        ranking = Ranking(ibge, ["FERNANDO"], "M", decadas=[1990])
        ranking.gera_ranking()
        nome_arquivo = ranking.exporta_json_ranking()

        self.assertTrue(os.path.exists(nome_arquivo))

        with open(nome_arquivo, "r") as arquivo:
            dados = json.load(arquivo)
            self.assertEqual(len(dados), 1)
            self.assertEqual(dados[0]["nome"], "FERNANDO")
            self.assertEqual(dados[0]["sexo"], "M")
            self.assertEqual(dados[0]["localidade"], "BR")
            self.assertEqual(dados[0]["decada"], 1990)
            self.assertEqual(dados[0]["frequencia"], 167744)

        os.remove(nome_arquivo)


if __name__ == "__main__":
    unittest.main()
