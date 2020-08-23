# 1) Programa una función que cuente el número de caracteres de una cadena de texto, pe. miFuncion("Hola Mundo") devolverá 10.

def contarCaracter(string):
    if not string:
        return 'Debes ingresar una cadena de texto'
    return len(string)
