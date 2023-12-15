from services.cache import Cache
from unittest.mock import patch
import redis
import unittest


class TestRedis(unittest.TestCase):
    @patch("services.cache.redis.Redis")
    def teste_except_connection_error(self, mock_redis):
        mock_redis.side_effect = redis.ConnectionError()
        Cache()

    @patch("services.cache.redis.Redis.get")
    def teste_busca(self, mock_redis):
        cache = Cache()
        mock_redis.return_value = b'"value"'
        value = cache.busca("key")
        self.assertEqual(value, "value")

    @patch("services.cache.redis.Redis.get")
    def teste_busca_none(self, mock_redis):
        cache = Cache()
        mock_redis.return_value = None
        value = cache.busca("key")
        self.assertIsNone(value)

    @patch("services.cache.redis.Redis.get")
    def teste_busca_except(self, mock_redis):
        cache = Cache()
        mock_redis.side_effect = redis.RedisError()
        value = cache.busca("key")
        self.assertIsNone(value)

    @patch("services.cache.redis.Redis.setex")
    def teste_define(self, mock_redis):
        cache = Cache()
        value = cache.define("key", "value")
        self.assertTupleEqual(value, ("key", '"value"'))

    @patch("services.cache.redis.Redis.setex")
    def teste_define_except(self, mock_redis):
        cache = Cache()
        mock_redis.side_effect = redis.RedisError()
        cache.define("key", "value")

    @patch("services.cache.redis.Redis.ping")
    def teste_verificar_conexao(self, mock_redis):
        cache = Cache()
        mock_redis.return_value = True
        self.assertTrue(cache.verificar_conexao())

    @patch("services.cache.redis.Redis.ping")
    def teste_verificar_conexao_except(self, mock_redis):
        cache = Cache()
        mock_redis.return_value = False
        mock_redis.side_effect = redis.ConnectionError()
        self.assertFalse(cache.verificar_conexao())


if __name__ == "__main__":
    unittest.main()
