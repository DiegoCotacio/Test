import random

def generar_contrasena():
    mayusculas = ['A', 'B', 'C', 'D','E','F']
    minusculas = ['a', 'b', 'c', 'd','e']
    simbolos = ['!','?','$','#','%']
    numeros = ['1','2','3','4','5','6']

    caracteres = mayusculas + minusculas + simbolos + numeros

    contrasena = []                                 # creo la lista primero
     
    for i in range(15):                             #limite de digitos
      caracter_random = random.choice(caracteres)   #escoger digitos random de la lista unificada
      contrasena.append(caracter_random)            #agregar digito a constr. hasta 15

    contrasena = "".join(contrasena)                ##esto unifica los str en uno solo
    return contrasena                               # le envia a la funcion run el valor de contrasena

def run():
    contrasena = generar_contrasena()
    print('Tu nueva constrasena es: '+ contrasena)


if __name__ == '__main__':
    run()