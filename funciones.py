#def imprimir_mensaje():
 #   print('mensaje especial: ')
  #  print('estoy aprendiendo a usar funciones')
    
#imprimir_mensaje

def conversacion(mensaje):
    print('hola')
    print('Como estas')
    print(mensaje)
    print('Adios')    

opcion = input('elige una opcion (1, 2, 3): ')
if opcion == '1':
    conversacion('Elegiste la opcion 1')
elif opcion == '2':
    conversacion('Elegiste la opcion 2')
elif opcion == '3':
    conversacion('Elegiste la opcion 3')
else:
    print('escribi bien maricon')