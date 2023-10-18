from rankings.ranking import Ranking
from testes.mock import TestMock
import unittest


class TesteRanking(unittest.TestCase):
    def setUp(self):
        self.mock = TestMock()

    def teste_titulo_sem_nomes(self):
        ranking = Ranking(self.mock.ibge)
        ranking.define_titulo()

        self.assertEqual(
            ranking.titulo,
            "Ranking geral dos nomes:\n",
        )

    def teste_titulo_sem_nomes_com_localidades(self):
        ranking = Ranking(self.mock.ibge, localidades=[self.mock.localidade])
        ranking.define_titulo()

        self.assertEqual(
            ranking.titulo,
            "Ranking geral dos nomes por localidade:\n",
        )

    def teste_titulo_sem_nomes_com_localidades_e_sexo(self):
        ranking = Ranking(
            self.mock.ibge, localidades=[self.mock.localidade], sexo=self.mock.sexo
        )
        ranking.define_titulo()

        self.assertEqual(
            ranking.titulo,
            "Ranking geral dos nomes do sexo Masculino por localidade:\n",
        )

    def teste_titulo_sem_nomes_com_localidades_e_decadas(self):
        ranking = Ranking(
            self.mock.ibge,
            localidades=[self.mock.localidade],
            decadas=[self.mock.decada],
        )
        ranking.define_titulo()

        self.assertEqual(
            ranking.titulo,
            "Ranking geral dos nomes por localidade e década:\n",
        )

    def teste_titulo_sem_nomes_com_localidades_sexo_e_decadas(self):
        ranking = Ranking(
            self.mock.ibge,
            localidades=[self.mock.localidade],
            sexo=self.mock.sexo,
            decadas=[self.mock.decada],
        )
        ranking.define_titulo()

        self.assertEqual(
            ranking.titulo,
            "Ranking geral dos nomes do sexo Masculino por localidade e década:\n",
        )

    def teste_titulo_sem_nomes_com_sexo(self):
        ranking = Ranking(self.mock.ibge, sexo=self.mock.sexo)
        ranking.define_titulo()

        self.assertEqual(
            ranking.titulo,
            "Ranking geral dos nomes do sexo Masculino:\n",
        )

    def teste_titulo_sem_nomes_com_sexo_e_decadas(self):
        ranking = Ranking(
            self.mock.ibge, sexo=self.mock.sexo, decadas=[self.mock.decada]
        )
        ranking.define_titulo()

        self.assertEqual(
            ranking.titulo,
            "Ranking geral dos nomes do sexo Masculino por década:\n",
        )

    def teste_titulo_sem_nomes_com_decadas(self):
        ranking = Ranking(self.mock.ibge, decadas=[self.mock.decada])
        ranking.define_titulo()

        self.assertEqual(
            ranking.titulo,
            "Ranking geral dos nomes por década:\n",
        )

    def teste_titulo_com_nomes(self):
        ranking = Ranking(self.mock.ibge, [self.mock.nome])
        ranking.define_titulo()

        self.assertEqual(
            ranking.titulo,
            "Ranking dos nomes:\n",
        )

    def teste_titulo_com_nomes_e_localidades(self):
        ranking = Ranking(
            self.mock.ibge, [self.mock.nome], localidades=[self.mock.localidade]
        )
        ranking.define_titulo()

        self.assertEqual(
            ranking.titulo,
            "Ranking dos nomes por localidade:\n",
        )

    def teste_titulo_com_nomes_localidades_e_sexo(self):
        ranking = Ranking(
            self.mock.ibge, [self.mock.nome], self.mock.sexo, [self.mock.localidade]
        )
        ranking.define_titulo()

        self.assertEqual(
            ranking.titulo,
            "Ranking dos nomes do sexo Masculino por localidade:\n",
        )

    def teste_titulo_com_nomes_localidades_sexo_e_decadas(self):
        ranking = Ranking(
            self.mock.ibge,
            [self.mock.nome],
            self.mock.sexo,
            [self.mock.localidade],
            [self.mock.decada],
        )
        ranking.define_titulo()

        self.assertEqual(
            ranking.titulo,
            "Ranking dos nomes do sexo Masculino por localidade e década:\n",
        )

    def teste_titulo_com_nomes_e_sexo(self):
        ranking = Ranking(self.mock.ibge, [self.mock.nome], self.mock.sexo)
        ranking.define_titulo()

        self.assertEqual(
            ranking.titulo,
            "Ranking dos nomes do sexo Masculino:\n",
        )

    def teste_titulo_com_nomes_sexo_e_decadas(self):
        ranking = Ranking(
            self.mock.ibge, [self.mock.nome], self.mock.sexo, decadas=[self.mock.decada]
        )
        ranking.define_titulo()

        self.assertEqual(
            ranking.titulo,
            "Ranking dos nomes do sexo Masculino por década:\n",
        )

    def teste_titulo_com_nomes_e_decadas(self):
        ranking = Ranking(self.mock.ibge, [self.mock.nome], decadas=[self.mock.decada])
        ranking.define_titulo()

        self.assertEqual(
            ranking.titulo,
            "Ranking dos nomes por década:\n",
        )

    def teste_gera_ranking(self):
        ranking = Ranking(self.mock.ibge, [self.mock.nome])
        ranking.gera_ranking()

        self.assertEqual(
            ranking.ranking,
            "1º - JOÃO - 794118\n",
        )


if __name__ == "__main__":
    unittest.main()
