import redis
import json


class Redis:
    def __init__(self, host="localhost", port=6379, db=0):
        try:
            self.redis = redis.Redis(host=host, port=port, db=db)
        except redis.ConnectionError:
            print(f"Não foi possível conectar ao servidor Redis em {host}:{port}")

    def busca(self, key):
        try:
            value = self.redis.get(key)
            if value:
                value = value.decode("utf-8")
                return json.loads(value)
            else:
                return None
        except redis.RedisError as e:
            print(f"Erro ao obter valor da chave {key} no Redis: {e}")

    def define(self, key, value, expiration=600):
        try:
            value = json.dumps(value)
            self.redis.setex(key, expiration, value)
            return key, value
        except (redis.RedisError, TypeError) as e:
            print(f"Erro ao definir chave {key} no Redis: {e}")

    def verificar_conexao(self):
        try:
            return self.redis.ping()
        except (redis.exceptions.ConnectionError, ConnectionRefusedError):
            return False
