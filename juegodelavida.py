#Importantdo librerías
import matplotlib.pyplot as plt
import numpy as np
import random as RD

#Configuración inicial de la simulación
width = 50
height = 50
initProb = 0.2

def init():
    #Tablero con células vivas o muertas al azar
    board = np.zeros((height, width), dtype=int)
    for x in range(width):
        for y in range(height):
            if RD.random() < initProb:
                board[y, x] = 1  #Celda viva
            else:
                board[y, x] = 0  #Celda muerta
    return board

def update(board):
    #Crea un nuevo tablero para el siguiente estado
    next_board = board.copy()
    for x in range(width):
        for y in range(height):
            #Cuenta las celdas vivas alrededor
            alive_neighbors = np.sum(board[max(0, y-1):min(y+2, height), max(0, x-1):min(x+2, width)]) - board[y, x]
            
            #Aplica las reglas del Juego de la Vida
            if board[y, x] == 0 and alive_neighbors == 3:
                next_board[y, x] = 1  #Celda revive
            elif board[y, x] == 1 and (alive_neighbors < 2 or alive_neighbors > 3):
                next_board[y, x] = 0  #Celda muere
    return next_board

def simulate(steps=50):
    board = init()
    
    plt.figure(figsize=(2, 2))
    for step in range(steps):
        plt.cla()
        plt.imshow(board, cmap="binary")
        plt.title(f"Juego de la Vida - Iteración {step + 1}")
        plt.axis("off")
        plt.pause(0.1)
        
        #Actualiza el tablero para el siguiente paso
        board = update(board)

    plt.show()

#Ejecuta la simulación
simulate(steps=50) #Unicamente se ejecuta 50 iteraciones