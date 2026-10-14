import numpy as np
import random

# Función de tablero
def crear_tablero(lado = 10):
    tablero = np.full((lado,lado),"~")
    return tablero

#Función de colocar los barcos en el tablero
barco_1 = [(0,1),(1,1)]
barco_2 = []
def colocar_barco(tablero, barco):
    for pieza in barco:
        tablero[pieza] = "O"
    return tablero

# Función para disparar
def recibir_disparo(tablero, coordenada):        
        if tablero[coordenada] == "O":
            tablero[coordenada] = "X"
            print("Le diste al barco")
            return "Acertaste"
        elif tablero[coordenada] == "~":
            tablero[coordenada] = "_"
            print("Le diste al agua")
            return "Agua"
        elif tablero[coordenada] == "X" or tablero[coordenada] == "_":
            print("Ya has disparado en ese lugar, vuelve a intentarlo")
            return "Disparo invalido"

# Función de barco aleatorio
def crea_barco_aleatorio(tablero, largo = 4, num_intentos = 100):
    num_max_filas = tablero.shape[0]
    num_max_columnas = tablero.shape[1]
    intentos = 0
    while intentos < num_intentos:
        barco = []
        intentos += 1
        pieza_original = (random.randint(0,num_max_filas-1),random.randint(0, num_max_columnas -1))
        print("Pieza original:", pieza_original)
        barco.append(pieza_original)
        orientacion = random.choice(["N","S","O","E"])
        print("Con orientacion", orientacion)
        fila = pieza_original[0]
        columna = pieza_original[1]
        for i in range(largo -1):
            if orientacion == "N":
                fila -= 1
            elif orientacion  == "S":
                fila += 1
            elif orientacion == "E":
                columna += 1
            else:
                columna -= 1
            pieza = (fila,columna)
            barco.append(pieza)
        tablero_temp = coloca_solo(tablero, barco)
        if type(tablero_temp) == np.ndarray:
            return tablero_temp
        print("Tengo que intentar colocar otro barco")
    return False

#Función de colocar barco solo
def coloca_solo(tablero, barco):
    tablero_temp = tablero.copy()
    num_max_filas = tablero.shape[0]
    num_max_columnas = tablero.shape[1]
    for pieza in barco:
        fila = pieza[0]
        columna = pieza[1]
        if fila < 0  or fila >= num_max_filas:
            print(f"No puedo poner la pieza {pieza} porque se sale del tablero")
            return False
        if columna <0 or columna>= num_max_columnas:
            print(f"No puedo poner la pieza {pieza} porque se sale del tablero")
            return False
        if tablero[pieza] == "O" or tablero[pieza] == "X":
            print(f"No puedo poner la pieza {pieza} porque hay otro barco")
            return False
        tablero_temp[pieza] = "O"
    return tablero_temp
    

#Flota
def flota(tablero):
    flota_largo = [2, 2, 2, 3, 3, 4]
    
    for largo in flota_largo:
        tablero_flota = crea_barco_aleatorio(tablero, largo, num_intentos = 100)

        if type(tablero_flota) == np.ndarray:
            tablero =  tablero_flota
        else:
            return False
    return tablero



"""
Hay dos tableros por jugador: 
- tablero_barcos
- tablero_disparo
- ejemplo: (jugador 1 dispara) jugador2.tablero_barcos --> hay o no barco --> se refleja en jugador1.tablero_disparo
"""

class Jugador:
    def __init__(self, nombre, tablero_barcos, tablero_disparo):
        self.nombre = nombre
        self.tablero_barcos = tablero_barcos
        self.tablero_disparo = tablero_disparo

    def disparar(self, oponente, coordenadas):
        resultado_1 = recibir_disparo(oponente.tablero_barcos, coordenadas)
        if resultado_1 == "Acertaste":
            self.tablero_disparo[coordenadas] = "X"
        elif resultado_1 == "Agua":
            self.tablero_disparo[coordenadas] = "_"
        return resultado_1


#tablero_barcos_1 = flota(crear_tablero(10))
#tablero_disparos_1 = crear_tablero(10)


#tablero_barcos_2 = flota(crear_tablero(10))
#tablero_disparos_2 = crear_tablero(10)


#jugador_1_1 = Jugador("Player_1", tablero_barcos_1, tablero_disparos_1)
#jugador_2_2 = Jugador("Maquina_1", tablero_barcos_2, tablero_disparos_2)

# Funcion / Bucle para jugar por turnos
def jugar(jugador_1, jugador_2):               
    turno = "jugador"
    while True:
        if turno == "jugador":
            print(f"tu tablero de disparos: \n {jugador_1.tablero_disparo}")


            coordenadas = input("Dígame donde quiere disparar: ")
            try:
                coordenadas = tuple(int(n) for n in coordenadas.split(","))
            except ValueError:
                print("Debes introducir los número separados por una coma.")
                continue
            
            while (coordenadas[0] < 0 or coordenadas[0] >= 10 or coordenadas[1] < 0 or coordenadas[1] >= 10):
                print("Coordenadas fuera del tablero. Inténtelo de nuevo.")

                coordenadas = input("Introduzca otras coordenadas: ")
                coordenadas = tuple(int(n) for n in coordenadas.split(","))
            
            turno_disparo = jugador_1.disparar(jugador_2, coordenadas)
            print (jugador_1.tablero_disparo)


            if "O" not in jugador_2.tablero_barcos:
                print(f"Ha ganado el {jugador_1.nombre}")
                return "Has ganado"
                break
                
            if turno_disparo == "Agua" or turno_disparo == "Disparo invalido":
                turno = "maquina"

        else:
            print("Es el turno de tu oponente.")
                    
            disparo_random = (random.randint(0,9),random.randint(0,9))
            
            while jugador_2.tablero_disparo[disparo_random] != "~":
                    disparo_random = (random.randint(0,9),random.randint(0,9))
            print("Su disparo es en:", disparo_random)
            
            turno_disparo_2 = jugador_2.disparar(jugador_1, disparo_random)
            print (jugador_2.tablero_disparo)
            if "O" not in jugador_1.tablero_barcos:
                print(f"Ha ganado el {jugador_2.nombre}")
                return "Has perdido"
                break

            if turno_disparo_2 == "Agua" or turno_disparo_2 == "Disparo invalido":
                turno = "jugador"

                              

    

#Son 4 tableros (uno por jugador donde se reflejan los disparos y en otro donde están los barcos) Las comprobaciones son en cruzado (si jugador a dispara se marca en los barcos del b y asi)
#Función para disparar (luego en modo aleatorio poner condicion para que el disparo revisa si ya se disparó en el mismo lugar y si es el caso, volver a intentarlo)
#Para alternar los turnos hacer objetos(jugador 1 y jugador 2)
