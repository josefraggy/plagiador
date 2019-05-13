# Programa que revisa la probabilidad de que varios archivos de texto sean
# parecidos, extrayendo las palabras de cada texto y despues comparando
# obteniendo un porcentaje de coincidencia.
#
# Fuente Palabras:
# https://www.ejemplos.co/100-ejemplos-de-conectores/#ixzz5ngoSK5xD
# Abrir Varios Archivos:
# https://www.quora.com/How-do-I-read-mutiple-txt-files-from-folder-in-python
#
# @author: Jose Fraggy
# @since: 12 de mayo de 2019
# @version: 1.1

# TODO:
# Hacer el codigo modular.
# Pensar si ordenar las palabras y solo buscar entre alfabeticas.
# Comparar las palabras entre arreglos y decir cuanto se parecen.
# El total entre las que existen es el porcentaje de coincidencia.
# Si hay mas del 50% de coincidencia se muestra el mensaje.

import os.path

palabras = []
relleno  = ["ante todo","antes que nada","despues","despues de lo cual",
"en primer lugar","en ultimo lugar","finalmente","luego","para concluir",
"para empezar","para terminar","por otra parte","por otro lado","por ultimo",
"por una parte","por un lado","primero","sobre todo","y asi sucesivamente",
"y demas","a saber","asi","en efecto","en otras palabras","es decir","o sea",
"por ejemplo","a causa de","como","dado que","debido a","gracias a",
"por culpa de","por causa de","porque","pues","puesto que","visto que","ya que",
"pues","ademas","asimismo","de manera anolaga","del mismo modo","igualmente",
"tambien","a menos que","asumiendo que","con la condicion de que",
"con tal de que","en caso de que","si","siempre que","suponiendo que",
"a fin de","con el fin de","con el objetivo","con la intencion de",
"con el objeto de","de manera que","de forma tal que","de modo que","para",
"para que","a consecuencia de","asi","de ahi","en consecuencia","entonces",
"por consiguiente","por esa razon","por ese motivo","por eso","a pesar de",
"al contrario","aunque","de lo contrario","en cambio","en comparacion con",
"mientras que","no obstante","pero","por otro lado","por el contrario",
"sin embargo","sino","a partir de entonces","actualmente","ahora","al final",
"al principio","antes","apenas","cuando","desde","desde entonces",
"desde ese momento","despues","durante","en ese tiempo","en esa epoca",
"en nuestros dias","en otra epoca","enseguida","entonces","hasta","hoy",
"luego","mas tarde","mientras tanto","tan pronto como","una vez que",
"en conclusion","en definitiva","sintetizando","en suma","como se ha mostrado",
"en resumen","en pocas palabras","para sintetizar", "", "que", "quien", "donde",
"cuando", "como", "cual""cuanto", "cuanta", "cuantos", "cuantas", "con", "de",
"hasta", "yo", "tu", "el","nosotros","ustedes","ellos","aquellos","y","a","en",
"la","las","los","su","es","ser","lo","mas","una","o","eso","estos","por","hay"
"sea","se","son","somos","un","muy","menos","sin","si","no","introduccion",
"desarrollo","conclusion","referencia","referencias","del","muchos","pocos",
"sea","su","sus","\u2028","esta","bueno","malo","1","2","3","4","5","6","7",
"8","9","e","t","x"]

# Quitamos acentos y simbolos especiales
a,b   = 'áéíóúü\n,.;:¿?/()','aeiouu          '
trans = str.maketrans(a,b)
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
            for i in file:
              i = i.translate(trans)
              i = i.split(" ")
              if i[:1] == ['https']:
                  pass
              else:
                  for j in range(len(i)):
                      i[j] = i[j].lower()
                      if i[j] in relleno:
                          pass
                      else:
                          palabras.append(i[j])
            # Guardamos las palabras en el arreglo con el nombre del archivo.
            files[filename] = palabras
            palabras        = []

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
