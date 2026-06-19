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
            raise ValueError("Not a valid binary string")
    return num

def convertToBinary(num:int):
    ind = int(num ** 0.5)
    str = ""
    while ind >=0 :
        if num >= 2 ** ind:
            num -= 2 ** ind
            str += "1"
        else:
            str += "0"
        ind-=1
    return str

def addBinary(string1:str,string2:str):
    answer =  convertToDecimal(string1) + convertToDecimal(string2)
    print(convertToBinary(answer))
    return answer

print(addBinary("1001","00000001354242"))
