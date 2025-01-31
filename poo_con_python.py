class Personaje:

    def __init__(self, nombre, fuerza, inteligencia, vida, defensa):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.vida = vida
        self.defensa = defensa
        self.inventario = {"vida": 0, "fuerza": 0, "inteligencia": 0}  # Inventario de pócimas

    def atributos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Fuerza: {self.fuerza}")
        print(f"Inteligencia: {self.inteligencia}")
        print(f"Vida: {self.vida}")
        print(f"Defensa: {self.defensa}")
        print(f"Inventario: {self.inventario}")
    
    def usar_pocima(self, tipo):
        if self.inventario[tipo] > 0:
            if tipo == "vida":
                self.vida += 20
                print(f"{self.nombre} ha usado una pócima de vida. Nueva vida: {self.vida}")
            elif tipo == "fuerza":
                self.fuerza += self.fuerza * 0.5
                print(f"{self.nombre} ha usado una pócima de fuerza. Nueva fuerza: {self.fuerza}")
            elif tipo == "inteligencia":
                self.inteligencia += self.inteligencia * 0.5
                print(f"{self.nombre} ha usado una pócima de inteligencia. Nueva inteligencia: {self.inteligencia}")
            self.inventario[tipo] -= 1
        else:
            print(f"{self.nombre} no tiene pócimas de {tipo} disponibles.")
    
    def agregar_pocima(self, tipo, cantidad=1):
        if tipo in self.inventario:
            self.inventario[tipo] += cantidad
        else:
            print("Tipo de pócima inválido.")

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
        enemigo.vida = max(0, enemigo.vida - daño)  # Evitar valores negativos
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        print("Vida de ", enemigo.nombre, "es", enemigo.vida)
        
class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, vida, defensa, espada):
        super().__init__(nombre, fuerza, inteligencia, vida, defensa)
        self.espada = espada
        
    def cambiar_arma(self):
        opcion = int(input("Escoge tu arma: (1) Espada de plata, daño 10. (2) Espada de bronce, daño 8"))
        if opcion == 1:
            self.espada = 10
        elif opcion == 2:
            self.espada = 8
        else:
            print("Valor incorrecto")
            
    def atributos(self):
        super().atributos()
        print(f"Espada: {self.espada}")
        
    def dañar(self, enemigo):
        return self.fuerza * self.espada - enemigo.defensa
    
class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, vida, defensa, libro):
        super().__init__(nombre, fuerza, inteligencia, vida, defensa)
        self.libro = libro
        
    def atributos(self):
        super().atributos()
        print(f"Libro: {self.libro}")
        
    def dañar(self, enemigo):
        return self.inteligencia * self.libro - enemigo.defensa
    
pepito = Personaje("Pepito", 20, 15, 10, 100)
hercules = Guerrero("Hércules", 20, 15, 10, 100, 5)
diosito = Mago("Diosito", 20, 15, 10, 100, 5)

pepito.agregar_pocima("vida", 2)
hercules.agregar_pocima("fuerza", 1)
diosito.agregar_pocima("inteligencia", 1)

pepito.atributos()
hercules.atributos()
diosito.atributos()

pepito.usar_pocima("vida")
hercules.usar_pocima("fuerza")
diosito.usar_pocima("inteligencia")

pepito.atributos()
hercules.atributos()
diosito.atributos()

'''
# Función para encontrar al personaje con más vida
def personaje_mas_vida(personajes):
    personaje_con_mas_vida = max(personajes, key=lambda p: p.vida)
    print(f"El personaje con más vida es {personaje_con_mas_vida.nombre} con {personaje_con_mas_vida.vida} puntos de vida.")

# Arreglo de personajes
personajes = [pepito, hercules, diosito]
# Llamar a la función
personaje_mas_vida(personajes)
print(personaje_mas_vida)


# Función para calcular la inteligencia total de los personajes
def inteligencia_total(personajes):
    total = sum(p.inteligencia for p in personajes)
    print(f"La inteligencia total de los personajes es: {total}")
pepito = Personaje("Pepito", 20, 15, 10, 100)
hercules = Guerrero("Hércules", 20, 15, 10, 100, 5)
diosito = Mago("Diosito", 20, 15, 10, 100, 5)
# Arreglo de personajes
personajes = [pepito, hercules, diosito]
# Llamar a la función
inteligencia_total(personajes)
print(inteligencia_total)

#Solo funciona hasta el momento con menos de 10 de vida ya que fue como lo dejamos en la ultima clase
# Función para filtrar personajes por vida
def filtrar_por_vida(personajes, valor_vida):
    personajes_filtrados = [p for p in personajes if p.vida > valor_vida]
    
    if personajes_filtrados:
        print(f"Los personajes con vida mayor a {valor_vida} son:")
        for p in personajes_filtrados:
            print(f"- {p.nombre}: {p.vida} puntos de vida")
    else:
        print(f"No hay personajes con vida mayor a {valor_vida}.")

pepito = Personaje("Pepito", 20, 15, 10, 100)
hercules = Guerrero("Hércules", 20, 15, 10, 100, 5)
diosito = Mago("Diosito", 20, 15, 10, 100, 5)
# Arreglo de personajes
personajes = [pepito, hercules, diosito]
# Pedir al usuario el valor de vida
valor_vida = int(input("Introduce un valor de vida: "))
# Llamar a la función
filtrar_por_vida(personajes, valor_vida)
print(filtrar_por_vida)
'''


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