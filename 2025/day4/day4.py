input = "/Users/marco/Developer/advent_of_code/2025/day4/input.txt"
fhandle = open(input)
racks = fhandle.read()
racks = racks.split()
rolls_count = 0

for i, rack in enumerate(racks):
    for j in range(len(rack)):
        # print(racks[i][j], "(",i, j,")", end= "   ")
        
        if racks[i][j] == "@":
            neighbor_count = 0
                
       
            for h in range(-1, 2):
                if i+h < 0 or i+h > len(racks)-1:
                    continue
                for l in range(-1, 2):
                    if j+l < 0 or j+l > len(rack)-1:
                        continue
                    if h==0 and l==0:
                        continue
                    adjacent_spots = racks[i+h][j+l]
                    if adjacent_spots == "@":
                        neighbor_count += 1
                        
        
            if neighbor_count < 4:
                rolls_count += 1
print(rolls_count)

        

   
    
        
        
        

            
            

        
                    

                



