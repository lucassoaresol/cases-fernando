import redis
from redis.exceptions import RedisError
from services.redis import Redis
from unittest.mock import patch
import unittest


class TestRedis(unittest.TestCase):
    @patch("redis.Redis")
    def teste_init(self, mock_redis):
        cache = Redis()
        mock_redis.assert_called_once()

    @patch("Redis.logging.error")
    @patch("redis.Redis")
    def teste_init_connection_error(self, mock_redis, mock_logging_error):
        mock_redis.side_effect = redis.ConnectionError("Connection Error")
        with self.assertRaises(redis.ConnectionError):
            Redis()
        mock_logging_error.assert_called_once_with(
            "Não foi possível conectar ao servidor Redis em localhost:6379"
        )

    @patch("redis.Redis")
    def teste_init_exception(self, mock_redis):
        mock_redis.side_effect = RedisError("Connection Error")
        with self.assertRaises(RedisError):
            Redis()

    @patch("redis.Redis")
    def teste_busca_key_exists(self, mock_redis):
        cache = Redis()
        cache.redis.busca.return_value = b'"value"'
        value = cache.busca("key")
        self.assertEqual(value, "value")

    @patch("redis.Redis")
    def teste_busca_key_not_exists(self, mock_redis):
        cache = Redis()
        cache.redis.busca.return_value = None
        value = cache.busca("key")
        self.assertIsNone(value)

    @patch("redis.Redis")
    def teste_busca_exception(self, mock_redis):
        cache = Redis()
        cache.redis.busca.side_effect = RedisError("Error getting key")
        value = cache.busca("key")
        self.assertIsNone(value)

    @patch("redis.Redis")
    def teste_define(self, mock_redis):
        cache = Redis()
        cache.define("key", "value")
        cache.redis.setex.assert_called_once()

    @patch("redis.Redis")
    def teste_define_exception(self, mock_redis):
        cache = Redis()
        cache.redis.setex.side_effect = RedisError("Error setting key")
        cache.define("key", "value")

    @patch("redis.Redis")
    def teste_verificar_conexao_success(self, mock_redis):
        cache = Redis()
        cache.redis.ping.return_value = True
        self.assertTrue(cache.verificar_conexao())

    @patch("redis.Redis")
    def teste_verificar_conexao_failure(self, mock_redis):
        cache = Redis()
        cache.redis.ping.return_value = False
        self.assertFalse(cache.verificar_conexao())


if __name__ == "__main__":
    unittest.main()
