def reverse(string1:str):
    newS = ""
    for letter in string1:
        newS = letter + newS
    return newS

def convertToDecimal(string1: str):
    string1 = reverse(string1)
    num = 0
    index = 0
    for letter in string1:
        if letter == "0" or letter == "1": 
            num += int(letter) * (2 ** index)
            index += 1
        else:
            return "Invalid input"
    return num


def addBinary(string1:str,string2:str):
    return convertToDecimal(string1) + convertToDecimal(string2)

print(addBinary("1001","1"))