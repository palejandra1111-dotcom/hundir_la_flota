from ejercicio import *
# Crear tableros
tablero_1 = crear_tablero(10)

# Barcos manuales
colocar_barco(tablero_1, [(0,0), (0,1)])
colocar_barco(tablero_1, [(2,0), (2,1)])
colocar_barco(tablero_1, [(4,0), (4,1)])

colocar_barco(tablero_1, [(6,0), (6,1), (6,2)])
colocar_barco(tablero_1, [(8,0), (8,1), (8,2)])

colocar_barco(tablero_1, [(0,5), (0,6), (0,7), (0,8)])

# Tablero de la máquina (aleatorio)
tablero_2 = flota(crear_tablero(10))

# Crear jugadores
jugador_1 = Jugador("Player_1", tablero_1, crear_tablero(10))
jugador_2 = Jugador("Maquina_1", tablero_2, crear_tablero(10))

jugar(jugador_1, jugador_2)