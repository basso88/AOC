
file = "/Users/marco/Developer/advent_of_code/2025/day1/day1.txt"
fhandl = open(file)
lines = fhandl.readlines()


password = 0
dial_number = 50

for line in lines:
    direction = line[0]
    clicks = int(line[1:])

    if clicks > 100:
        clicks = clicks%100
        
    if direction == "L":
        dial_number -= clicks
        if dial_number < 0:
            dial_number += 100

    if direction == "R":
        
        dial_number += clicks
        if dial_number > 99:
            dial_number -= 100
    if dial_number == 0:
        password += 1
        
print(password)



    


        

    

        


