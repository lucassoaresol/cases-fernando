def define_decada(decada=0):
    if decada:
        if isinstance(decada, int):
            if decada < 1930 or decada > 2010 or decada % 10 != 0:
                raise ValueError(f"Década: {decada} não é válida.")
            else:
                return decada
        else:
            raise ValueError(f"Década: {decada} não é válida.")
