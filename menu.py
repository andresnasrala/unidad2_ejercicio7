import os
import csv
from claseViajeroFrecuente import ViajeroFrecuente as viajero_frecuente

class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 1: self.opc1,
                            2: self.opc2,
                            3: self.opc3,
                            4: self.opc4,
                            0: self.salir
                        }
        
    def opcion(self,op, ListaViajeros):   
        func=self.__switcher.get(op, lambda: print("Opción no válida, intente de nuevo"))
        if op ==1 or op==2 or op==3 or op==4:
            func(ListaViajeros)
        else:
            func()

    def mostrarMenu(self, LV=None):
        os.system('cls')
        print ('''
    -------->Menu<--------
    Seleccione una opcion:
    1. Realizar carga
    2. Determinar el/los viajero/s con mayor cantidad de millas acumuladas (inciso 1)
    3. Acumular millas (inciso 2)
    4. Canjear millas (inciso 3)
    0. Salir
''')
   
    def buscarViajero (self, n, LV):
        indice=0
        valorDeRetorno = None
        bandera=False
        while not bandera and indice < len(LV):
            if LV[indice].getNumero()==n:
                bandera=True
                valorDeRetorno=indice
            else: indice+=1
        if valorDeRetorno == None:
            print ('Error, Numero no encontrado')
        return valorDeRetorno

    def comparaPorIzq (self, LV): 
        os.system('cls')
        print ('-------->igual por Izquierda<--------')
        x = int (input ('Ingrese cantidad de millas a comparar: '))
        if LV[0] == x:
            print ('Son Iguales')
        else: print ('Son distintos')
    
    def comparaPorDer (self, LV):
        print ('-------->igual por Derecha<--------')
        x = int (input ('Ingrese cantidad de millas a comparar: '))
        if x == LV[0]:
            print ('Son Iguales')
        else: print ('Son distintos')
        
    def opc1 (self, LV):
        total = 0
        bandera = True
        path = './archivo_Viajeros.csv'
        archivo = open(path, 'r')
        reader = csv.reader(archivo, delimiter =',')


        for fila in reader:
            if bandera:
                bandera = False
            else:
                num_viajero = int (fila[0])
                dni = fila[1]
                nombre = fila[2]
                apellido = fila[3]
                millas = int (fila[4])
                viajero = viajero_frecuente(num_viajero, dni, nombre, apellido, millas)
                LV.append(viajero)
                total += 1
        if total > 0:
            print (f'Lista cargada correctamente, se cargaron {total} viajeros')
        else:
            print ('Error en la carga')



    def opc2 (self, LV):
        os.system('cls')
        ind = self.buscarMayor (LV)
        print (f'el viajero con mayor millas acumuladas es: {LV[ind].getNombre()} {LV[ind].getApellido()}, Numero: {LV[ind].getNumero()}')
        

    def opc3 (self, LV):
        os.system('cls')
        r = int (input ('Ingrese numero de viajero: '))
        i = self.buscarViajero(r, LV)
        x = int (input ('Ingrese millas a acumular: '))
        LV[i] += x
        print (f'Cantidad de millas actuales: {LV[i].getMillas()}')

    def opc4 (self, LV):
        os.system('cls')
        r = int (input ('Ingrese numero de viajero: '))
        i = self.buscarViajero(r, LV)
        x = int (input ('Ingrese millas a canjear: '))
        LV[i] = LV[i] - x
        print (f'Cantidad de millas actuales: {LV[i].getMillas()}')

    def salir (self):
        print ('saliendo...')