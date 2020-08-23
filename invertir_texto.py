# Programa una función que invierta las palabras de una cadena de texto, pe. miFuncion("Hola Mundo") devolverá "odnuM aloH".

def invertirTexto(texto):
    if not texto:
        return 'Debes ingresar una cadena de texto'
    return texto[::-1]
