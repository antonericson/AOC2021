directionLines = open("input1.txt", "r").readlines()

def calculateDepth():
    directions = dict()
    for line in directionLines:
        currentDirectionData = line.replace("\n","").split(" ")
        currentDirection = currentDirectionData[0]
        currentMovement = int(currentDirectionData[1])
        
        if currentDirectionData[0] in directions.keys():
            directions[currentDirection] += currentMovement 
        else:
            directions[currentDirection] = currentMovement
        
    xPos = directions["forward"]
    yPos = directions["down"] - directions["up"]
    
    return xPos * yPos

def main():
    print(f'Part one: {calculateDepth()}')


if __name__ == "__main__":
    main()