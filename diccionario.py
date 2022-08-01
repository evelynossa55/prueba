def run():
    mi_dicionario={
        "llave1":1,
        "llave2":2,
        "llave3":3,
    }
    # print(mi_dicionario["llave1"])
    # print(mi_dicionario["llave1"])
    # print(mi_dicionario["llave1"])
    poblacion_paises={
        "argentina": 4566788,
        "brasil" :4653466,
        "colombia": 355345,
    }
    # print(poblacion_paises["argentina"])
    # for pais in poblacion_paises.keys():
    #     print(pais)
    # for pais in poblacion_paises.values():
    #     print(pais)
    for pais, poblacion in poblacion_paises.items():
        print(pais+" tiene "+ str(poblacion)+" habitantes") 

if __name__== "__main__":
    run()