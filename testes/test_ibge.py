from services.ibge import Ibge
from unittest.mock import patch, Mock
import unittest


class TestIbge(unittest.TestCase):
    @patch("services.ibge.Session.get")
    def teste_buscar_ranking_sem_parametros(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = [{"Any": "any"}]
        mock_get.return_value = mock_response

        resultado = Ibge().busca_ranking()

        mock_get.assert_called_once_with(
            "https://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking",
            params=None,
            timeout=5,
        )
        self.assertEqual(resultado, [{"Any": "any"}])

    @patch("services.ibge.Session.get")
    def teste_buscar_ranking_com_parametro_sem_nome(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = [{"localidade": "MG", "sexo": "M"}]
        mock_get.return_value = mock_response

        resultado = Ibge().busca_ranking(localidade="MG", sexo="M")

        mock_get.assert_called_once_with(
            "https://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking",
            params={"localidade": "MG", "sexo": "M"},
            timeout=5,
        )
        self.assertEqual(resultado, [{"localidade": "MG", "sexo": "M"}])

    @patch("services.ibge.Session.get")
    def teste_buscar_localidade(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {"sigla": "SP", "nome": "São Paulo"}
        mock_get.return_value = mock_response

        resultado = Ibge().busca_localidade("SP")

        mock_get.assert_called_once_with(
            "https://servicodados.ibge.gov.br/api/v1/localidades/estados/SP",
            timeout=5,
        )
        self.assertEqual(resultado, {"sigla": "SP", "nome": "São Paulo"})


if __name__ == "__main__":
    unittest.main()
