def userInput():
    data = input("please type 5 numbers:")
    return data
def writeToTextFile(filePath, data):
    file = open(filePath, "w")
    file.write(data)
    file.close()
def readFromTextFile(filePath):
    file = open(filePath, "r")
    line = file.readline()
    list = line.split(",")
    intList = [int(num) for num in list]
    return intList
def totalOFList(list):
    total = 0
    for i in range(len(list)):
        total += list[i]
        return total
def main():
    filePath = "totalOfList.txt"
    userData = userInput()
    writeToTextFile(filePath, userData)
    dataFromFile = readFromTextFile(filePath)
    total = totalOFList(dataFromFile)
    print(total)
if __name__ == "__main__":
    main()

