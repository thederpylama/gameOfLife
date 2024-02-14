def noWallsDetection(sizeOfGrid, neighborsAlive):

    tempArr = []
    currentState = []

    for i in range(sizeOfGrid):
        tempArr.append(0)


    for j in range(sizeOfGrid):
        currentState.append(tempArr)

    for y in range(len(currentState)):
        print(currentState[y])

    for k in range(len(currentState)):
        for l in range(len(currentState[0])):

            # checks to do if cell is at top and not against either side
            if (k - 1) == -1 and (l - 1) != -1 and (not ((l + 1) > sizeOfGrid)):

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

            elif (k + 1) > sizeOfGrid and (l - 1) != -1 and (not ((l + 1) > sizeOfGrid)):

                if currentState[k][l - 1] == 1:
                    neighborsAlive += 1

                if currentState[k][l + 1] == 1:
                    neighborsAlive += 1

                if currentState[k - 1][l] == 1:
                    neighborsAlive += 1

                if currentState[k - 1][l - 1] == 1:
                    neighborsAlive += 1

                if currentState[k - 1][l + 1] == 1:
                    neighborsAlive += 1

            elif True:

                if (k + 1) > sizeOfGrid:
                    pass

            else:
                pass

    return 7

