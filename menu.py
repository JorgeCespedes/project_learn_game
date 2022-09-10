from leer_preguntas import *

def menu():
    while True:
        try:
            option = int(input(
                    '''
                Escoge una opción:
                    [1] Iniciar juego.
                    [2] Salir.
                    : '''))
            if option == 1:
                print('Iniciar juego.')
                puntos = inicia_juego()
                print_puntos(puntos)

            elif option == 2:
                print('Gracias por su visita.')
                quit()

            elif option != 1 or option != 2:
                print('Ingresa una opción válida...')
                continue

        except ValueError:
            print('Ingresa una opción válida.')
            continue

