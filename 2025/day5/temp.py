
    
    
ranges = '''3-5
10-14
16-20
17-18'''
fresh_count = 0
ranges_list = ranges.strip().split()
splitted_range_list = []

for ran in ranges_list:
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
                merged_range = [splitted_range_list[n][0], max(splitted_range_list[n+1][1],splitted_range_list[n][1])]
                merged_ranges_list.append(merged_range)
                merge = True
                n += 1

        else:
            merged_ranges_list.append(splitted_range_list[n])       
        n+=1
                
    splitted_range_list = merged_ranges_list

print(merged_ranges_list)
for r in merged_ranges_list:
    fresh_count += len(range(r[0], r[1]+1))        

print(fresh_count)
    
    # print( splitted_range_list, len(splitted_range_list))
