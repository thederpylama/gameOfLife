import copy
import sys
import pygame
from pygame.locals import *


sizeOfGrid = 10

tempArr = []

pygame.init()

window = pygame.display.set_mode((1000, 1000))

window.fill((255, 255, 255))

pygame.draw.rect(window, (0, 0, 255), [100, 100, 400, 100], 2)

pygame.display.update()
def createGrid(sizeOfGrid):

    _sizeOfGrid = sizeOfGrid






def boundaries(sizeOfGrid, neighborsAlive):

    arrTemp = []
    currentState = []
    nextState = []
    blank = []
    size = 10
    for i in range(size + 2):
        arrTemp.append(-1)

    currentState.append(arrTemp)

    for j in range(size):
        arr_1d = []
        arr_1d.append(-1)

        for k in range(size):
            arr_1d.append(0)
        arr_1d.append(-1)
        currentState.append(arr_1d)


    currentState.append(arrTemp)

    nextState = copy.deepcopy(currentState)
    blank = copy.deepcopy(currentState)

    currentState[1][2] = 1
    currentState[2][3] = 1
    currentState[3][3] = 1
    currentState[3][2] = 1
    currentState[3][1] = 1


    for y in range(len(currentState)):
        print(currentState[y])

    for z in range(len(nextState)):
        print(nextState[z])


    x = 0



    while x < 10:

        for k in range(1, (len(currentState) - 1)):
            for l in range(1, (len(currentState[0]) - 1)):

                neighborsAlive = 0

                if currentState[k][l - 1] == 1:
                    neighborsAlive += 1

                if currentState[k][l + 1] == 1:
                    neighborsAlive += 1

                if currentState[k + 1][l] == 1:
                    neighborsAlive += 1

                if currentState[k + 1][l - 1] == 1:
                    neighborsAlive += 1

                if currentState[k + 1][l + 1] == 1:
                    neighborsAlive += 1

                if currentState[k - 1][l] == 1:
                    neighborsAlive += 1

                if currentState[k - 1][l - 1] == 1:
                    neighborsAlive += 1

                if currentState[k - 1][l + 1] == 1:
                    neighborsAlive += 1

                if currentState[k][l] == 1 and neighborsAlive <= 1:
                    nextState[k][l] = 0


                elif currentState[k][l] == 1 and neighborsAlive >= 4:
                    nextState[k][l] = 0

                elif currentState[k][l] == 1 and (neighborsAlive == 2 or neighborsAlive == 3):
                    nextState[k][l] = 1

                elif currentState[k][l] == 0 and neighborsAlive == 3:
                    nextState[k][l] = 1
                    #print("h")
                else:
                    pass

                print(str(nextState[k][l]), end=" ")
            print("\n")
        # update states
        print("\n")
        currentState = copy.deepcopy(nextState)
        nextState = copy.deepcopy(blank)

        # shuffle next and current state

        x+=1



createGrid(sizeOfGrid)

boundaries(10, 0)








