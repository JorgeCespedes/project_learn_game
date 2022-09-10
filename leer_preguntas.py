from preguntas import *
preguntas = preguntas(lista_preguntas)
alternativas = alternativas(lista_preguntas)
respuestas = respuestas(lista_preguntas)


def inicia_juego():
    puntos = 0
    numero_pregunta = 0
    while numero_pregunta < len(preguntas):
        print()
        print('Pregunta: ', preguntas[numero_pregunta])
        for al in alternativas[numero_pregunta]:
            print('   ', alternativas[numero_pregunta].index(al) + 1,':' , al)


        opcion_usuario = valida_opcion_usuario()
        if alternativas[numero_pregunta][int(opcion_usuario) - 1] == respuestas[numero_pregunta]:
            puntos += 1

        print('-' * 50)

        numero_pregunta += 1
    return puntos



def print_puntos(puntos):
    print()
    print('*'*20)
    print('Lograste: ', puntos , 'puntos.')
    print('Porcentaje: ', puntos/len(preguntas) , '%')
    print('*'*20)
    print()
    print('Gracias por jugar.')
    quit()


def valida_opcion_usuario():
    correcto = False
    opcion_usuario = 0
    while not correcto:
        try:
            opcion_usuario = int(input('    Selecciona la opción 1 ó 2: '))
            if opcion_usuario == 1 or opcion_usuario == 2:
                correcto = True
            else:
                print('    Ingresa un número válido.')
        except ValueError:
            print('    Error, introduce un numero entero')
     
    return opcion_usuario
