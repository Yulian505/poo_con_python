class Personaje:

    def __init__(self, nombre, fuerza, inteligencia, vida, defensa):
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.inteligencia = inteligencia
        self.__vida = vida
        self.__defensa = defensa
        
    def atributos(self):
        print(f"Nombre: {self.__nombre}")
        print(f"Fuerza: {self.__fuerza}")
        print(f"Inteligencia: {self.inteligencia}")
        print(f"Vida: {self.__vida}")
        print(f"Defensa: {self.__defensa}")
        
    def Nivel(self, fuerza, inteligencia, vida, defensa):
        self.__fuerza += fuerza
        self.inteligencia += inteligencia
        self.__vida += vida
        self.__defensa += defensa
    
    def esta_vivo(self):
        return self.__vida > 0
    
    def __morir(self):
        self.__vida = 0
        print(f"Tu personaje {self.__nombre} ha muerto")
        
    def dañar(self, enemigo):
        return self.__fuerza - enemigo.__defensa if self.__fuerza > enemigo.__defensa else 0
    
    def atacar(self, enemigo):
        daño = self.dañar(enemigo)
        enemigo.__vida = enemigo.__vida - daño
        print(self.__nombre, "ha realizado", daño, "puntos de daño a", enemigo.__nombre)
        if not enemigo.esta_vivo():
            enemigo.__morir()
        print("Vida de ", enemigo.__nombre, "es", enemigo.__vida)
        
    def get_fuerza(self):
        return self.__fuerza
    
    def set_fuerza(self, fuerza):
        if fuerza < 0:
            print("ERROR, VALOR NEGATIVO")
        else:
            self.__fuerza = fuerza
        self.__fuerza = fuerza
#Variable del constructor  de la clase
mi_personaje = Personaje("Pipito", 8000, 90, 50, 100)
mi_enemigo = Personaje("Enemigo", 60, 90, 40, 100)
print(mi_personaje.dañar(mi_enemigo))
#Prueba 1. Sin acceso al atributo fuerza
#Prueba 4. ¿Podra morir?
'''
print(mi_personaje.get_fuerza())
mi_personaje.set_fuerza(-100)
print(mi_personaje.get_fuerza())
''' 
#print(mi_personaje.esta_vivo())
'''
mi_personaje.atributos()
mi_personaje.atacar(mi_enemigo)
mi_enemigo.atributos()
'''
mi_personaje._Personaje__fuerza = 10
mi_personaje.atributos()