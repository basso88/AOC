'''The newly-improved calibration document consists of lines of text; 
each line originally contained a specific calibration value that the Elves now need to recover. 
On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?'''

file = 'coordinates.txt'
fhand = open(file)


lines = fhand.readlines()


def only_int(str):
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    inlist = list()
    n = ''
    for ch in str:
        if ch in numbers:
            inlist.append(ch)
        else: continue    
    nstr = n.join(inlist)
    return(int(nstr[0]+nstr[-1]))


sum = 0
for line in lines:
    sum = sum + only_int(line)
    print(only_int(line))

print(line)
print(sum)


#----- part two ------ #



'''Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters:
 one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".
Equipped with this new information, you now need to find the real first and last digit on each line.'''



def convert(string):

    dnums = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6',
            'seven':'7', 'eight':'8', 'nine':'9', 'zero':'0'}


    first_n = ''
    last_n  = ''
    for n in range(len(string)):
        for k in dnums:
            
            if string.startswith(k):
                first_n = (dnums[k])
                break
            elif string.startswith(dnums[k]):
                    first_n = (dnums[k])
                    break
        else:
            string = string[1:]
        
    for n in range(len(string)):
        for k in dnums:
            
            if string[::-1].startswith(k[::-1]):
                last_n = (dnums[k])
                break
            elif string[::-1].startswith(dnums[k]):
                    last_n = (dnums[k])
                    break
        else:
            string = string[:-1]
    
    coordinate = first_n + last_n
    return int(coordinate)


sum2 = 0
for line in lines:
     coordinates = convert(line)
     sum2 = sum2 + coordinates
     print(coordinates)
     
print(sum2)   
     
    
    

    
    
        
    