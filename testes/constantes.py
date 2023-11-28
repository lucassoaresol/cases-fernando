nome_sem_parametros = [
    {
        "nome": "FERNANDO",
        "sexo": None,
        "localidade": "BR",
        "res": [
            {"periodo": "1930[", "frequencia": 2204},
            {"periodo": "[1930,1940[", "frequencia": 6962},
            {"periodo": "[1940,1950[", "frequencia": 15234},
            {"periodo": "[1950,1960[", "frequencia": 35366},
            {"periodo": "[1960,1970[", "frequencia": 58110},
            {"periodo": "[1970,1980[", "frequencia": 88046},
            {"periodo": "[1980,1990[", "frequencia": 169079},
            {"periodo": "[1990,2000[", "frequencia": 119794},
            {"periodo": "[2000,2010[", "frequencia": 61551},
        ],
    }
]


nome_invalido = []

nome_com_localidade = [
    {
        "nome": "FERNANDO",
        "sexo": None,
        "localidade": "43",
        "res": [
            {"periodo": "1930[", "frequencia": 144},
            {"periodo": "[1930,1940[", "frequencia": 413},
            {"periodo": "[1940,1950[", "frequencia": 788},
            {"periodo": "[1950,1960[", "frequencia": 1899},
            {"periodo": "[1960,1970[", "frequencia": 3383},
            {"periodo": "[1970,1980[", "frequencia": 4374},
            {"periodo": "[1980,1990[", "frequencia": 10193},
            {"periodo": "[1990,2000[", "frequencia": 6578},
            {"periodo": "[2000,2010[", "frequencia": 3507},
        ],
    }
]

nome_com_sexo = [
    {
        "nome": "FERNANDO",
        "sexo": "M",
        "localidade": "BR",
        "res": [
            {"periodo": "1930[", "frequencia": 2194},
            {"periodo": "[1930,1940[", "frequencia": 6937},
            {"periodo": "[1940,1950[", "frequencia": 15186},
            {"periodo": "[1950,1960[", "frequencia": 35261},
            {"periodo": "[1960,1970[", "frequencia": 57922},
            {"periodo": "[1970,1980[", "frequencia": 87601},
            {"periodo": "[1980,1990[", "frequencia": 167744},
            {"periodo": "[1990,2000[", "frequencia": 118365},
            {"periodo": "[2000,2010[", "frequencia": 60566},
        ],
    }
]

nome_com_localidade_sexo = [
    {
        "nome": "FERNANDO",
        "sexo": "M",
        "localidade": "43",
        "res": [
            {"periodo": "1930[", "frequencia": 144},
            {"periodo": "[1930,1940[", "frequencia": 413},
            {"periodo": "[1940,1950[", "frequencia": 787},
            {"periodo": "[1950,1960[", "frequencia": 1896},
            {"periodo": "[1960,1970[", "frequencia": 3372},
            {"periodo": "[1970,1980[", "frequencia": 4355},
            {"periodo": "[1980,1990[", "frequencia": 10118},
            {"periodo": "[1990,2000[", "frequencia": 6510},
            {"periodo": "[2000,2010[", "frequencia": 3456},
        ],
    }
]

nome_com_localidade_numeral_invalida = []

nome_com_localidade_alfabeto = nome_sem_parametros

nome_com_sexo_invalido = nome_sem_parametros

siglas_estados = {
    "id": 43,
    "sigla": "RS",
    "nome": "Rio Grande do Sul",
    "regiao": {"id": 4, "sigla": "S", "nome": "Sul"},
}


ranking_geral = [
    {
        "localidade": "BR",
        "sexo": None,
        "res": [
            {"nome": "MARIA", "frequencia": 11734129, "ranking": 1},
            {"nome": "JOSE", "frequencia": 5754529, "ranking": 2},
            {"nome": "ANA", "frequencia": 3089858, "ranking": 3},
            {"nome": "JOAO", "frequencia": 2984119, "ranking": 4},
            {"nome": "ANTONIO", "frequencia": 2576348, "ranking": 5},
            {"nome": "FRANCISCO", "frequencia": 1772197, "ranking": 6},
            {"nome": "CARLOS", "frequencia": 1489191, "ranking": 7},
            {"nome": "PAULO", "frequencia": 1423262, "ranking": 8},
            {"nome": "PEDRO", "frequencia": 1219605, "ranking": 9},
            {"nome": "LUCAS", "frequencia": 1127310, "ranking": 10},
            {"nome": "LUIZ", "frequencia": 1107792, "ranking": 11},
            {"nome": "MARCOS", "frequencia": 1106165, "ranking": 12},
            {"nome": "LUIS", "frequencia": 935905, "ranking": 13},
            {"nome": "GABRIEL", "frequencia": 932449, "ranking": 14},
            {"nome": "RAFAEL", "frequencia": 821638, "ranking": 15},
            {"nome": "FRANCISCA", "frequencia": 725642, "ranking": 16},
            {"nome": "DANIEL", "frequencia": 711338, "ranking": 17},
            {"nome": "MARCELO", "frequencia": 693215, "ranking": 18},
            {"nome": "BRUNO", "frequencia": 668217, "ranking": 19},
            {"nome": "EDUARDO", "frequencia": 632664, "ranking": 20},
        ],
    }
]

ranking_com_decada = [
    {
        "localidade": "BR",
        "sexo": None,
        "res": [
            {"nome": "MARIA", "frequencia": 1487042, "ranking": 1},
            {"nome": "JOSE", "frequencia": 648754, "ranking": 2},
            {"nome": "ANTONIO", "frequencia": 314375, "ranking": 3},
            {"nome": "JOAO", "frequencia": 256001, "ranking": 4},
            {"nome": "FRANCISCO", "frequencia": 160721, "ranking": 5},
            {"nome": "ANA", "frequencia": 101259, "ranking": 6},
            {"nome": "MANOEL", "frequencia": 95014, "ranking": 7},
            {"nome": "FRANCISCA", "frequencia": 91799, "ranking": 8},
            {"nome": "PEDRO", "frequencia": 86926, "ranking": 9},
            {"nome": "SEBASTIAO", "frequencia": 84668, "ranking": 10},
            {"nome": "RAIMUNDO", "frequencia": 80134, "ranking": 11},
            {"nome": "LUIZ", "frequencia": 74213, "ranking": 12},
            {"nome": "ANTONIA", "frequencia": 72229, "ranking": 13},
            {"nome": "TEREZINHA", "frequencia": 65194, "ranking": 14},
            {"nome": "JOSEFA", "frequencia": 61101, "ranking": 15},
            {"nome": "PAULO", "frequencia": 60073, "ranking": 16},
            {"nome": "GERALDO", "frequencia": 56005, "ranking": 17},
            {"nome": "CARLOS", "frequencia": 53410, "ranking": 18},
            {"nome": "RAIMUNDA", "frequencia": 50089, "ranking": 19},
            {"nome": "LUIS", "frequencia": 48056, "ranking": 20},
        ],
    }
]

ranking_com_decada_invalida = []
