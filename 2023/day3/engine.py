
inp = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''

file = open('original_input.txt')


part_numbers = []

lines = file.readlines()
#lines = inp.split('\n')


def get_neighbors(j, i):
    neighbors = []
    #if ch.isdigit():
    for ny in range(-1, 2):
        for nx in range(-1, 2):
            if 0 <= j+ny <= (len(lines))-1 and 0 <= i+nx <= (len(lines[j]))-1:
                neigh_char = lines[j+ny][i+nx]
                if neigh_char == lines[j][i]:
                    continue
                if neigh_char != '.' and not neigh_char.isdigit():
                    return neigh_char
                
    
                     
n = ''                              
adj_lst = []                                
for j, string in enumerate(lines):
    print(string)                                
    for i, ch in enumerate(string):
        ch = lines[j][i]
        if ch.isdigit():  
            adj_ch = get_neighbors(j, i)              
            n = n + ch
            adj_lst.append(adj_ch)            
        elif n:                 
            #print(n, adj_lst)
            if any(item != None for item in adj_lst):
                part_numbers.append(int(n))

            n = ''
            adj_lst = []
                
                 
print(part_numbers)

tot = 0
for num in part_numbers:
    tot += num

print(tot)                   
                    
           
                                    
                        


                    
            
        

        


  
    
    

        

        
            
            
                

                
                
            
                
                

        

                

            
             

            

                
            
                
                    
                    
                      
                
                    

                
            
            
            
            

            
                
           
                
            
            



            
        

            
        



        
        

    
    
        
         
               
          
            
           
            
            

                
                

               
                
                
             
                

                


        



            

    

  





        


    
    
            
            

            



            
            
            


        
         
    