def define_sexo(sexo=""):
    if sexo:
        sexo = sexo.upper()
        if sexo == "M" or sexo == "F":
            return sexo
        else:
            print(f"Sexo: {sexo} não é válido. \nDigite M (Masculino) ou F (Feminino).")
