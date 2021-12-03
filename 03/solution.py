diagnosticsLines = open("input.txt", "r").readlines()

def getFuelConsumption():
    # gamma rate => most common bit in each pos
    # epsilon rate => least common bit in each pos
    # fuel consumption => gamma rate * epsilon rate
    nrOfOnesInPos = [0] * (len(diagnosticsLines[0])-1)
    epsilonRateBinary = ""
    gammaRateBinary = ""
    
    for binaryNumber in diagnosticsLines:
        bits = list(binaryNumber.strip())
        for index, bit in enumerate(bits):
            nrOfOnesInPos[index] += int(bit)
    
    for pos in nrOfOnesInPos:
        if pos > len(diagnosticsLines)/2:
            epsilonRateBinary += "0"
            gammaRateBinary += "1"
        else:
           epsilonRateBinary += "1"
           gammaRateBinary += "0"
    
    return int(epsilonRateBinary, 2) * int(gammaRateBinary, 2)
    
        

def main():
    print(f'Part one: {getFuelConsumption()}')
    print(f'Part two: ')


if __name__ == "__main__":
    main()