inp = "/Users/marco/Developer/advent_of_code/2025/day6/input.txt"
filehandl= open(inp)
problems_rows = filehandl.readlines()

result = 0
problems_list = []
for row in problems_rows:
    p = row.split()
    problems_list.append(p)



results_list=[]
for p in range(len(problems_list[0])):
    res = 0
    m_res = 1
    if problems_list[4][p] == "+":
        for n in range(4):
            res += int(problems_list[n][p])
        results_list.append(res)
            
    if problems_list[4][p] == "*":
        for n in range(4):
            m_res *= int(problems_list[n][p])
        results_list.append(m_res)
        
     
for res in results_list:
    result += res

print(result)



