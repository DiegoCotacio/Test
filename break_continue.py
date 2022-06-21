def run():
    # se continua cada que encuentre un par hasta mil
    #for contador in range(1000):
     #   if contador % 2 != 0:
      #      continue
       # print(contador)

    # se ejecuta hasta llegar a 5678, lo paramos
    #for i in range(1000):
    #   print(i)
    #   if i == 5678:
    #       break
    
    texto = input('Escribe un texto: ')
    for letra in texto:
        if letra == 'o':
            break
        print(letra)

if __name__ == '__main__':
    run()