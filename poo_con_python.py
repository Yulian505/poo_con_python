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
        
    #Pedirle al usuario escoger un arma
    def cambiar_arma(self):
        opcion = int(input("Escoge tu arma: (1) Esapada de plata, daño 10. (2) Espada de bronce, daño 8"))
        if opcion == 1:
            self.espada = 10
        elif opcion == 2:
            self.espada = 8
        else:
            print("Valor incorrecto")
            
    #Sobrescribir método       
    def atributos(self):
        super().atributos()
        print(f"Espada: {self.espada}")
        
    #Sobrescribir el cálculo de daño
    def dañar(self, enemigo):
        return self.fuerza * self.espada - enemigo.defensa
    
class Mago(Personaje):
    #Sobreescribir el constructor de la clase padre
    def __init__(self, nombre, fuerza, inteligencia, vida, defensa, libro):
        #Personaje.__init__(self, nombre, fuerza, inteligencia, vida, defensa)
        #Llamar al constructor de la clase padre
        super().__init__(nombre, fuerza, inteligencia, vida, defensa)
        self.libro = libro
        
    #Sobrescribir método       
    def atributos(self):
        super().atributos()
        print(f"Libro: {self.libro}")
        
    #Sobrescribir el cálculo de daño
    def dañar(self, enemigo):
        return self.inteligencia * self.libro - enemigo.defensa
    
pepito = Personaje("Pepito", 20, 15, 10, 100)
hercules = Guerrero("Hércules", 20, 15, 10, 100, 5)
diosito = Mago("Diosito", 20, 15, 10, 100, 5)
#Imprimir atributos antes del ataque
pepito.atributos()
hercules.atributos()
diosito.atributos()
#Ataques
pepito.atacar(hercules)
hercules.atacar(diosito)
diosito.atacar(pepito)
#Imprimir despues del ataque
pepito.atributos()
hercules.atributos()
diosito.atributos()

#print(hercules.espada)


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