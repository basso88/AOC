
import math

inp = "/Users/marco/Developer/advent_of_code/2025/day6/input.txt"
filehandl= open(inp)
problems_rows = filehandl.readlines()

result = 0
result_list = []
nums_list = []
operator = []
i = 0
while i < len(problems_rows[0]):
    num=""
    for row in problems_rows:
        if row[i].isdigit():
            num += row[i]
        
        if row[i] == "+" or row[i] == "*":
            operator.append(row[i])
        else:
            continue

    if num.isdigit():
        num.strip()
        nums_list.append(int(num))
    else:
        if operator[0] =='*':
            result_list.append(math.prod(nums_list))
            nums_list = []
            operator = []
        elif operator[0] =='+':
            result_list.append(sum(nums_list))
            nums_list = []
            operator = []

        
    i+=1
            
    
nums_list = []   
print(sum(result_list))
    

