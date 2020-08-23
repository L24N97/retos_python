# Programa una función que dada una String te devuelva un Array de textos separados por cierto caracter, pe. miFuncion('hola que tal', ' ') devolverá ['hola', 'que', 'tal'].

def cambiarArray(texto, caracter):
    return texto.split(caracter)

print(cambiarArray('hola que tal', ' '))
