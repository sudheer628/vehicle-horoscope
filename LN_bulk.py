import math
class Solution:
   def solve(self, n):
      if n < 10:
         return n
      s = 0
      l = math.floor(math.log(n, 10) + 1)
      while l > 0:
         s += n % 10
         n //= 10
         l -= 1
      return self.solve(s)
ob = Solution()

import os, json, re
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
confile = "lib/pythagoras.json"
chalfile = "lib/chaldean.json"

with open('{}'.format(confile)) as f:
    FromConfig = json.load(f)
    f.close()

with open('{}'.format(chalfile)) as z:
    FromConfig2 = json.load(z)
    z.close()

def split(word):
    return [char for char in word]

def isAscending(xs):
    for n in range(len(xs) - 1):
        if xs[n] > xs[n+1]:
            return False
    return True

def logic(input_string, input_string2, horonum, threshold):
    total = 0
    list  = split(input_string)
    pythagorassum = 0
    pythagoras = []
    chaldean = []
    chaldeansum = 0
    for x in list:
        if x.isalpha():
            y = x.upper()
            pythagoras.append(FromConfig[y])
            chaldean.append(FromConfig2[y])
        else:
            pythagoras.append(x)
            chaldean.append(x)

    for num in pythagoras:
        pythagorassum += int(num)

    for num2 in chaldean:
        chaldeansum += int(num2)

    finalsum = ob.solve(pythagorassum)
    finalchaldean = ob.solve(chaldeansum)
    if int(finalsum) == 1:
        total = total + 2
    elif int(finalsum) == 2:
        total = total + 2
    elif int(finalsum) == 4:
        total = total + 1
    elif int(finalsum) == 5:
        total = total + 1   
    elif int(finalsum) == 6:
        total = total + 1
    elif int(finalsum) == 8:
        total = total + 1
    elif int(finalsum) == 9:
        total = total + 1

    vehnumber = input_string[-4:]
    vehnumber2 = re.findall("\d+", vehnumber)
    vehnumber3 = str(vehnumber2[0])
    A = 1
    result = []
    for i in range(0, len(vehnumber3), A):
        result.append(int(vehnumber3[i : i + A]))

    if isAscending(result):
        total = total + 0.5
    else:
        pass

    if len(input_string2) != 0:
        lucky  = split(input_string2)
        lucksum = 0
        for luk in lucky:
            lucksum += int(luk)
        finalluk = ob.solve(lucksum)

        if int(finalsum) == int(finalluk) and int(finalchaldean) == int(finalluk):
            total = total + 2
        elif int(finalsum) == int(finalluk) and int(finalchaldean) != int(finalluk):
            total = total + 1
        elif int(finalchaldean) == int(finalluk) and int(finalsum) != int(finalluk):
            total = total + 1

        try:
            value = int(horonum)
            if int(finalsum) == int(horonum) and int(finalchaldean) == int(horonum):
                total = total + 1
            elif int(finalsum) == int(horonum) and int(finalchaldean) != int(horonum):
                total = total + 1
            elif int(finalchaldean) == int(horonum) and int(finalsum) != int(horonum):
                total = total + 1
        except ValueError:
            pass

        fourdig  = split(vehnumber3)
        if fourdig[-1] == "1" or fourdig[0] == "1":
            if int(finalluk) == 1:
                total = total + 2
            else:
                total = total + 1
        if fourdig[-1] == "2" or fourdig[0] == "2":
            if int(finalluk) == 2:
                total = total + 1
            else:
                total = total + 0.5
        if fourdig[-1] == "4" or fourdig[0] == "4":
            if int(finalluk) == 4:
                total = total + 2
            else:
                total = total + 1
        if fourdig[-1] == "5" or fourdig[0] == "5":
            if int(finalluk) == 5:
                total = total + 2
            else:
                total = total + 1
        if fourdig[-1] == "6" or fourdig[0] == "6":
            if int(finalluk) == 6:
                total = total + 2
            else:
                total = total + 1
        if fourdig[-1] == "7" or fourdig[0] == "7":
            if int(finalluk) == 7:
                total = total + 0.5
            else:
                pass
        if fourdig[-1] == "8" or fourdig[0] == "8":
            if int(finalluk) == 8:
                total = total + 0.5

        if fourdig[-1] == "9" or fourdig[0] == "9":
            if int(finalluk) == 9:
                total = total + 0.5

        if int(finalluk) == 1:
            if int(finalsum) in (2, 3, 9) and int(finalchaldean) in (2, 3, 9):
                total = total + 2.5
            elif int(finalchaldean) in (2, 3, 9):
                total = total + 2
            elif int(finalsum) in (2, 3, 9):
                total = total + 1
            elif int(finalchaldean) in (6, 8):
                total = total - 1
            else:
                total = total + 1
        elif int(finalluk) == 2:
            if int(finalsum) in (1, 3) and int(finalchaldean) in (1, 3):
                total = total + 2.5
            elif int(finalchaldean) in (1, 3):
                total = total + 2
            elif int(finalsum) in (1, 3):
                total = total + 1
            elif int(finalchaldean) in (8, 9):
                total = total - 1
            else:
                total = total + 1
        elif int(finalluk) == 3:
            if int(finalsum) in (1, 2, 9) and int(finalchaldean) in (1, 2, 9):
                total = total + 2.5
            elif int(finalchaldean) in (1, 2, 9):
                total = total + 2
            elif int(finalsum) in (1, 2, 9):
                total = total + 1
            elif int(finalchaldean) in (5, 6):
                total = total - 1
            else:
                total = total + 1
        elif int(finalluk) == 4:
            if int(finalsum) in (5, 6, 8) and int(finalchaldean) in (5, 6, 8):
                total = total + 2.5
            elif int(finalchaldean) in (5, 6, 8):
                total = total + 2
            elif int(finalsum) in (5, 6, 8):
                total = total + 1
            elif int(finalchaldean) in (1, 2):
                total = total - 1
            else:
                total = total + 1
        elif int(finalluk) == 5:
            if int(finalsum) in (1, 4, 6) and int(finalchaldean) in (1, 4, 6):
                total = total + 2.5
            elif int(finalchaldean) in (1, 4, 6):
                total = total + 2
            elif int(finalsum) in (1, 4, 6):
                total = total + 1
            elif int(finalchaldean) in (2, 9):
                total = total - 1
            else:
                total = total + 1
        elif int(finalluk) == 6:
            if int(finalsum) in (4, 5, 8) and int(finalchaldean) in (4, 5, 8):
                total = total + 2.5
            elif int(finalchaldean) in (4, 5, 8):
                total = total + 2
            elif int(finalsum) in (4, 5, 8):
                total = total + 1
            elif int(finalchaldean) in (1, 9):
                total = total - 1
            else:
                total = total + 1
        elif int(finalluk) == 7:
            if int(finalsum) in (8, 6, 5) and int(finalchaldean) in (8, 6, 5):
                total = total + 2.5
            elif int(finalchaldean) in (8, 6, 5):
                total = total + 2
            elif int(finalsum) in (8, 6, 5):
                total = total + 1
            elif int(finalchaldean) in (6, 8):
                total = total - 1
            else:
                total = total + 1
        elif int(finalluk) == 8:
            if int(finalsum) in (4, 5, 6) and int(finalchaldean) in (4, 5, 6):
                total = total + 2.5
            elif int(finalchaldean) in (4, 5, 6):
                total = total + 2
            elif int(finalsum) in (4, 5, 6):
                total = total + 1
            elif int(finalchaldean) in (1, 2):
                total = total - 1
            else:
                total = total + 1
        elif int(finalluk) == 9:
            if int(finalsum) in (1, 2, 3) and int(finalchaldean) in (1, 2, 3):
                total = total + 2.5
            elif int(finalchaldean) in (1, 2, 3):
                total = total + 2
            elif int(finalsum) in (1, 2, 3):
                total = total + 1
            elif int(finalchaldean) in (5, 8):
                total = total - 1
            else:
                total = total + 1

        if total <= 0:
            total = 0
        elif total >= float(threshold):
            return input_string, total
        else:
            return "low_score"

input_string2 = input("Enter the DOB in DDMMYYYY format: ")
horonum = input("Enter your lucky number by your horoscope: ")
threshold = input("Score limit out of total 11 [exp: 5 - only numbers greater 5 are printed]: ")
print("")

inputfile = open('bulk-num-list.csv', 'r')
NumberLines = inputfile.readlines()
converted_list = []

for element in NumberLines:
    converted_list.append(element.strip())

print("Final scores for total of 11:")
for x in converted_list:
    y = logic(x, input_string2, horonum, threshold)
    if y != "low_score" and y is not None:
        finalcode = list(y)
        print(finalcode)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
