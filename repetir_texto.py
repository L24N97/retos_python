# Programa una función que repita un texto X veces, pe. miFuncion('Hola Mundo', 3) devolverá Hola Mundo Hola Mundo Hola Mundo.

def repetirTexto(texto, veces):
    if not texto:
        return 'Debes ingresar la frase a repetir'
    if not veces:
        return 'Debes ingresar el numero de veces a repetir'
    if veces == 0:
        return 'El numero a repetir no puede ser 0'
    if veces < 0:
        return 'El numero a repetir no puede ser negativo'
    return texto * veces

