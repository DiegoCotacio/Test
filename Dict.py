def run():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }
    print(mi_diccionario['llave1'])

    poblacion_paises = {
        'Argentina': 44.9,
        'Brasil': 210,
        'Colombia': 50
    }
    # print(poblacion_paises['Colombia'])
    # for pais in poblacion_paises.keys():  --- esto para ver llaves
    #    print(pais)
    #for pais in poblacion_paises.values(): --- para ver valores
    #  print(pais)
    for pais, poblacion in poblacion_paises.items():
        print(pais + ' tiene ' + str(poblacion) + ' habitantes')




if __name__ == '__main__':
    run()