from itens import Item
from rankings import Ranking
from services import Api
import unittest


class Teste(unittest.TestCase):
    def setUp(self):
        self.api = Api()

    def test_sem_nomes(self):
        ranking = Ranking(self.api, False, False)
        self.assertEqual(
            ranking.geral(),
            "Ranking geral dos nomes:\n1º - MARIA\n2º - JOSE\n3º - ANA\n4º - JOAO\n5º - ANTONIO\n6º - FRANCISCO\n7º - CARLOS\n8º - PAULO\n9º - PEDRO\n10º - LUCAS\n11º - LUIZ\n12º - MARCOS\n13º - LUIS\n14º - GABRIEL\n15º - RAFAEL\n16º - FRANCISCA\n17º - DANIEL\n18º - MARCELO\n19º - BRUNO\n20º - EDUARDO\n",
        )

    def test_sem_nomes_com_localidades(self):
        ranking = Ranking(self.api, True, False)
        localidades = ["11", "33"]
        self.assertEqual(
            ranking.geral(localidades),
            "Ranking geral dos nomes por localidade:\n\nLocalidade: 11\n1º - MARIA\n2º - JOSE\n3º - JOAO\n4º - ANA\n5º - ANTONIO\n6º - FRANCISCO\n7º - PAULO\n8º - LUCAS\n9º - CARLOS\n10º - MARCOS\n11º - PEDRO\n12º - LUIZ\n13º - GABRIEL\n14º - MATEUS\n15º - RAIMUNDO\n16º - DANIEL\n17º - RAFAEL\n18º - BRUNO\n19º - TIAGO\n20º - SEBASTIAO\n\nLocalidade: 33\n1º - MARIA\n2º - JOSE\n3º - ANA\n4º - JOAO\n5º - CARLOS\n6º - PAULO\n7º - ANTONIO\n8º - LUIZ\n9º - JORGE\n10º - MARCOS\n11º - PEDRO\n12º - LUCAS\n13º - GABRIEL\n14º - LUIS\n15º - MARCELO\n16º - RAFAEL\n17º - MARCIA\n18º - LEONARDO\n19º - BRUNO\n20º - RODRIGO\n",
        )

    def test_sem_nomes_com_sexo(self):
        ranking = Ranking(self.api, False, False, "F")
        self.assertEqual(
            ranking.geral(),
            "Ranking geral dos nomes do sexo Feminino:\n1º - MARIA\n2º - ANA\n3º - FRANCISCA\n4º - ANTONIA\n5º - ADRIANA\n6º - JULIANA\n7º - MARCIA\n8º - FERNANDA\n9º - PATRICIA\n10º - ALINE\n11º - SANDRA\n12º - CAMILA\n13º - AMANDA\n14º - BRUNA\n15º - JESSICA\n16º - LETICIA\n17º - JULIA\n18º - LUCIANA\n19º - VANESSA\n20º - MARIANA\n",
        )

    def test_com_nomes(self):
        nomes = ["lucas", "pedro", "carlos"]
        nomes_frequencia = Item(self.api, nomes).frequencia()
        ranking = Ranking(self.api, False, False)
        self.assertEqual(
            ranking.nomes(nomes_frequencia),
            "Ranking dos nomes:\n1º - LUCAS\n2º - PEDRO\n3º - CARLOS\n",
        )


if __name__ == "__main__":
    unittest.main()
