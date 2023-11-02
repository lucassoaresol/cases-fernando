from services.redis import Redis
from testes import constantes
import unittest


class TestRedis(unittest.TestCase):
    def teste_key_ranking(self):
        redis = Redis(constantes.ibge)
        self.assertEqual(redis.define_key("ranking", "M"), "ranking-M")

    def teste_key_nome(self):
        redis = Redis(constantes.ibge)
        self.assertEqual(
            redis.define_key("FERNANDO", "M", decada=1930), "FERNANDO-M-1930"
        )

    def teste_key_localidade(self):
        redis = Redis(constantes.ibge)
        self.assertEqual(redis.define_key("localidade", localidade=12), "localidade-12")

    def teste_ranking(self):
        redis = Redis(constantes.ibge_ranking_geral)
        self.assertEqual(redis.ranking(), constantes.ranking_geral[0]["res"])

    def teste_frequencia(self):
        redis = Redis(constantes.ibge)
        self.assertEqual(
            redis.frequencia("FERNANDO"), constantes.nome_sem_parametros[0]["res"]
        )

    def teste_localidade(self):
        redis = Redis(constantes.ibge)
        self.assertEqual(redis.localidade("43"), constantes.siglas_estados)


if __name__ == "__main__":
    unittest.main()
