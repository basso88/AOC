
item_priority_dict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13,
                       'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25,
                       'z':26, 'A':27, 'B':28, 'C':29, 'D':30, 'E':31, 'F':32, 'G':33, 'H':34, 'I':35, 'J':36, 'K':37, 'L':38, 
                       'M':39, 'N':40, 'O':41, 'P':42, 'Q':43, 'R':44, 'S':45, 'T':46, 'U':47, 'V':48, 'W':49, 'X':50, 'Y':51,
                       'Z':52}

input = "/Users/marco/Developer/advent_of_code/2022/day_3/input.txt"

fhandle = open(input)


first_compartment_list = []
second_compartment_list = []
for line in fhandle:
    stripline = line.strip()

    first_compartment = stripline[:int(len(stripline)/2)]
    first_compartment_list.append(first_compartment)

    second_compartment = stripline[int(len(stripline)/2):]
    second_compartment_list.append(second_compartment)
    
   
count = 0
sum = 0
for n in range(300):
    for item in first_compartment_list[n]:
        if item in second_compartment_list[n]:
            sum += item_priority_dict[item]
            count += 1
            #print(count, ':', item)
            break
print(sum)


#-------- part two -----------

for i , line in enumerate(fhandle):
    print(i, line)





    
            
            
            
            
            

   


    
        
            



  
    
