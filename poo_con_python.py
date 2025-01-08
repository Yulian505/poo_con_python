class Personaje:
    #Atributos de la clase
    nombre = 'Default'
    fuerza = 0
    inteligencia = 0
    vida = 0
    defensa = 0
    
#Variable del constructor
mi_personaje = Personaje()
mi_personaje.nombre = "Makai"
mi_personaje.fuerza = 10
print("El nombre del personaje es: ", mi_personaje.nombre)
print("La fuerza del personaje es: ", mi_personaje.fuerza)