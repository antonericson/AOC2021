import string

input_lines =  open("input.txt", "r").readlines()

def part1():
    numberOfIncreases = 0
    prevNumber = int(input_lines[0])
    for number in input_lines:
        if (int(number) > int(prevNumber)):
            numberOfIncreases += 1
        prevNumber = number

    print("1. Number of increases: ", numberOfIncreases)

def part2():
    numberOfIncreases = 0
    prevSum = int(input_lines[0]) + int(input_lines[1]) + int(input_lines[2])
    for i in range(0, len(input_lines)):
        currentNumber = int(input_lines[i])
        if len(input_lines) <= i+2:
            break
        currentSum = int(input_lines[i]) + int(input_lines[i+1]) + int(input_lines[i+2])
        if currentSum > prevSum:
            numberOfIncreases += 1

        prevSum = currentSum
    
    print("2. Number of increases: ", numberOfIncreases)

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()