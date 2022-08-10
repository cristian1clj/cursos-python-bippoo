# Una funcion es un grupo de instrucciones (bloque de codigo) que recibe 0 o mas argunentos de entrada.
# Se definen con la palabra clave "def".
#
# Estructura =>        def nombre_funcion(parametros):
#                           codigo...

def imprimir_HW():
    frase = "Hello world"
    print (frase)

    juntar_frases(frase)

def juntar_frases(frase1):
    frase2 = " or algo que no se que poner"
    print (frase1 + frase2)

imprimir_HW()