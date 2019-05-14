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
@version: 2.0

TODO:
    - Quitar las palabras entre comillas.
    - Proximamente que funcione con pdf, pages y office.
    - Que regrese un reporte en el que subraye las partes de coincidencia.
"""

import os.path
from text_fill import relleno

"""
searchWords(nombre_archivo) Lee las palabras del txt y regresa:
    - Quita las palabras de relleno.
    - Las hace minusculas.
    - Quita simbolos y acentos.
    - Validar para archivos vacios.
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

"""
compare(file1, file2) Compara las palabras entre textos:
    - Regresa el porcentaje de coincidencias con 2 decimales.
"""
def compare(file1, file2):
    number = 0
    current = 0
    last = 0

    for i in file1:
        for j in file2:
            # Revisamos la distancia de coincidencia
            if i == j and (current - last) < 5:
                number = number + 1
                # Borras el elemento encontrado
                file2.remove(i)
                last = current
            else:
                pass
        current = current + 1
    # Validamos si el archivo esta vacio.
    if len(file1) == 0:
        percentage = 0
    else:
        percentage = round((number * 100) / len(file1))
    return percentage

"""
combinations(files, filelist) Compara los arreglos.
    - Regresa los porcentajes de error.
"""
def combinations(files, filelist):
    results = 0
    c = 0
    # Hacemos las combinaciones.
    for i in filelist:
        for j in range(len(filelist)):
            # Si es la el mismo archivo o el ultimo, no lo cuenta.
            if j + c >= len(filelist) \
            or filelist[j + c] == filelist[c]:
                pass
            else:
                results = compare(files[filelist[c]], files[filelist[j + c]])

                print(str(results).zfill(2) + "% de Probabilidad de Plagio entre: " +
                      str(filelist[c]) + " y " + str(filelist[j + c]) + "\n")
        c = c + 1

"""
main()
    - Lee la carpeta y revia los archivos que sean txt.
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

if __name__ == '__main__':
    main()
