
input = "/Users/marco/Developer/advent_of_code/2025/day3/day3.txt"
with open(input) as fhandl:
    banks = fhandl.readlines()


    jolts_list = []
    tot_jolts = 0
    for bank in banks:
        bank = bank.strip()

        for j in bank:
            jolts_list.append(j)

        highest_jolt = 0
        first_jolt = 0
        index = 0
        second_jolt = 0
        
        for j in jolts_list[:-1]:
            if int(j) > first_jolt:
                first_jolt = int(j)
                index = jolts_list.index(j)

        for k in jolts_list[index+1:]:
            if int(k) > second_jolt:
                second_jolt = int(k)


        highest_jolt = first_jolt *10 + second_jolt
            
        # print(highest_jolt)
        jolts_list = []
        tot_jolts += highest_jolt
    print(tot_jolts)

                
