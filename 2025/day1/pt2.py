file = "/Users/marco/Developer/advent_of_code/2025/day1/day1.txt"
fhandl = open(file)
lines = fhandl.readlines()


password = 0
dial_number = 50

        
for line in lines:
    direction = line[0]
    clicks = int(line[1:])

    if direction == "L":
        password += clicks//100
        if dial_number != 0 and (dial_number - clicks%100) <= 0:
            password += 1

        if dial_number - clicks%100 < 0:
            dial_number = (dial_number - clicks%100) +100 
        else:
            dial_number -= clicks%100

    if direction == "R":
        password += clicks//100 + (dial_number + clicks%100)//100
        
        if dial_number + clicks%100 > 99:
            dial_number = (dial_number + clicks%100) - 100
        else:
            dial_number += clicks%100

        
   # print(dial_number)

print("password is", password)


    

