
import math

input = "/Users/marco/Developer/advent_of_code/2025/day6/input.txt"
filehandl= open(input)
problems_rows = filehandl.readlines()

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
        
    if num.isdigit():
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

print(sum(result_list))
        
  
    
    

