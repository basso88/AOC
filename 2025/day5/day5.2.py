input = "/Users/marco/Developer/advent_of_code/2025/day5/input.txt"
fhandl = open(input)
database = fhandl.read()
database = database.split()

range_ids = [x for x in database if "-" in x]

fresh_count = 0

splitted_range_list = []

for ran in sorted(range_ids):
    r = ran.split("-")
    ran_list=[r[0],r[1]]
    splitted_range_list.append(ran_list)

merge = True
while merge:
    merged_ranges_list = []
    merge = False
    for n in range(len(splitted_range_list)):
        if n+1 >= len(splitted_range_list):
            merged_ranges_list.append(splitted_range_list[n])
            continue
            
        if splitted_range_list[n][0]< splitted_range_list[n+1][0] and splitted_range_list[n][1] > splitted_range_list[n+1][0]:
            new_range_list = [splitted_range_list[n][0], splitted_range_list[n+1][1]]
            merged_ranges_list.append(new_range_list)
            merge = True
            break
            
            
        elif splitted_range_list[n][1] < splitted_range_list[n+1][0]:
            merged_ranges_list.append(splitted_range_list[n])

    splitted_range_list = merged_ranges_list
        

for n in range(len(merged_ranges_list)-1, 0, -1):
    if merged_ranges_list[n][1] == merged_ranges_list[n-1][1]:
        merged_ranges_list.pop(n-1)
       

for ran in merged_ranges_list:
    fresh_count += len(range(int(ran[0]),int(ran[1])))

print(merged_ranges_list, "\n") 
print(fresh_count)