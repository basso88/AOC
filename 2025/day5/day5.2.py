input = "/Users/marco/Developer/advent_of_code/2025/day5/input.txt"
fhandl = open(input)
database = fhandl.read()
database = database.split()

range_ids = [x for x in database if "-" in x]

fresh_count = 0

splitted_range_list = []

for ran in sorted(range_ids):
    r = ran.split("-")
    ran_list=[int(r[0]),int(r[1])]
    splitted_range_list.append(ran_list)

splitted_range_list = sorted(splitted_range_list, key=lambda x : x[0])

merge=True
while merge:
    merge=False
    n = 0
    merged_ranges_list = []
    while n < len(splitted_range_list):
        if n+1 < len(splitted_range_list):
            
            if splitted_range_list[n][1] < splitted_range_list[n+1][0]:
                merged_ranges_list.append(splitted_range_list[n])
                

            elif splitted_range_list[n][1] >= splitted_range_list[n+1][0]:
                merged_range = [splitted_range_list[n][0], max(splitted_range_list[n+1][1], splitted_range_list[n][1])] #merged_range goes from the left edge of the range [n][0] to the biggest between [n][1] and [n+1][1]
                merged_ranges_list.append(merged_range)
                merge = True
                n+=1
        else:
            merged_ranges_list.append(splitted_range_list[n])
                    
        n+=1
                
    splitted_range_list = merged_ranges_list
    

for ran in merged_ranges_list:
    fresh_count += len(range(ran[0],ran[1]+1))

# print(merged_ranges_list, len(merged_ranges_list), "\n") 
print(fresh_count)