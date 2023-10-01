from rankings.ranking import Ranking
from services.ibge import Ibge
import unittest


class Teste(unittest.TestCase):
    def setUp(self):
        self.api = Ibge(3, 5)
        self.localidades = ["11", "33"]
        self.decadas = [1930, 1940]
        self.nomes = ["lucas", "pedro", "carlos"]
        self.nomes_sexo = ["lucas", "pedro", "carlos", "maria"]

    def teste_sem_nomes(self):
        ranking = Ranking(self.api, None, None, None, None)
        self.assertEqual(
            ranking.exibir_ranking(),
            "Ranking geral dos nomes:\n1º - MARIA - 11734129\n2º - JOSE - 5754529\n3º - ANA - 3089858\n4º - JOAO - 2984119\n5º - ANTONIO - 2576348\n6º - FRANCISCO - 1772197\n7º - CARLOS - 1489191\n8º - PAULO - 1423262\n9º - PEDRO - 1219605\n10º - LUCAS - 1127310\n11º - LUIZ - 1107792\n12º - MARCOS - 1106165\n13º - LUIS - 935905\n14º - GABRIEL - 932449\n15º - RAFAEL - 821638\n16º - FRANCISCA - 725642\n17º - DANIEL - 711338\n18º - MARCELO - 693215\n19º - BRUNO - 668217\n20º - EDUARDO - 632664\n",
        )

    def teste_sem_nomes_com_localidades(self):
        ranking = Ranking(self.api, None, self.localidades, None, None)
        self.assertEqual(
            ranking.exibir_ranking(),
            "Ranking geral dos nomes por localidade:\n\nLocalidade: 11\n1º - MARIA - 72579\n2º - JOSE - 37986\n3º - JOAO - 23366\n4º - ANA - 20134\n5º - ANTONIO - 16252\n6º - FRANCISCO - 11594\n7º - PAULO - 10402\n8º - LUCAS - 9910\n9º - CARLOS - 9525\n10º - MARCOS - 9150\n11º - PEDRO - 8838\n12º - LUIZ - 7655\n13º - GABRIEL - 6807\n14º - MATEUS - 6056\n15º - RAIMUNDO - 5380\n16º - DANIEL - 5298\n17º - RAFAEL - 5268\n18º - BRUNO - 5028\n19º - TIAGO - 5003\n20º - SEBASTIAO - 4883\n\nLocalidade: 33\n1º - MARIA - 752021\n2º - JOSE - 314276\n3º - ANA - 297079\n4º - JOAO - 208941\n5º - CARLOS - 191014\n6º - PAULO - 158797\n7º - ANTONIO - 144954\n8º - LUIZ - 128256\n9º - JORGE - 115461\n10º - MARCOS - 112525\n11º - PEDRO - 101736\n12º - LUCAS - 99990\n13º - GABRIEL - 95954\n14º - LUIS - 90032\n15º - MARCELO - 88994\n16º - RAFAEL - 85723\n17º - MARCIA - 71954\n18º - LEONARDO - 71693\n19º - BRUNO - 70446\n20º - RODRIGO - 70436\n",
        )

    def teste_sem_nomes_com_localidades_e_sexo(self):
        ranking = Ranking(self.api, None, self.localidades, "M", None)
        self.assertEqual(
            ranking.exibir_ranking(),
            "Ranking geral dos nomes do sexo Masculino por localidade:\n\nLocalidade: 11\n1º - JOSE\n2º - JOAO\n3º - ANTONIO\n4º - FRANCISCO\n5º - PAULO\n6º - LUCAS\n7º - CARLOS\n8º - MARCOS\n9º - PEDRO\n10º - LUIZ\n11º - GABRIEL\n12º - MATEUS\n13º - RAIMUNDO\n14º - DANIEL\n15º - RAFAEL\n16º - BRUNO\n17º - TIAGO\n18º - SEBASTIAO\n19º - EDUARDO\n20º - MARCELO\n\nLocalidade: 33\n1º - JOSE\n2º - JOAO\n3º - CARLOS\n4º - PAULO\n5º - ANTONIO\n6º - LUIZ\n7º - JORGE\n8º - MARCOS\n9º - PEDRO\n10º - LUCAS\n11º - GABRIEL\n12º - LUIS\n13º - MARCELO\n14º - RAFAEL\n15º - LEONARDO\n16º - RODRIGO\n17º - BRUNO\n18º - FRANCISCO\n19º - DANIEL\n20º - FELIPE\n",
        )

    def teste_sem_nomes_com_localidades_e_decadas(self):
        ranking = Ranking(self.api, None, self.localidades, None, self.decadas)
        self.assertEqual(
            ranking.exibir_ranking(),
            "Ranking geral dos nomes por localidade e década:\n\nDécada: 1930\n\nLocalidade: 11\n1º - MARIA\n2º - JOSE\n3º - JOAO\n4º - ANTONIO\n5º - FRANCISCO\n6º - MANOEL\n7º - FRANCISCA\n8º - SEBASTIAO\n9º - ANA\n10º - RAIMUNDO\n11º - PEDRO\n12º - JOAQUIM\n13º - RAIMUNDA\n14º - ANTONIA\n15º - LUIZ\n16º - MANUEL\n17º - GERALDO\n18º - JOANA\n19º - BENEDITO\n20º - ROSA\n\nLocalidade: 33\n1º - MARIA\n2º - JOSE\n3º - ANTONIO\n4º - JOAO\n5º - MANOEL\n6º - FRANCISCO\n7º - ANA\n8º - SEBASTIAO\n9º - NAIR\n10º - ELZA\n11º - FRANCISCA\n12º - ROSA\n13º - IRENE\n14º - ANTONIA\n15º - MANUEL\n16º - SEBASTIANA\n17º - PEDRO\n18º - JORGE\n19º - ALICE\n20º - HELENA\n\nDécada: 1940\n\nLocalidade: 11\n1º - MARIA\n2º - JOSE\n3º - ANTONIO\n4º - JOAO\n5º - FRANCISCO\n6º - MANOEL\n7º - SEBASTIAO\n8º - PEDRO\n9º - ANA\n10º - FRANCISCA\n11º - RAIMUNDO\n12º - RAIMUNDA\n13º - GERALDO\n14º - JOAQUIM\n15º - MANUEL\n16º - ANTONIA\n17º - LUIZ\n18º - JOSEFA\n19º - TEREZINHA\n20º - LUZIA\n\nLocalidade: 33\n1º - MARIA\n2º - JOSE\n3º - ANTONIO\n4º - JOAO\n5º - MANOEL\n6º - FRANCISCO\n7º - SEBASTIAO\n8º - JORGE\n9º - TEREZINHA\n10º - MARLENE\n11º - ANA\n12º - LUIZ\n13º - PAULO\n14º - ELZA\n15º - CARLOS\n16º - PEDRO\n17º - MANUEL\n18º - GERALDO\n19º - FRANCISCA\n20º - IRENE\n",
        )

    def teste_sem_nomes_com_localidades_sexo_e_decadas(self):
        ranking = Ranking(self.api, None, self.localidades, "M", self.decadas)
        self.assertEqual(
            ranking.exibir_ranking(),
            "Ranking geral dos nomes do sexo Masculino por localidade e década:\n\nDécada: 1930\n\nLocalidade: 11\n1º - JOSE\n2º - JOAO\n3º - ANTONIO\n4º - FRANCISCO\n5º - MANOEL\n6º - SEBASTIAO\n7º - RAIMUNDO\n8º - PEDRO\n9º - JOAQUIM\n10º - MANUEL\n11º - LUIZ\n12º - GERALDO\n13º - BENEDITO\n14º - VICENTE\n15º - MIGUEL\n16º - LUIS\n17º - ALFREDO\n18º - JORGE\n19º - JULIO\n20º - VALDEMAR\n\nLocalidade: 33\n1º - JOSE\n2º - ANTONIO\n3º - JOAO\n4º - MANOEL\n5º - FRANCISCO\n6º - SEBASTIAO\n7º - MANUEL\n8º - PEDRO\n9º - JORGE\n10º - LUIZ\n11º - GERALDO\n12º - JOAQUIM\n13º - PAULO\n14º - MARIO\n15º - CARLOS\n16º - NELSON\n17º - HELIO\n18º - LUIS\n19º - WALTER\n20º - WILSON\n\nDécada: 1940\n\nLocalidade: 11\n1º - JOSE\n2º - ANTONIO\n3º - JOAO\n4º - FRANCISCO\n5º - MANOEL\n6º - SEBASTIAO\n7º - PEDRO\n8º - RAIMUNDO\n9º - GERALDO\n10º - JOAQUIM\n11º - MANUEL\n12º - LUIZ\n13º - OSVALDO\n14º - PAULO\n15º - BENEDITO\n16º - VICENTE\n17º - ADAO\n18º - JORGE\n19º - LUIS\n20º - VALDEMAR\n\nLocalidade: 33\n1º - JOSE\n2º - ANTONIO\n3º - JOAO\n4º - MANOEL\n5º - FRANCISCO\n6º - SEBASTIAO\n7º - JORGE\n8º - LUIZ\n9º - PAULO\n10º - CARLOS\n11º - PEDRO\n12º - MANUEL\n13º - GERALDO\n14º - MARIO\n15º - JOAQUIM\n16º - NELSON\n17º - HELIO\n18º - LUIS\n19º - ROBERTO\n20º - FERNANDO\n",
        )

    def teste_sem_nomes_com_sexo(self):
        ranking = Ranking(self.api, None, None, "F", None)
        self.assertEqual(
            ranking.exibir_ranking(),
            "Ranking geral dos nomes do sexo Feminino:\n1º - MARIA\n2º - ANA\n3º - FRANCISCA\n4º - ANTONIA\n5º - ADRIANA\n6º - JULIANA\n7º - MARCIA\n8º - FERNANDA\n9º - PATRICIA\n10º - ALINE\n11º - SANDRA\n12º - CAMILA\n13º - AMANDA\n14º - BRUNA\n15º - JESSICA\n16º - LETICIA\n17º - JULIA\n18º - LUCIANA\n19º - VANESSA\n20º - MARIANA\n",
        )

    def teste_sem_nomes_com_sexo_e_decadas(self):
        ranking = Ranking(self.api, None, None, "F", self.decadas)
        self.assertEqual(
            ranking.exibir_ranking(),
            "Ranking geral dos nomes do sexo Masculino por década:\n\nDécada: 1930\n1º - JOSE\n2º - ANTONIO\n3º - JOAO\n4º - FRANCISCO\n5º - MANOEL\n6º - PEDRO\n7º - SEBASTIAO\n8º - RAIMUNDO\n9º - JOAQUIM\n10º - MANUEL\n11º - LUIZ\n12º - GERALDO\n13º - BENEDITO\n14º - LUIS\n15º - SEVERINO\n16º - MARIO\n17º - PAULO\n18º - VICENTE\n19º - MIGUEL\n20º - CARLOS\n\nDécada: 1940\n1º - JOSE\n2º - ANTONIO\n3º - JOAO\n4º - FRANCISCO\n5º - MANOEL\n6º - PEDRO\n7º - SEBASTIAO\n8º - RAIMUNDO\n9º - LUIZ\n10º - GERALDO\n11º - JOAQUIM\n12º - MANUEL\n13º - BENEDITO\n14º - PAULO\n15º - LUIS\n16º - CARLOS\n17º - NELSON\n18º - MARIO\n19º - OSVALDO\n20º - SEVERINO\n",
        )

    def teste_sem_nomes_com_decadas(self):
        ranking = Ranking(self.api, None, None, None, self.decadas)
        self.assertEqual(
            ranking.exibir_ranking(),
            "Ranking geral dos nomes por década:\n\nDécada: 1930\n1º - MARIA\n2º - JOSE\n3º - ANTONIO\n4º - JOAO\n5º - ANA\n6º - FRANCISCO\n7º - MANOEL\n8º - FRANCISCA\n9º - ANTONIA\n10º - PEDRO\n11º - JOSEFA\n12º - RAIMUNDO\n13º - SEBASTIAO\n14º - RAIMUNDA\n15º - ROSA\n16º - JOANA\n17º - JOAQUIM\n18º - MANUEL\n19º - LUIZ\n20º - SEBASTIANA\n\nDécada: 1940\n1º - MARIA\n2º - JOSE\n3º - ANTONIO\n4º - JOAO\n5º - FRANCISCO\n6º - MANOEL\n7º - ANA\n8º - FRANCISCA\n9º - PEDRO\n10º - SEBASTIAO\n11º - TEREZINHA\n12º - ANTONIA\n13º - RAIMUNDO\n14º - JOSEFA\n15º - RAIMUNDA\n16º - LUIZ\n17º - TEREZA\n18º - GERALDO\n19º - JOAQUIM\n20º - MANUEL\n",
        )

    def teste_com_nomes(self):
        ranking = Ranking(self.api, self.nomes, None, None, None)
        self.assertEqual(
            ranking.exibir_ranking(),
            "Ranking dos nomes:\n1º - LUCAS\n2º - PEDRO\n3º - CARLOS\n",
        )

    def teste_com_nomes_e_localidades(self):
        ranking = Ranking(self.api, self.nomes, self.localidades)
        self.assertEqual(
            ranking.exibir_ranking(),
            "Ranking dos nomes por localidade:\n\nLocalidade: 11\n1º - LUCAS\n2º - PEDRO\n3º - CARLOS\n\nLocalidade: 33\n1º - LUCAS\n2º - PEDRO\n3º - CARLOS\n",
        )

    def teste_com_nomes_localidades_e_sexo(self):
        ranking = Ranking(self.api, self.nomes_sexo, self.localidades, "F")
        self.assertEqual(
            ranking.exibir_ranking(),
            "Ranking dos nomes do sexo Feminino por localidade:\n\nLocalidade: 11\n1º - MARIA\n2º - LUCAS\n3º - PEDRO\n4º - CARLOS\n\nLocalidade: 33\n1º - MARIA\n2º - LUCAS\n3º - PEDRO\n4º - CARLOS\n",
        )

    def teste_com_nomes_localidades_sexo_e_decadas(self):
        ranking = Ranking(
            self.api, self.nomes_sexo, self.localidades, "M", self.decadas
        )
        self.assertEqual(
            ranking.exibir_ranking(),
            "Ranking dos nomes do sexo Masculino por localidade e década:\n\nDécada: 1930\n\nLocalidade: 11\n1º - LUCAS\n2º - PEDRO\n3º - CARLOS\n4º - MARIA\n\nLocalidade: 33\n1º - LUCAS\n2º - PEDRO\n3º - CARLOS\n4º - MARIA\n\nDécada: 1940\n\nLocalidade: 11\n1º - LUCAS\n2º - PEDRO\n3º - CARLOS\n4º - MARIA\n\nLocalidade: 33\n1º - LUCAS\n2º - PEDRO\n3º - CARLOS\n4º - MARIA\n",
        )

    def teste_com_nomes_e_sexo(self):
        ranking = Ranking(self.api, self.nomes_sexo, sexo="F")
        self.assertEqual(
            ranking.exibir_ranking(),
            "Ranking dos nomes do sexo Feminino:\n1º - MARIA\n2º - LUCAS\n3º - PEDRO\n4º - CARLOS\n",
        )

    def teste_com_nomes_sexo_e_decadas(self):
        ranking = Ranking(self.api, self.nomes_sexo, decadas=self.decadas, sexo="M")
        self.assertEqual(
            ranking.exibir_ranking(),
            "Ranking dos nomes do sexo Masculino por década:\n\nDécada: 1930\n1º - LUCAS\n2º - PEDRO\n3º - CARLOS\n4º - MARIA\n\nDécada: 1940\n1º - LUCAS\n2º - PEDRO\n3º - CARLOS\n4º - MARIA\n",
        )

    def teste_com_nomes_e_decadas(self):
        ranking = Ranking(self.api, self.nomes_sexo, decadas=self.decadas)
        self.assertEqual(
            ranking.exibir_ranking(),
            "Ranking dos nomes por década:\n\nDécada: 1930\n1º - MARIA\n2º - LUCAS\n3º - PEDRO\n4º - CARLOS\n\nDécada: 1940\n1º - MARIA\n2º - LUCAS\n3º - PEDRO\n4º - CARLOS\n",
        )


if __name__ == "__main__":
    unittest.main()
