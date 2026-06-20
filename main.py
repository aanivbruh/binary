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
    ind = 0
    fakeNum = num
    str = ""

    while fakeNum > 2:
        new = fakeNum/2
        fakeNum = new
        ind+=1

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
    return answer


def addBinaryWBinary(string1:str,string2:str):
   #longer string is string1, shorter is string 2
   strResult = ""
   carry = 0
   if len(string1) < len(string2):
       place = string1
       string1 = string2
       string2 = place
   for x in range(len(string1)):
       result = 0
       num1 = string1[len(string1)-x-1:len(string1)-x]
       num2 = string2[len(string1)-x-1:len(string1)-x]
      
       if num2 == "0" and num1 == "0":
          result += 0
       elif num2 == "0" and num1 == "1" or (num2 == "1"  and num1 == "0"):
           result += 1
       else:
           result += 2

       result += carry

       if result < 2:
           strResult = str(result) + strResult
           carry = 0
       else:
          carry = 1
          strResult =  str(result%2) + strResult
   if carry == 1:
       strResult = "1" + strResult
   return strResult

print(addBinaryWBinary("11111","10101"))
    
       