from redis.exceptions import ConnectionError, RedisError
from services.redis import Redis
from unittest.mock import patch
import redis
import unittest


class TestRedis(unittest.TestCase):
    @patch("redis.Redis")
    def teste_connection_error(self, mock_redis):
        mock_redis.side_effect = redis.ConnectionError()
        with self.assertRaises(ConnectionError):
            redis.Redis()

    @patch("services.redis.Redis.busca")
    def teste_busca_key_exists(self, mock_redis):
        cache = Redis()
        mock_redis.return_value = "value"
        value = cache.busca("key")
        self.assertEqual(value, "value")

    @patch("services.redis.Redis.busca")
    def teste_busca_key_not_exists(self, mock_redis):
        cache = Redis()
        mock_redis.return_value = None
        value = cache.busca("key")
        self.assertIsNone(value)

    @patch("services.redis.Redis.busca")
    def teste_busca_key_not_exists_except(self, mock_redis):
        cache = Redis()
        mock_redis.side_effect = redis.RedisError()
        with self.assertRaises(RedisError):
            cache.busca("key")

    @patch("services.redis.Redis.define")
    def teste_define(self, mock_redis):
        cache = Redis()
        mock_redis.return_value = "key", "value"
        value = cache.define("key", "value")
        self.assertTupleEqual(value, ("key", "value"))

    @patch("services.redis.Redis.define")
    def teste_define_err(self, mock_redis):
        cache = Redis()
        mock_redis.return_value = None
        value = cache.define("key", "value")
        self.assertIsNone(value)

    @patch("services.redis.Redis.define")
    def teste_define_except(self, mock_redis):
        cache = Redis()
        mock_redis.side_effect = redis.RedisError()
        with self.assertRaises(RedisError):
            cache.define("key", "value")

    @patch("services.redis.Redis.verificar_conexao")
    def teste_verificar_conexao_success(self, mock_redis):
        cache = Redis()
        mock_redis.return_value = True
        self.assertTrue(cache.verificar_conexao())

    @patch("services.redis.Redis.verificar_conexao")
    def teste_verificar_conexao_failure(self, mock_redis):
        cache = Redis()
        mock_redis.return_value = False
        self.assertFalse(cache.verificar_conexao())


if __name__ == "__main__":
    unittest.main()
