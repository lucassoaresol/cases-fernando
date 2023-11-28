from services.cache import Cache
from services.ibge import Ibge
from testes import constantes
from unittest.mock import patch, MagicMock, Mock
import unittest


class TestIbge(unittest.TestCase):
    def setUp(self):
        self.ibge = Ibge()

    def teste_retry_timeout(self):
        self.assertEqual(self.ibge.retry, 3)
        self.assertEqual(self.ibge.timeout, 5)

    def teste_params(self):
        self.assertEqual(self.ibge.params(), None)

    def teste_params_sexo(self):
        self.assertEqual(self.ibge.params("M"), {"sexo": "M"})

    def teste_params_sexo_e_localidade(self):
        self.assertEqual(self.ibge.params("M", 43), {"sexo": "M", "localidade": 43})

    def teste_params_sexo_localidade_e_decada(self):
        self.assertEqual(
            self.ibge.params("M", 43, 1990),
            {"sexo": "M", "localidade": 43, "decada": 1990},
        )

    @patch("services.ibge.Session")
    def teste_config_sessao(self, mock_sessao):
        self.ibge.config_sessao()
        mock_sessao.assert_called_once()

    @patch("services.ibge.Session.get")
    def teste_busca(self, mock_sessao):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = constantes.ranking_geral

        mock_sessao.return_value = mock_response

        url = "https://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking"
        response = self.ibge.busca(url)

        mock_sessao.assert_called_once_with(url, timeout=5, params=None)

        self.assertEqual(response, constantes.ranking_geral)

    @patch("services.ibge.Ibge.busca")
    def teste_busca_ranking_nome_sem_parametros(self, mock_busca):
        mock_busca.return_value = constantes.nome_sem_parametros

        response = self.ibge.busca_ranking("FERNANDO")
        mock_busca.assert_called_once_with(
            "https://servicodados.ibge.gov.br/api/v2/censos/nomes/FERNANDO",
            None,
        )

        self.assertEqual(response, constantes.nome_sem_parametros)

    @patch("services.ibge.Ibge.busca")
    def teste_busca_ranking_nome_invalido(self, mock_busca):
        mock_busca.return_value = constantes.nome_invalido

        response = self.ibge.busca_ranking("fernanndoo")
        mock_busca.assert_called_once_with(
            "https://servicodados.ibge.gov.br/api/v2/censos/nomes/fernanndoo", None
        )

        self.assertEqual(response, constantes.nome_invalido)

    @patch("services.ibge.Ibge.busca")
    def teste_busca_ranking_nome_com_localidade(self, mock_busca):
        mock_busca.return_value = constantes.nome_com_localidade

        response = self.ibge.busca_ranking("FERNANDO", localidade="43")
        mock_busca.assert_called_once_with(
            "https://servicodados.ibge.gov.br/api/v2/censos/nomes/FERNANDO",
            {"localidade": "43"},
        )

        self.assertEqual(response, constantes.nome_com_localidade)

    @patch("services.ibge.Ibge.busca")
    def teste_busca_ranking_nome_com_sexo(self, mock_busca):
        mock_busca.return_value = constantes.nome_com_sexo

        response = self.ibge.busca_ranking("FERNANDO", "M")
        mock_busca.assert_called_once_with(
            "https://servicodados.ibge.gov.br/api/v2/censos/nomes/FERNANDO",
            {"sexo": "M"},
        )

        self.assertEqual(response, constantes.nome_com_sexo)

    @patch("services.ibge.Ibge.busca")
    def teste_busca_ranking_nome_com_localidade_sexo(self, mock_busca):
        mock_busca.return_value = constantes.nome_com_localidade_sexo

        response = self.ibge.busca_ranking("FERNANDO", "M", "43")
        mock_busca.assert_called_once_with(
            "https://servicodados.ibge.gov.br/api/v2/censos/nomes/FERNANDO",
            {"sexo": "M", "localidade": "43"},
        )

        self.assertEqual(response, constantes.nome_com_localidade_sexo)

    @patch("services.ibge.Ibge.busca")
    def teste_busca_ranking_nome_com_localidade_numeral_invalida(self, mock_busca):
        mock_busca.return_value = constantes.nome_com_localidade_numeral_invalida

        response = self.ibge.busca_ranking("FERNANDO", localidade="4311")
        mock_busca.assert_called_once_with(
            "https://servicodados.ibge.gov.br/api/v2/censos/nomes/FERNANDO",
            {"localidade": "4311"},
        )

        self.assertEqual(response, constantes.nome_com_localidade_numeral_invalida)

    @patch("services.ibge.Ibge.busca")
    def teste_busca_ranking_nome_com_localidade_alfabeto(self, mock_busca):
        mock_busca.return_value = constantes.nome_com_localidade_alfabeto

        response = self.ibge.busca_ranking("FERNANDO", localidade="MG")
        mock_busca.assert_called_once_with(
            "https://servicodados.ibge.gov.br/api/v2/censos/nomes/FERNANDO",
            {"localidade": "MG"},
        )

        self.assertEqual(response, constantes.nome_com_localidade_alfabeto)

    @patch("services.ibge.Ibge.busca")
    def teste_busca_ranking_nome_com_sexo_invalido(self, mock_busca):
        mock_busca.return_value = constantes.nome_com_sexo_invalido

        response = self.ibge.busca_ranking("FERNANDO", "X")
        mock_busca.assert_called_once_with(
            "https://servicodados.ibge.gov.br/api/v2/censos/nomes/FERNANDO",
            {"sexo": "X"},
        )

        self.assertEqual(response, constantes.nome_com_sexo_invalido)

    @patch("services.ibge.Ibge.busca")
    def teste_busca_ranking_com_decada(self, mock_busca):
        mock_busca.return_value = constantes.ranking_com_decada

        response = self.ibge.busca_ranking(decada=1950)
        mock_busca.assert_called_once_with(
            "https://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking",
            {"decada": 1950},
        )

        self.assertEqual(response, constantes.ranking_com_decada)

    @patch("services.ibge.Ibge.busca")
    def teste_busca_ranking_com_decada_invalida(self, mock_busca):
        mock_busca.return_value = constantes.ranking_com_decada_invalida

        response = self.ibge.busca_ranking(decada=2030)
        mock_busca.assert_called_once_with(
            "https://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking",
            {"decada": 2030},
        )

        self.assertEqual(response, constantes.ranking_com_decada_invalida)

    @patch("services.ibge.Ibge.busca")
    def teste_busca_localidade(self, mock_busca):
        mock_busca.return_value = constantes.siglas_estados

        response = self.ibge.busca_localidade("RS")
        mock_busca.assert_called_once_with(
            "https://servicodados.ibge.gov.br/api/v1/localidades/estados/RS"
        )

        self.assertEqual(response, constantes.siglas_estados)

    @patch("services.ibge.Cache.busca")
    def teste_busca_cache(self, mock_busca):
        mock_busca.return_value = constantes.ranking_geral

        cache = Mock(Cache)
        cache.busca.return_value = constantes.ranking_geral

        ibge = Ibge(cache=cache)

        self.assertEqual(ibge.busca_cache("key"), mock_busca("key"))

    @patch("services.ibge.Cache.busca")
    def teste_busca_ranking_cache(self, mock_busca):
        mock_busca.return_value = constantes.ranking_geral

        cache = Mock(Cache)
        cache.busca.return_value = constantes.ranking_geral

        ibge = Ibge(cache=cache, cache_ativo=True)

        self.assertEqual(ibge.busca_ranking(), mock_busca(""))

    @patch("services.ibge.Cache.busca")
    def teste_busca_ranking_cache_define(self, mock_busca):
        mock_busca.return_value = constantes.ranking_geral

        cache = Mock(Cache)
        cache.busca.return_value = None

        ibge = Ibge(cache=cache, cache_ativo=True)

        self.assertEqual(ibge.busca_ranking(), constantes.ranking_geral)


if __name__ == "__main__":
    unittest.main()
