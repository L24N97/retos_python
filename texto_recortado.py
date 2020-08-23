# Programa una función que te devuelva el texto recortado según el número de caracteres indicados, pe. miFuncion("Hola Mundo", 4) devolverá "Hola".

def textoRecortado(texto, fin):
   if not texto:
       return 'No ingresaste una cadena de texto'
   if not fin:
       return 'No ingresaste el final del texto'
   return texto[:fin]


