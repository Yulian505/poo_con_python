class Personaje:

    def __init__(self, nombre, fuerza, inteligencia, vida, defensa):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.vida = vida
        self.defensa = defensa
        
    def atributos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Fuerza: {self.fuerza}")
        print(f"Inteligencia: {self.inteligencia}")
        print(f"Vida: {self.vida}")
        print(f"Defensa: {self.defensa}")
        
    def Nivel(self, fuerza, inteligencia, vida, defensa):
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.vida += vida
        self.defensa += defensa
    
    def esta_vivo(self):
        return self.vida > 0
    
    def esta_muerto(self):
        self.vida = 0
        print(f"Tu personaje {self.nombre} ha muerto")
        
    def dañar(self, enemigo):
        return self.fuerza - enemigo.defensa
    
    def atacar(self, enemigo):
        daño = self.dañar(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        print("Vida de ", enemigo.nombre, "es", enemigo.vida)
        
#Creando clase guerrero que hereda de su clase padre "Personaje"
class Guerrero(Personaje):
    #Sobreescribir el constructor de la clase padre
    def __init__(self, nombre, fuerza, inteligencia, vida, defensa, espada):
        #Personaje.__init__(self, nombre, fuerza, inteligencia, vida, defensa)
        #Llamar al constructor de la clase padre
        super().__init__(nombre, fuerza, inteligencia, vida, defensa)
        self.espada = espada

hercules = Guerrero("Hércules", 80, 50, 100, 100, 5)
hercules.atributos()
print(hercules.espada)


'''
#Variable del constructor  de la clase
mi_personaje = Personaje("Pipito", 70, 90, 50, 100)
mi_enemigo = Personaje("Enemigo", 60, 90, 40, 100)
print(mi_personaje.dañar(mi_enemigo))
#print(mi_personaje.esta_vivo())
mi_personaje.atributos()
mi_personaje.atacar(mi_enemigo)
mi_enemigo.atributos()
'''