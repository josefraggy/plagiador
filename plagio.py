"""
Programa que revisa la probabilidad de que varios archivos de texto sean
parecidos, extrayendo las palabras de cada texto, quitando el relleno
y comparandolas para obtener un porcentaje de coincidencia.

Fuente Palabras:
https://www.ejemplos.co/100-ejemplos-de-conectores/#ixzz5ngoSK5xD

Abrir Varios Archivos:
https://www.quora.com/How-do-I-read-mutiple-txt-files-from-folder-in-python

@author:  Jose Fraggy
@since:   12 de mayo de 2019
@version: 1.1

TODO:
    - Pensar si ordenar las palabras y solo buscar entre alfabeticas.
    - Comparar las palabras entre arreglos y decir cuanto se parecen.
    - El total entre las que existen es el porcentaje de coincidencia.
    - Si hay mas del 50% de coincidencia se muestra el mensaje.
"""

import os.path
from text_fill import relleno

"""
searchWords(nombre_archivo) lee las palabras del txt y regresa:
    - Quita las palabras de relleno.
    - Las hace minusculas.
    - Quita simbolos y acentos.
"""
def searchWords(file):
    # Declaramos las letras y simbolos que se cambian.
    a,b   = 'áéíóúü\n,.;:¿?/()','aeiouu          '
    trans = str.maketrans(a,b)
    # Declaramos el arreglo palabras.
    palabras = []
    # Abrimos el archivo y quitamos palabras que no ocupamos.
    for i in file:
      # Cambiamos las palabras
      i = i.translate(trans)
      # Separamos por espacio.
      i = i.split(" ")
      # Valida si es una referencia
      if i[:1] == ['https']:
          pass
      else:
          for j in range(len(i)):
              i[j] = i[j].lower()
              if i[j] in relleno:
                  pass
              else:
                  palabras.append(i[j])
    return palabras

def main():
    # Arreglos
    files    = {}
    filelist = []

    for filename in os.listdir():
        if os.path.isfile(filename) \
           and filename.endswith(".txt") \
           and not filename in files:
            with open(filename, "r") as file:
                # Abrimos el archivo y quitamos palabras que no ocupamos.
                filelist.append(filename)
                files[filename] = searchWords(file)

    # Estos prints son para recordar como están los arreglos formados
    print('\n')
    print('\n')
    print(filelist[0])
    print('\n')
    print(files[filelist[0]])
    print('\n')
    print('\n')
    print(filelist[1])
    print('\n')
    print(files[filelist[1]])
    print('\n')
    print('\n')
    print(filelist[2])
    print('\n')
    print(files[filelist[2]][0])
    print('\n')
    print('\n')

if __name__ == '__main__':
    main()
