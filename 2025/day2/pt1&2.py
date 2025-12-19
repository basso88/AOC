from pattern_checker import check_pattern
with open("/Users/marco/Developer/advent_of_code/2025/day2/input.txt","r") as fhandl:
    text = fhandl.readline()
    id_range_list = text.split(",")
    id_sum2 = 0
    id_sum = 0
    for id_range in id_range_list:
        edges = (id_range.split("-"))
        for n in range(int(edges[0]), int(edges[1])+1):
            n=str(n)
            if len(str(n))%2 == 0:
                if n[:(int(len(n)/2))] == n[(int(len(n)/2)):] and n[0] != "0":
                    id_sum += int(n)

            if check_pattern(n) == True:
                id_sum2 += int(n)
    print(id_sum)
    print(id_sum2)



                    

                
                
                