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
    - El total entre las que existen es el porcentaje de coincidencia.
    - Si hay mas del 50% de coincidencia se muestra el mensaje.
    - Quitar las palabras entre comillas.
    - Proximamente que funcione con pdf, pages y office.
    - Que regrese un reporte en el que subraye las partes de coincidencia.
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

def compare(file1, file2):
    number = 0
    for i in file1:
        if i in file2:
            number = number + 1
        else:
            pass
    print(number)
"""
combinations() compara los arreglos y regresa los porcentajes de error.
"""
def combinations(files, filelist):
    results = []
    c = 0
    # Hacemos las combinaciones.
    for i in filelist:
        for j in range(len(filelist)):
            # Si es la el mismo archivo o el ultimo, no lo cuenta.
            if j + c >= len(filelist) \
            or filelist[j + c] == filelist[c]:
                pass
            else:
                compare(files[filelist[c]], files[filelist[j + c]])
                # print(filelist[c])
                # print(len(files[filelist[c]]))
                # print("-" + filelist[j + c])
                # # Revisar las palabras de filelist[c] con las de filelist[j + c]
                # print(len(files[filelist[j + c]]))

                # files[filelist[2]][k]
        c = c + 1
    return results
"""
main() lee la carpeta y revia los archivos que sean txt.
"""
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
    combinations(files, filelist)
    # Estos prints son para recordar como están los arreglos formados
    # print('\n')
    # print('\n')
    # print(filelist[0])
    # print('\n')
    # print(files[filelist[0]])
    # print('\n')
    # print('\n')
    # print(filelist[1])
    # print('\n')
    # print(files[filelist[1]])
    # print('\n')
    # print('\n')
    # print(filelist[2])
    # print('\n')
    # print(files[filelist[2]][0])
    # print('\n')
    # print('\n')

if __name__ == '__main__':
    main()
