class ViajeroFrecuente(): 
    __num_viajero = int 
    __dni = str
    __nombre = str 
    __apellido = str 
    __millas_acum = int 


    def __init__(self,num_viajero=0,dni=0,nombre='',apellido='',millas_acum=0): 

        self.__num_viajero = num_viajero 
        self.__dni= dni 
        self.__nombre = nombre 
        self.__apellido = apellido 
        self.__millas_acum= millas_acum 


    def __eq__ (self, n):
        return self.__millasAcum == n
        
    def __radd__ (self, val):
        return ViajeroFrecuente(self.__num_viajero, self.__dni, self.__nom, self.__apellido, self.__millas_acum + val)
    
    def __rsub__ (self, val):
        return ViajeroFrecuente(self.__numViajero, self.__dni, self.__nom, self.__apellido, self.__millasAcum - val)


    def cantidadTotaldeMillas(self):
        return self.__millas_acum



    def acumularMillas(self,valor_millas): 

        self.__millas_acum+=valor_millas

        return self.__millas_acum 
        
    def canjearMillas(self,valor_millas): 

        if valor_millas <= self.__millas_acum:
            self.__millas_acum -= valor_millas
        else:
            print('Error, cantidad de millas insuficiente')
        return self.__millas_acum


    def getNumero(self):
        return self.__num_viajero


    def getMillas (self):
        return self.__millas_acum
    
    def getNombre(self):
        return self.__nombre
    
    def getApellido(self):
        return self.__apellido