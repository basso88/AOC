

def highest_joltage(bank):
    highest_joltage = ""
    start = 0
    while len(highest_joltage) < 12:
        
        remaining_numbers = 12 - len(highest_joltage)-1
        end = len(bank) - remaining_numbers
        best_jolt = "0"
        best_index = start

        for n in range(start, end):
            if bank[n] > best_jolt:
                best_jolt = bank[n]
                best_index = n
    
        start=best_index+1
        highest_joltage += best_jolt
        
    return highest_joltage            
            

input = "/Users/marco/Developer/advent_of_code/2025/day3/day3.txt"
with open(input) as fhandl:
    banks = fhandl.readlines()

tot_jolts = 0
for bank in banks:
    bank = bank.strip()

    highest_jolt= highest_joltage(bank)
    tot_jolts += int(highest_jolt)

    
print(tot_jolts)  
    