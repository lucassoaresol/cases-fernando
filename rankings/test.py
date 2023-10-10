from rankings.ranking import Ranking
from services.ibge import Ibge
import unittest


class TesteRanking(unittest.TestCase):
    def setUp(self):
        self.ibge = Ibge(3, 5)

    def teste_sem_nomes(self):
        ranking = Ranking(self.ibge)
        ranking.define_titulo()
        ranking.gera_ranking()

        self.assertEqual(
            ranking.titulo + ranking.ranking,
            "Ranking geral dos nomes:\n1º - MARIA - 11734129\n2º - JOSE - 5754529\n3º - ANA - 3089858\n4º - JOAO - 2984119\n5º - ANTONIO - 2576348\n6º - FRANCISCO - 1772197\n7º - CARLOS - 1489191\n8º - PAULO - 1423262\n9º - PEDRO - 1219605\n10º - LUCAS - 1127310\n11º - LUIZ - 1107792\n12º - MARCOS - 1106165\n13º - LUIS - 935905\n14º - GABRIEL - 932449\n15º - RAFAEL - 821638\n16º - FRANCISCA - 725642\n17º - DANIEL - 711338\n18º - MARCELO - 693215\n19º - BRUNO - 668217\n20º - EDUARDO - 632664\n",
        )

    def teste_sem_nomes_com_localidades(self):
        ranking = Ranking(self.ibge, localidades=["11", "33"])
        ranking.define_titulo()
        ranking.gera_ranking()

        self.assertEqual(
            ranking.titulo + ranking.ranking,
            "Ranking geral dos nomes por localidade:\n\nLocalidade: 11\n1º - MARIA - 72579\n2º - JOSE - 37986\n3º - JOAO - 23366\n4º - ANA - 20134\n5º - ANTONIO - 16252\n6º - FRANCISCO - 11594\n7º - PAULO - 10402\n8º - LUCAS - 9910\n9º - CARLOS - 9525\n10º - MARCOS - 9150\n11º - PEDRO - 8838\n12º - LUIZ - 7655\n13º - GABRIEL - 6807\n14º - MATEUS - 6056\n15º - RAIMUNDO - 5380\n16º - DANIEL - 5298\n17º - RAFAEL - 5268\n18º - BRUNO - 5028\n19º - TIAGO - 5003\n20º - SEBASTIAO - 4883\n\nLocalidade: 33\n1º - MARIA - 752021\n2º - JOSE - 314276\n3º - ANA - 297079\n4º - JOAO - 208941\n5º - CARLOS - 191014\n6º - PAULO - 158797\n7º - ANTONIO - 144954\n8º - LUIZ - 128256\n9º - JORGE - 115461\n10º - MARCOS - 112525\n11º - PEDRO - 101736\n12º - LUCAS - 99990\n13º - GABRIEL - 95954\n14º - LUIS - 90032\n15º - MARCELO - 88994\n16º - RAFAEL - 85723\n17º - MARCIA - 71954\n18º - LEONARDO - 71693\n19º - BRUNO - 70446\n20º - RODRIGO - 70436\n",
        )

    def teste_sem_nomes_com_localidades_e_sexo(self):
        ranking = Ranking(self.ibge, localidades=["11", "33"], sexo="M")
        ranking.define_titulo()
        ranking.gera_ranking()

        self.assertEqual(
            ranking.titulo + ranking.ranking,
            "Ranking geral dos nomes do sexo Masculino por localidade:\n\nLocalidade: 11\n1º - JOSE - 37858\n2º - JOAO - 23266\n3º - ANTONIO - 16205\n4º - FRANCISCO - 11549\n5º - PAULO - 10351\n6º - LUCAS - 9829\n7º - CARLOS - 9485\n8º - MARCOS - 9107\n9º - PEDRO - 8794\n10º - LUIZ - 7626\n11º - GABRIEL - 6727\n12º - MATEUS - 6007\n13º - RAIMUNDO - 5356\n14º - DANIEL - 5273\n15º - RAFAEL - 5224\n16º - BRUNO - 4983\n17º - TIAGO - 4966\n18º - SEBASTIAO - 4872\n19º - EDUARDO - 4728\n20º - MARCELO - 4485\n\nLocalidade: 33\n1º - JOSE - 312855\n2º - JOAO - 207913\n3º - CARLOS - 190319\n4º - PAULO - 158295\n5º - ANTONIO - 144526\n6º - LUIZ - 127710\n7º - JORGE - 115144\n8º - MARCOS - 112033\n9º - PEDRO - 101097\n10º - LUCAS - 98955\n11º - GABRIEL - 94895\n12º - LUIS - 89628\n13º - MARCELO - 88622\n14º - RAFAEL - 85018\n15º - LEONARDO - 71277\n16º - RODRIGO - 70107\n17º - BRUNO - 69964\n18º - FRANCISCO - 68849\n19º - DANIEL - 67870\n20º - FELIPE - 67505\n",
        )

    def teste_sem_nomes_com_localidades_e_decadas(self):
        ranking = Ranking(
            self.ibge,
            localidades=["11", "33"],
            decadas=[1930, 1940],
        )
        ranking.define_titulo()
        ranking.gera_ranking()

        self.assertEqual(
            ranking.titulo + ranking.ranking,
            "Ranking geral dos nomes por localidade e década:\n\nDécada: 1930\n\nLocalidade: 11\n1º - MARIA - 1059\n2º - JOSE - 618\n3º - JOAO - 335\n4º - ANTONIO - 320\n5º - FRANCISCO - 204\n6º - MANOEL - 158\n7º - FRANCISCA - 146\n8º - SEBASTIAO - 129\n9º - ANA - 127\n10º - RAIMUNDO - 126\n11º - PEDRO - 123\n12º - JOAQUIM - 94\n13º - RAIMUNDA - 92\n14º - ANTONIA - 70\n15º - LUIZ - 63\n16º - MANUEL - 63\n17º - GERALDO - 59\n18º - JOANA - 57\n19º - BENEDITO - 42\n20º - ROSA - 40\n\nLocalidade: 33\n1º - MARIA - 32516\n2º - JOSE - 8376\n3º - ANTONIO - 4216\n4º - JOAO - 3604\n5º - MANOEL - 2219\n6º - FRANCISCO - 1848\n7º - ANA - 1845\n8º - SEBASTIAO - 1634\n9º - NAIR - 1609\n10º - ELZA - 1503\n11º - FRANCISCA - 1264\n12º - ROSA - 1221\n13º - IRENE - 1184\n14º - ANTONIA - 1176\n15º - MANUEL - 1151\n16º - SEBASTIANA - 1095\n17º - PEDRO - 1073\n18º - JORGE - 1069\n19º - ALICE - 1058\n20º - HELENA - 1002\n\nDécada: 1940\n\nLocalidade: 11\n1º - MARIA - 3239\n2º - JOSE - 1977\n3º - ANTONIO - 972\n4º - JOAO - 923\n5º - FRANCISCO - 544\n6º - MANOEL - 419\n7º - SEBASTIAO - 403\n8º - PEDRO - 392\n9º - ANA - 350\n10º - FRANCISCA - 318\n11º - RAIMUNDO - 313\n12º - RAIMUNDA - 241\n13º - GERALDO - 217\n14º - JOAQUIM - 215\n15º - MANUEL - 175\n16º - ANTONIA - 175\n17º - LUIZ - 151\n18º - JOSEFA - 143\n19º - TEREZINHA - 139\n20º - LUZIA - 138\n\nLocalidade: 33\n1º - MARIA - 69834\n2º - JOSE - 23819\n3º - ANTONIO - 11044\n4º - JOAO - 9223\n5º - MANOEL - 5197\n6º - FRANCISCO - 4779\n7º - SEBASTIAO - 4689\n8º - JORGE - 4564\n9º - TEREZINHA - 3683\n10º - MARLENE - 3591\n11º - ANA - 3198\n12º - LUIZ - 3124\n13º - PAULO - 3106\n14º - ELZA - 2899\n15º - CARLOS - 2881\n16º - PEDRO - 2809\n17º - MANUEL - 2797\n18º - GERALDO - 2604\n19º - FRANCISCA - 2261\n20º - IRENE - 2237\n",
        )

    def teste_sem_nomes_com_localidades_sexo_e_decadas(self):
        ranking = Ranking(
            self.ibge,
            localidades=["11", "33"],
            sexo="M",
            decadas=[1930, 1940],
        )
        ranking.define_titulo()
        ranking.gera_ranking()

        self.assertEqual(
            ranking.titulo + ranking.ranking,
            "Ranking geral dos nomes do sexo Masculino por localidade e década:\n\nDécada: 1930\n\nLocalidade: 11\n1º - JOSE - 618\n2º - JOAO - 335\n3º - ANTONIO - 319\n4º - FRANCISCO - 204\n5º - MANOEL - 156\n6º - SEBASTIAO - 127\n7º - RAIMUNDO - 124\n8º - PEDRO - 120\n9º - JOAQUIM - 94\n10º - MANUEL - 63\n11º - LUIZ - 62\n12º - GERALDO - 59\n13º - BENEDITO - 42\n14º - VICENTE - 36\n15º - MIGUEL - 33\n16º - LUIS - 27\n17º - ALFREDO - 26\n18º - JORGE - 21\n19º - JULIO - 21\n20º - VALDEMAR - 19\n\nLocalidade: 33\n1º - JOSE - 8339\n2º - ANTONIO - 4195\n3º - JOAO - 3592\n4º - MANOEL - 2205\n5º - FRANCISCO - 1841\n6º - SEBASTIAO - 1622\n7º - MANUEL - 1145\n8º - PEDRO - 1073\n9º - JORGE - 1065\n10º - LUIZ - 966\n11º - GERALDO - 957\n12º - JOAQUIM - 915\n13º - PAULO - 883\n14º - MARIO - 804\n15º - CARLOS - 793\n16º - NELSON - 655\n17º - HELIO - 475\n18º - LUIS - 471\n19º - WALTER - 459\n20º - WILSON - 458\n\nDécada: 1940\n\nLocalidade: 11\n1º - JOSE - 1970\n2º - ANTONIO - 968\n3º - JOAO - 922\n4º - FRANCISCO - 542\n5º - MANOEL - 419\n6º - SEBASTIAO - 403\n7º - PEDRO - 392\n8º - RAIMUNDO - 313\n9º - GERALDO - 215\n10º - JOAQUIM - 213\n11º - MANUEL - 175\n12º - LUIZ - 151\n13º - OSVALDO - 107\n14º - PAULO - 96\n15º - BENEDITO - 89\n16º - VICENTE - 86\n17º - ADAO - 77\n18º - JORGE - 73\n19º - LUIS - 71\n20º - VALDEMAR - 65\n\nLocalidade: 33\n1º - JOSE - 23755\n2º - ANTONIO - 11014\n3º - JOAO - 9207\n4º - MANOEL - 5186\n5º - FRANCISCO - 4763\n6º - SEBASTIAO - 4674\n7º - JORGE - 4552\n8º - LUIZ - 3116\n9º - PAULO - 3102\n10º - CARLOS - 2875\n11º - PEDRO - 2803\n12º - MANUEL - 2791\n13º - GERALDO - 2590\n14º - MARIO - 1903\n15º - JOAQUIM - 1836\n16º - NELSON - 1708\n17º - HELIO - 1575\n18º - LUIS - 1526\n19º - ROBERTO - 1525\n20º - FERNANDO - 1467\n",
        )

    def teste_sem_nomes_com_sexo(self):
        ranking = Ranking(self.ibge, sexo="F")
        ranking.define_titulo()
        ranking.gera_ranking()

        self.assertEqual(
            ranking.titulo + ranking.ranking,
            "Ranking geral dos nomes do sexo Feminino:\n1º - MARIA - 11694738\n2º - ANA - 3079729\n3º - FRANCISCA - 721637\n4º - ANTONIA - 588783\n5º - ADRIANA - 565621\n6º - JULIANA - 562589\n7º - MARCIA - 551855\n8º - FERNANDA - 531607\n9º - PATRICIA - 529446\n10º - ALINE - 509869\n11º - SANDRA - 479230\n12º - CAMILA - 469851\n13º - AMANDA - 464624\n14º - BRUNA - 460770\n15º - JESSICA - 456472\n16º - LETICIA - 434056\n17º - JULIA - 430067\n18º - LUCIANA - 429769\n19º - VANESSA - 417512\n20º - MARIANA - 381778\n",
        )

    def teste_sem_nomes_com_sexo_e_decadas(self):
        ranking = Ranking(self.ibge, sexo="M", decadas=[1930, 1940])
        ranking.define_titulo()
        ranking.gera_ranking()

        self.assertEqual(
            ranking.titulo + ranking.ranking,
            "Ranking geral dos nomes do sexo Masculino por década:\n\nDécada: 1930\n1º - JOSE - 117671\n2º - ANTONIO - 60397\n3º - JOAO - 59996\n4º - FRANCISCO - 33180\n5º - MANOEL - 28153\n6º - PEDRO - 21432\n7º - SEBASTIAO - 17231\n8º - RAIMUNDO - 17210\n9º - JOAQUIM - 13764\n10º - MANUEL - 12131\n11º - LUIZ - 11024\n12º - GERALDO - 9973\n13º - BENEDITO - 9016\n14º - LUIS - 7595\n15º - SEVERINO - 6447\n16º - MARIO - 6215\n17º - PAULO - 6214\n18º - VICENTE - 5834\n19º - MIGUEL - 5315\n20º - CARLOS - 4642\n\nDécada: 1940\n1º - JOSE - 310427\n2º - ANTONIO - 152996\n3º - JOAO - 141530\n4º - FRANCISCO - 78062\n5º - MANOEL - 59927\n6º - PEDRO - 49057\n7º - SEBASTIAO - 44910\n8º - RAIMUNDO - 41683\n9º - LUIZ - 31039\n10º - GERALDO - 29527\n11º - JOAQUIM - 27443\n12º - MANUEL - 26249\n13º - BENEDITO - 23435\n14º - PAULO - 20701\n15º - LUIS - 20317\n16º - CARLOS - 15586\n17º - NELSON - 15386\n18º - MARIO - 15039\n19º - OSVALDO - 14763\n20º - SEVERINO - 14558\n",
        )

    def teste_sem_nomes_com_decadas(self):
        ranking = Ranking(self.ibge, decadas=[1930, 1940])
        ranking.define_titulo()
        ranking.gera_ranking()

        self.assertEqual(
            ranking.titulo + ranking.ranking,
            "Ranking geral dos nomes por década:\n\nDécada: 1930\n1º - MARIA - 336477\n2º - JOSE - 118121\n3º - ANTONIO - 60651\n4º - JOAO - 60155\n5º - ANA - 33395\n6º - FRANCISCO - 33338\n7º - MANOEL - 28241\n8º - FRANCISCA - 27317\n9º - ANTONIA - 22746\n10º - PEDRO - 21483\n11º - JOSEFA - 19421\n12º - RAIMUNDO - 17300\n13º - SEBASTIAO - 17299\n14º - RAIMUNDA - 16455\n15º - ROSA - 15097\n16º - JOANA - 14520\n17º - JOAQUIM - 13809\n18º - MANUEL - 12185\n19º - LUIZ - 11073\n20º - SEBASTIANA - 10365\n\nDécada: 1940\n1º - MARIA - 749053\n2º - JOSE - 311202\n3º - ANTONIO - 153459\n4º - JOAO - 141772\n5º - FRANCISCO - 78300\n6º - MANOEL - 60061\n7º - ANA - 56160\n8º - FRANCISCA - 50099\n9º - PEDRO - 49143\n10º - SEBASTIAO - 45035\n11º - TEREZINHA - 44876\n12º - ANTONIA - 42629\n13º - RAIMUNDO - 41825\n14º - JOSEFA - 37220\n15º - RAIMUNDA - 31166\n16º - LUIZ - 31114\n17º - TEREZA - 30545\n18º - GERALDO - 29624\n19º - JOAQUIM - 27493\n20º - MANUEL - 26309\n",
        )

    def teste_com_nomes(self):
        ranking = Ranking(self.ibge, ["lucas", "pedro", "carlos"])
        ranking.define_titulo()
        ranking.gera_ranking()

        self.assertEqual(
            ranking.titulo + ranking.ranking,
            "Ranking dos nomes:\n1º - LUCAS - 505306\n2º - PEDRO - 443275\n3º - CARLOS - 266690\n",
        )

    def teste_com_nomes_e_localidades(self):
        ranking = Ranking(
            self.ibge, ["lucas", "pedro", "carlos"], localidades=["11", "33"]
        )
        ranking.define_titulo()
        ranking.gera_ranking()

        self.assertEqual(
            ranking.titulo + ranking.ranking,
            "Ranking dos nomes por localidade:\n\nLocalidade: 11\n1º - LUCAS - 5402\n2º - PEDRO - 3092\n3º - CARLOS - 2701\n\nLocalidade: 33\n1º - LUCAS - 45410\n2º - PEDRO - 40703\n3º - CARLOS - 18710\n",
        )

    def teste_com_nomes_localidades_e_sexo(self):
        ranking = Ranking(
            self.ibge,
            ["lucas", "pedro", "carlos", "maria"],
            "F",
            ["11", "33"],
        )
        ranking.define_titulo()
        ranking.gera_ranking()

        self.assertEqual(
            ranking.titulo + ranking.ranking,
            "Ranking dos nomes do sexo Feminino por localidade:\n\nLocalidade: 11\n1º - MARIA - 5899\n2º - LUCAS - 46\n3º - PEDRO - 28\n4º - CARLOS - 19\n\nLocalidade: 33\n1º - MARIA - 78126\n2º - LUCAS - 505\n3º - PEDRO - 384\n4º - CARLOS - 154\n",
        )

    def teste_com_nomes_localidades_sexo_e_decadas(self):
        ranking = Ranking(
            self.ibge,
            ["lucas", "pedro", "carlos", "maria"],
            "M",
            ["11", "33"],
            [1930, 1940],
        )
        ranking.define_titulo()
        ranking.gera_ranking()

        self.assertEqual(
            ranking.titulo + ranking.ranking,
            "Ranking dos nomes do sexo Masculino por localidade e década:\n\nDécada: 1930\n\nLocalidade: 11\n1º - PEDRO - 120\n2º - CARLOS - 19\n3º - LUCAS - 18\n4º - MARIA - 15\n\nLocalidade: 33\n1º - PEDRO - 1073\n2º - CARLOS - 793\n3º - MARIA - 143\n4º - LUCAS - 26\n\nDécada: 1940\n\nLocalidade: 11\n1º - PEDRO - 392\n2º - CARLOS - 55\n3º - LUCAS - 33\n4º - MARIA - 29\n\nLocalidade: 33\n1º - CARLOS - 2875\n2º - PEDRO - 2803\n3º - MARIA - 256\n4º - LUCAS - 65\n",
        )

    def teste_com_nomes_e_sexo(self):
        ranking = Ranking(
            self.ibge,
            ["lucas", "pedro", "carlos", "maria"],
            "F",
        )
        ranking.define_titulo()
        ranking.gera_ranking()

        self.assertEqual(
            ranking.titulo + ranking.ranking,
            "Ranking dos nomes do sexo Feminino:\n1º - MARIA - 1105524\n2º - LUCAS - 5334\n3º - PEDRO - 3663\n4º - CARLOS - 2244\n",
        )

    def teste_com_nomes_sexo_e_decadas(self):
        ranking = Ranking(
            self.ibge,
            ["lucas", "pedro", "carlos", "maria"],
            "M",
            decadas=[1930, 1940],
        )
        ranking.define_titulo()
        ranking.gera_ranking()

        self.assertEqual(
            ranking.titulo + ranking.ranking,
            "Ranking dos nomes do sexo Masculino por década:\n\nDécada: 1930\n1º - PEDRO - 21432\n2º - CARLOS - 4642\n3º - MARIA - 1529\n4º - LUCAS - 379\n\nDécada: 1940\n1º - PEDRO - 49057\n2º - CARLOS - 15586\n3º - MARIA - 2996\n4º - LUCAS - 917\n",
        )

    def teste_com_nomes_e_decadas(self):
        ranking = Ranking(
            self.ibge,
            ["lucas", "pedro", "carlos", "maria"],
            decadas=[1930, 1940],
        )
        ranking.define_titulo()
        ranking.gera_ranking()

        self.assertEqual(
            ranking.titulo + ranking.ranking,
            "Ranking dos nomes por década:\n\nDécada: 1930\n1º - MARIA - 336477\n2º - PEDRO - 21483\n3º - CARLOS - 4659\n4º - LUCAS - 388\n\nDécada: 1940\n1º - MARIA - 749053\n2º - PEDRO - 49143\n3º - CARLOS - 15620\n4º - LUCAS - 937\n",
        )


if __name__ == "__main__":
    unittest.main()
