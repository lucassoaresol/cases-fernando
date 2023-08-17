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

    def test_sem_nomes_com_localidades_e_sexo(self):
        ranking = Ranking(self.api, True, False, "M")
        localidades = ["11", "33"]
        self.assertEqual(
            ranking.geral(localidades),
            "Ranking geral dos nomes do sexo Masculino por localidade:\n\nLocalidade: 11\n1º - JOSE\n2º - JOAO\n3º - ANTONIO\n4º - FRANCISCO\n5º - PAULO\n6º - LUCAS\n7º - CARLOS\n8º - MARCOS\n9º - PEDRO\n10º - LUIZ\n11º - GABRIEL\n12º - MATEUS\n13º - RAIMUNDO\n14º - DANIEL\n15º - RAFAEL\n16º - BRUNO\n17º - TIAGO\n18º - SEBASTIAO\n19º - EDUARDO\n20º - MARCELO\n\nLocalidade: 33\n1º - JOSE\n2º - JOAO\n3º - CARLOS\n4º - PAULO\n5º - ANTONIO\n6º - LUIZ\n7º - JORGE\n8º - MARCOS\n9º - PEDRO\n10º - LUCAS\n11º - GABRIEL\n12º - LUIS\n13º - MARCELO\n14º - RAFAEL\n15º - LEONARDO\n16º - RODRIGO\n17º - BRUNO\n18º - FRANCISCO\n19º - DANIEL\n20º - FELIPE\n",
        )

    def test_sem_nomes_com_localidades_e_decadas(self):
        ranking = Ranking(self.api, True, True)
        localidades = ["11", "33"]
        decadas = ["1930", "1940"]
        self.assertEqual(
            ranking.geral(localidades, decadas),
            "Ranking geral dos nomes por localidade e década:\n\nDécada: 1930\n\nLocalidade: 11\n1º - MARIA\n2º - JOSE\n3º - JOAO\n4º - ANTONIO\n5º - FRANCISCO\n6º - MANOEL\n7º - FRANCISCA\n8º - SEBASTIAO\n9º - ANA\n10º - RAIMUNDO\n11º - PEDRO\n12º - JOAQUIM\n13º - RAIMUNDA\n14º - ANTONIA\n15º - LUIZ\n16º - MANUEL\n17º - GERALDO\n18º - JOANA\n19º - BENEDITO\n20º - ROSA\n\nLocalidade: 33\n1º - MARIA\n2º - JOSE\n3º - ANTONIO\n4º - JOAO\n5º - MANOEL\n6º - FRANCISCO\n7º - ANA\n8º - SEBASTIAO\n9º - NAIR\n10º - ELZA\n11º - FRANCISCA\n12º - ROSA\n13º - IRENE\n14º - ANTONIA\n15º - MANUEL\n16º - SEBASTIANA\n17º - PEDRO\n18º - JORGE\n19º - ALICE\n20º - HELENA\n\nDécada: 1940\n\nLocalidade: 11\n1º - MARIA\n2º - JOSE\n3º - ANTONIO\n4º - JOAO\n5º - FRANCISCO\n6º - MANOEL\n7º - SEBASTIAO\n8º - PEDRO\n9º - ANA\n10º - FRANCISCA\n11º - RAIMUNDO\n12º - RAIMUNDA\n13º - GERALDO\n14º - JOAQUIM\n15º - MANUEL\n16º - ANTONIA\n17º - LUIZ\n18º - JOSEFA\n19º - TEREZINHA\n20º - LUZIA\n\nLocalidade: 33\n1º - MARIA\n2º - JOSE\n3º - ANTONIO\n4º - JOAO\n5º - MANOEL\n6º - FRANCISCO\n7º - SEBASTIAO\n8º - JORGE\n9º - TEREZINHA\n10º - MARLENE\n11º - ANA\n12º - LUIZ\n13º - PAULO\n14º - ELZA\n15º - CARLOS\n16º - PEDRO\n17º - MANUEL\n18º - GERALDO\n19º - FRANCISCA\n20º - IRENE\n",
        )

    def test_sem_nomes_com_localidades_sexo_e_decadas(self):
        ranking = Ranking(self.api, True, True, "M")
        localidades = ["11", "33"]
        decadas = ["1930", "1940"]
        self.assertEqual(
            ranking.geral(localidades, decadas),
            "Ranking geral dos nomes do sexo Masculino por localidade e década:\n\nDécada: 1930\n\nLocalidade: 11\n1º - JOSE\n2º - JOAO\n3º - ANTONIO\n4º - FRANCISCO\n5º - MANOEL\n6º - SEBASTIAO\n7º - RAIMUNDO\n8º - PEDRO\n9º - JOAQUIM\n10º - MANUEL\n11º - LUIZ\n12º - GERALDO\n13º - BENEDITO\n14º - VICENTE\n15º - MIGUEL\n16º - LUIS\n17º - ALFREDO\n18º - JORGE\n19º - JULIO\n20º - VALDEMAR\n\nLocalidade: 33\n1º - JOSE\n2º - ANTONIO\n3º - JOAO\n4º - MANOEL\n5º - FRANCISCO\n6º - SEBASTIAO\n7º - MANUEL\n8º - PEDRO\n9º - JORGE\n10º - LUIZ\n11º - GERALDO\n12º - JOAQUIM\n13º - PAULO\n14º - MARIO\n15º - CARLOS\n16º - NELSON\n17º - HELIO\n18º - LUIS\n19º - WALTER\n20º - WILSON\n\nDécada: 1940\n\nLocalidade: 11\n1º - JOSE\n2º - ANTONIO\n3º - JOAO\n4º - FRANCISCO\n5º - MANOEL\n6º - SEBASTIAO\n7º - PEDRO\n8º - RAIMUNDO\n9º - GERALDO\n10º - JOAQUIM\n11º - MANUEL\n12º - LUIZ\n13º - OSVALDO\n14º - PAULO\n15º - BENEDITO\n16º - VICENTE\n17º - ADAO\n18º - JORGE\n19º - LUIS\n20º - VALDEMAR\n\nLocalidade: 33\n1º - JOSE\n2º - ANTONIO\n3º - JOAO\n4º - MANOEL\n5º - FRANCISCO\n6º - SEBASTIAO\n7º - JORGE\n8º - LUIZ\n9º - PAULO\n10º - CARLOS\n11º - PEDRO\n12º - MANUEL\n13º - GERALDO\n14º - MARIO\n15º - JOAQUIM\n16º - NELSON\n17º - HELIO\n18º - LUIS\n19º - ROBERTO\n20º - FERNANDO\n",
        )

    def test_sem_nomes_com_sexo(self):
        ranking = Ranking(self.api, False, False, "F")
        self.assertEqual(
            ranking.geral(),
            "Ranking geral dos nomes do sexo Feminino:\n1º - MARIA\n2º - ANA\n3º - FRANCISCA\n4º - ANTONIA\n5º - ADRIANA\n6º - JULIANA\n7º - MARCIA\n8º - FERNANDA\n9º - PATRICIA\n10º - ALINE\n11º - SANDRA\n12º - CAMILA\n13º - AMANDA\n14º - BRUNA\n15º - JESSICA\n16º - LETICIA\n17º - JULIA\n18º - LUCIANA\n19º - VANESSA\n20º - MARIANA\n",
        )

    def test_sem_nomes_com_sexo_e_decadas(self):
        ranking = Ranking(self.api, False, True, "M")
        decadas = ["1930", "1940"]
        self.assertEqual(
            ranking.geral(decadas=decadas),
            "Ranking geral dos nomes do sexo Masculino por década:\n\nDécada: 1930\n1º - JOSE\n2º - ANTONIO\n3º - JOAO\n4º - FRANCISCO\n5º - MANOEL\n6º - PEDRO\n7º - SEBASTIAO\n8º - RAIMUNDO\n9º - JOAQUIM\n10º - MANUEL\n11º - LUIZ\n12º - GERALDO\n13º - BENEDITO\n14º - LUIS\n15º - SEVERINO\n16º - MARIO\n17º - PAULO\n18º - VICENTE\n19º - MIGUEL\n20º - CARLOS\n\nDécada: 1940\n1º - JOSE\n2º - ANTONIO\n3º - JOAO\n4º - FRANCISCO\n5º - MANOEL\n6º - PEDRO\n7º - SEBASTIAO\n8º - RAIMUNDO\n9º - LUIZ\n10º - GERALDO\n11º - JOAQUIM\n12º - MANUEL\n13º - BENEDITO\n14º - PAULO\n15º - LUIS\n16º - CARLOS\n17º - NELSON\n18º - MARIO\n19º - OSVALDO\n20º - SEVERINO\n",
        )

    def test_sem_nomes_com_decadas(self):
        ranking = Ranking(self.api, False, True)
        decadas = ["1930", "1940"]
        self.assertEqual(
            ranking.geral(decadas=decadas),
            "Ranking geral dos nomes por década:\n\nDécada: 1930\n1º - MARIA\n2º - JOSE\n3º - ANTONIO\n4º - JOAO\n5º - ANA\n6º - FRANCISCO\n7º - MANOEL\n8º - FRANCISCA\n9º - ANTONIA\n10º - PEDRO\n11º - JOSEFA\n12º - RAIMUNDO\n13º - SEBASTIAO\n14º - RAIMUNDA\n15º - ROSA\n16º - JOANA\n17º - JOAQUIM\n18º - MANUEL\n19º - LUIZ\n20º - SEBASTIANA\n\nDécada: 1940\n1º - MARIA\n2º - JOSE\n3º - ANTONIO\n4º - JOAO\n5º - FRANCISCO\n6º - MANOEL\n7º - ANA\n8º - FRANCISCA\n9º - PEDRO\n10º - SEBASTIAO\n11º - TEREZINHA\n12º - ANTONIA\n13º - RAIMUNDO\n14º - JOSEFA\n15º - RAIMUNDA\n16º - LUIZ\n17º - TEREZA\n18º - GERALDO\n19º - JOAQUIM\n20º - MANUEL\n",
        )

    def test_com_nomes(self):
        ranking = Ranking(self.api, False, False)
        nomes = ["lucas", "pedro", "carlos"]
        nomes_frequencia = Item(self.api, nomes).frequencia()
        self.assertEqual(
            ranking.nomes(nomes_frequencia),
            "Ranking dos nomes:\n1º - LUCAS\n2º - PEDRO\n3º - CARLOS\n",
        )

    def test_com_nomes_e_localidades(self):
        ranking = Ranking(self.api, True, False)
        nomes = ["lucas", "pedro", "carlos"]
        localidades = ["11", "33"]
        nomes_frequencia = Item(self.api, nomes).frequencia(localidades)
        self.assertEqual(
            ranking.nomes(nomes_frequencia),
            "Ranking dos nomes por localidade:\n\nLocalidade: 11\n1º - LUCAS\n2º - PEDRO\n3º - CARLOS\n\nLocalidade: 33\n1º - LUCAS\n2º - PEDRO\n3º - CARLOS\n",
        )

    def test_com_nomes_localidades_e_sexo(self):
        ranking = Ranking(self.api, True, False, "F")
        nomes = ["lucas", "pedro", "carlos", "maria"]
        localidades = ["11", "33"]
        nomes_frequencia = Item(self.api, nomes, "F").frequencia(localidades)
        self.assertEqual(
            ranking.nomes(nomes_frequencia),
            "Ranking dos nomes do sexo Feminino por localidade:\n\nLocalidade: 11\n1º - MARIA\n2º - LUCAS\n3º - PEDRO\n4º - CARLOS\n\nLocalidade: 33\n1º - MARIA\n2º - LUCAS\n3º - PEDRO\n4º - CARLOS\n",
        )

    def test_com_nomes_e_sexo(self):
        ranking = Ranking(self.api, False, False, "F")
        nomes = ["lucas", "pedro", "carlos", "maria"]
        nomes_frequencia = Item(self.api, nomes, "F").frequencia()
        self.assertEqual(
            ranking.nomes(nomes_frequencia),
            "Ranking dos nomes do sexo Feminino:\n1º - MARIA\n2º - LUCAS\n3º - PEDRO\n4º - CARLOS\n",
        )


if __name__ == "__main__":
    unittest.main()
