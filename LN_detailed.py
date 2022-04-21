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
total = 0
confile = "pythagoras.json"
chalfile = "chaldean.json"

with open('{}'.format(confile)) as f:
    FromConfig = json.load(f)
    f.close()

with open('{}'.format(chalfile)) as z:
    FromConfig2 = json.load(z)
    z.close()

def split(word):
    return [char for char in word]

input_string = input("Enter the registration number: ")
input_string2 = input("Enter the DOB in DDMMYYYY format: ")
horonum = input("Enter your lucky number by your horoscope: ")

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
print("")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("Generated Number as per pythagoras system -", finalsum, "and chaldean system -", finalchaldean)
#print("Generated Number as per chaldean system:", finalchaldean)
print("")
print("@@Nature of this vehicle@@")
############## Total points - 2
if int(finalsum) == 1:
    print("A vehicle with 01 as a number is the leader on the road. It accelerates quickly, is reliable and attracts attention. It is very favourable for business people. 11- Doubles the value of one")
    total = total + 2
elif int(finalsum) == 2:
    print("Such a vehicle is reliable and rarely breaks down and is a very promising number. Such vehicles rarely get stolen or stopped by traffic cops. A vehicle with the energy of two is a real fortress on wheels. 22 – Enhances the influence of number 2.")
    total = total + 2
elif int(finalsum) == 3:
    print("The number 3 is a somewhat inconsistent number on a vehicle. On the upside, though, the number brings good luck for some, especially those whose professions are related to money. It can puncture a tire in the middle of the road and cause minor troubles if you are not attentive to it.")
elif int(finalsum) == 4:
    print("Well, this vehicle is not designed for fast driving on the road. The vehicle is not for business people, but great for creative people. It rarely has a serious break down. Fortunately, the accidents are not of a serious nature.")
    total = total + 1
elif int(finalsum) == 5:
    print("The number five promotes unreasonable rearrangements and resourcefulness on the road, but gets along well with other travellers on the way and rarely has accidents.")
    total = total + 1   
elif int(finalsum) == 6:
    print("A combination of 6 with other even numbers is the best option for the most expensive vehicles as it will give service for a long time and will not fail.")
    total = total + 1
elif int(finalsum) == 7:
    print("A vehicle with a registration number that translates into the number seven does not attract attention in the stream. It rarely breaks down, but the vehicle body is very susceptible to corrosion.It will not work well as a taxi, since no one will try to get into this car because of its inconspicuousness.")
elif int(finalsum) == 8:
    print("Eight is a reliable vehicle for quiet riders. It is not able to show character, but rarely breaks down. A vehicle with such a number plate is efficient and a good choice for commuting. ")
    total = total + 1
elif int(finalsum) == 9:
    print("A vehicle with 9 is an impulsive machine that loves to drive. This number means you take quick decisions, but may also drive too fast. It does not tolerate obstructions and does not let other traffic overtake it on the road.It is a car for influential people.")
    total = total + 1
print("")

vehnumber = input_string[-4:]
vehnumber2 = re.findall("\d+", vehnumber)
vehnumber3 = str(vehnumber2[0])
A = 1
# create a result list
result = []
for i in range(0, len(vehnumber3), A):
    # convert to int, after the slicing process
    result.append(int(vehnumber3[i : i + A]))

def isAscending(xs):
    for n in range(len(xs) - 1):
        if xs[n] > xs[n+1]:
            return False
    return True
############## Total points - 0.5
if isAscending(result):
    print("Great, Vehicle number is a raising number.")
    total = total + 0.5
else:
    pass

if len(input_string2) != 0:
    lucky  = split(input_string2)
    lucksum = 0
    for luk in lucky:
        lucksum += int(luk)
############## Total points - 2
    print("")
    print("@@Matching or Not matching@@")
    finalluk = ob.solve(lucksum)
    print("your birth number is", finalluk)
    if int(finalsum) == int(finalluk) and int(finalchaldean) == int(finalluk):
        print("Awesome.. Birth Number is matched with pythagoras & chaldean numbers")
        total = total + 2
    elif int(finalsum) == int(finalluk) and int(finalchaldean) != int(finalluk):
        print("Awesome.. Birth Number is matched with pythagoras number")
        total = total + 1
    elif int(finalchaldean) == int(finalluk) and int(finalsum) != int(finalluk):
        print("Awesome.. Birth Number is matched with chaldean number")
        total = total + 1

############## Total points - 1
    try:
        value = int(horonum)
        if int(finalsum) == int(horonum) and int(finalchaldean) == int(horonum):
            print("Awesome.. Horoscope Number is matched with pythagoras & chaldean systems")
            total = total + 1
        elif int(finalsum) == int(horonum) and int(finalchaldean) != int(horonum):
            print("Awesome.. Horoscope Number is matched with pythagoras systems")
            total = total + 1
        elif int(finalchaldean) == int(horonum) and int(finalsum) != int(horonum):
            print("Awesome.. Horoscope Number is matched with chaldean systems")
            total = total + 1
    except ValueError:
        print("Horoscope lucky number was not given!")

    print("")
    print("Prediction based on 4 Digit registration number", vehnumber3)
    fourdig  = split(vehnumber3)

############## Total points - 3
    if fourdig[-1] == "1" or fourdig[0] == "1":
        if int(finalluk) == 1:
            print("Started or ended with 1 - Its a very good sign for the vehicle. also matched with birth number")
            total = total + 2
        else:
            print("Started or ended with 1 - Its a very good sign for the vehicle.")
            total = total + 1
    if fourdig[-1] == "2" or fourdig[0] == "2":
        if int(finalluk) == 2:
            print("Started or ended with 2 - Good sign for vehicle, but indicates unnecessary travelling, vehicle will not have rest.")
            total = total + 1
        else:
            print("Started or ended with 2 - Good sign for vehicle, but indicates unnecessary travelling, vehicle will not have rest.")
            total = total + 0.5
    if fourdig[-1] == "3" or fourdig[0] == "3" or ("3" in fourdig):
        print("It contains 3 - Not a good sign for vehicle, accident prone number. ")
    if fourdig[-1] == "4" or fourdig[0] == "4":
        if int(finalluk) == 4:
            print("Started or ended with 4 - Good for a family, no repairs, no accidents. also matched with birth number")
            total = total + 2
        else:
            print("Started or ended with 4 - Good for a family, no repairs, no accidents.")
            total = total + 1
    if fourdig[-1] == "5" or fourdig[0] == "5":
        if int(finalluk) == 5:
            print("Started or ended with 5 - Very Very Best sign for your vehicle. also matched with birth number")
            total = total + 2
        else:
            print("Started or ended with 5 - Very Very Best sign for your vehicle.")
            total = total + 1
    if fourdig[-1] == "6" or fourdig[0] == "6":
        if int(finalluk) == 6:
            print("Started or ended with 6 - Very Good sign for vehicle, gives lot of maintenance, but matched with birth number, so no worry")
            total = total + 2
        else:
            print("Started or ended with 6 - Very Good sign for vehicle, gives lot of maintenance.")
            total = total + 1
    if fourdig[-1] == "7" or fourdig[0] == "7":
        if int(finalluk) == 7:
            print("Started or ended with 7 - Not at all a good sign for vehicle, accident prone number, but matched with birth number, so no worry")
            total = total + 0.5
        else:
            print("Started or ended with 7 - Not at all a good sign for vehicle, accident prone number.")
    if fourdig[-1] == "8" or fourdig[0] == "8":
        if int(finalluk) == 8:
            print("Started or ended with 8 - Not a good sign for vehicle, but matched with birth number, so no worry")
            total = total + 0.5
        else:
            print("Started or ended with 8 - Not good, minor accident prone, good for commercial purposes.")
    if fourdig[-1] == "9" or fourdig[0] == "9":
        if int(finalluk) == 9:
            print("Started or ended with 9 - Not a good sign for vehicle, but matched with birth number, so it became good for owner. Tip: keep well maintained")
            total = total + 0.5
        else:
            print("Started or ended with 9 - It damages battery, wires, ignition., etc.")
    if ("0" in fourdig):
        print("")
        print("A single zero will not affect you in any way. But do avoid multiple zeros.")

############## Total points - 2.5
    if int(finalluk) == 1:
        if int(finalsum) in (2, 3, 9) and int(finalchaldean) in (2, 3, 9):
            print("Awesome.. Birth Number is compatible with pythagoras & chaldean systems")
            total = total + 2.5
        elif int(finalchaldean) in (2, 3, 9):
            print("Birth Number is compatible with chaldean systems")
            total = total + 2
        elif int(finalsum) in (2, 3, 9):
            print("Birth Number is compatible with pythagoras systems")
            total = total + 1
        elif int(finalchaldean) in (6, 8):
            print("your lucky number 1 and not compitable with 6 or 8")
            total = total - 1
        else:
            print("Birth number", finalluk,"neither matched or opposed with chaldean number", finalchaldean)
            total = total + 1
    elif int(finalluk) == 2:
        if int(finalsum) in (1, 3) and int(finalchaldean) in (1, 3):
            print("Awesome.. Birth Number is compatible with pythagoras & chaldean systems")
            total = total + 2.5
        elif int(finalchaldean) in (1, 3):
            print("Birth Number is compatible with chaldean systems")
            total = total + 2
        elif int(finalsum) in (1, 3):
            print("Birth Number is compatible with pythagoras systems")
            total = total + 1
        elif int(finalchaldean) in (8, 9):
            print("your lucky number 2 is not compitable with 8 or 9")
            total = total - 1
        else:
            print("Birth number", finalluk,"neither matched or opposed with chaldean number", finalchaldean)
            total = total + 1
    elif int(finalluk) == 3:
        if int(finalsum) in (1, 2, 9) and int(finalchaldean) in (1, 2, 9):
            print("Awesome.. Birth Number is compatible with pythagoras & chaldean systems")
            total = total + 2.5
        elif int(finalchaldean) in (1, 2, 9):
            print("Birth Number is compatible with chaldean systems")
            total = total + 2
        elif int(finalsum) in (1, 2, 9):
            print("Birth Number is compatible with pythagoras systems")
            total = total + 1
        elif int(finalchaldean) in (5, 6):
            print("your lucky number 3 is not compitable with 5 or 6")
            total = total - 1
        else:
            print("Birth number", finalluk,"neither matched or opposed with chaldean number", finalchaldean)
            total = total + 1
    elif int(finalluk) == 4:
        if int(finalsum) in (5, 6, 8) and int(finalchaldean) in (5, 6, 8):
            print("Awesome.. Birth Number is compatible with pythagoras & chaldean systems")
            total = total + 2.5
        elif int(finalchaldean) in (5, 6, 8):
            print("Birth Number is compatible with chaldean systems")
            total = total + 2
        elif int(finalsum) in (5, 6, 8):
            print("Birth Number is compatible with pythagoras systems")
            total = total + 1
        elif int(finalchaldean) in (1, 2):
            print("your lucky number 4 is not compitable with 1 or 2")
            total = total - 1
        else:
            print("Birth number", finalluk,"neither matched or opposed with chaldean number", finalchaldean)
            total = total + 1
    elif int(finalluk) == 5:
        if int(finalsum) in (1, 4, 6) and int(finalchaldean) in (1, 4, 6):
            print("Awesome.. Birth Number is compatible with pythagoras & chaldean systems")
            total = total + 2.5
        elif int(finalchaldean) in (1, 4, 6):
            print("Birth Number is compatible with chaldean systems")
            total = total + 2
        elif int(finalsum) in (1, 4, 6):
            print("Birth Number is compatible with pythagoras systems")
            total = total + 1
        elif int(finalchaldean) in (2, 9):
            print("your lucky number 5 is not compitable with 2 or 9")
            total = total - 1
        else:
            print("Birth number", finalluk,"neither matched or opposed with chaldean number", finalchaldean)
            total = total + 1
    elif int(finalluk) == 6:
        if int(finalsum) in (4, 5, 8) and int(finalchaldean) in (4, 5, 8):
            print("Awesome.. Birth Number is compatible with pythagoras & chaldean systems")
            total = total + 2.5
        elif int(finalchaldean) in (4, 5, 8):
            print("Birth Number is compatible with chaldean systems")
            total = total + 2
        elif int(finalsum) in (4, 5, 8):
            print("Birth Number is compatible with pythagoras systems")
            total = total + 1
        elif int(finalchaldean) in (1, 9):
            print("your lucky number 6 is not compitable with 1 or 9")
            total = total - 1
        else:
            print("Birth number", finalluk,"neither matched or opposed with chaldean number", finalchaldean)
            total = total + 1
    elif int(finalluk) == 7:
        if int(finalsum) in (8, 6, 5) and int(finalchaldean) in (8, 6, 5):
            print("Awesome.. Birth Number is compatible with pythagoras & chaldean systems")
            total = total + 2.5
        elif int(finalchaldean) in (8, 6, 5):
            print("Birth Number is compatible with chaldean systems")
            total = total + 2
        elif int(finalsum) in (8, 6, 5):
            print("Birth Number is compatible with pythagoras systems")
            total = total + 1
        elif int(finalchaldean) in (6, 8):
            print("your lucky number 7 is not compitable with 6 or 8")
            total = total - 1
        else:
            print("Birth number", finalluk,"neither matched or opposed with chaldean number", finalchaldean)
            total = total + 1
    elif int(finalluk) == 8:
        if int(finalsum) in (4, 5, 6) and int(finalchaldean) in (4, 5, 6):
            print("Awesome.. Birth Number is compatible with pythagoras & chaldean systems")
            total = total + 2.5
        elif int(finalchaldean) in (4, 5, 6):
            print("Birth Number is compatible with chaldean systems")
            total = total + 2
        elif int(finalsum) in (4, 5, 6):
            print("Birth Number is compatible with pythagoras systems")
            total = total + 1
        elif int(finalchaldean) in (1, 2):
            print("your lucky number 8 is not compitable with 1 or 2")
            total = total - 1
        else:
            print("Birth number", finalluk,"neither matched or opposed with chaldean number", finalchaldean)
            total = total + 1
    elif int(finalluk) == 9:
        if int(finalsum) in (1, 2, 3) and int(finalchaldean) in (1, 2, 3):
            print("Awesome.. Birth Number is compatible with pythagoras & chaldean systems")
            total = total + 2.5
        elif int(finalchaldean) in (1, 2, 3):
            print("Birth Number is compatible with chaldean systems")
            total = total + 2
        elif int(finalsum) in (1, 2, 3):
            print("Birth Number is compatible with pythagoras systems")
            total = total + 1
        elif int(finalchaldean) in (5, 8):
            print("your lucky number 9 is not compitable with 5 or 8")
            total = total - 1
        else:
            print("Birth number", finalluk,"neither matched or opposed with chaldean number", finalchaldean)
            total = total + 1

    if total <= 0:
        print("Vehicle number not supportive, this must be avoided.")
    else:
        print("Vehicle total points", total, "out of 11")

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
