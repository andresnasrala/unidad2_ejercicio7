from menu import Menu
import os

if __name__ == '__main__':

    listaViajero = []

    Menu = Menu()
    manager = Menu.mostrarMenu()

    bandera = False

    while not bandera:

        Menu.mostrarMenu()
        op = int(input('Su opcion: '))
        Menu.opcion (op, listaViajero)
        os.system('pause')

        if op == 0:
            bandera = True

    print ('saliendo...')
    os.system('pause')
    os.system('exit')