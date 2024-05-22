input = '''....
.5..
#...'''
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        str = "Point x{} y{}".format(self.x, self.y)
        return str


def multidigitnumber(ch):  
    number = '' 
    if ch.isdigit(): 
        number += ch
    elif number != '':
        print(number)
        yield number


schema = []
cx = []
cy = []
coordinates = []

lines = input.split('\n')
    
for i, line in enumerate(lines):
    schema.append(line)
    for j, ch in enumerate(line):
        cx.append(j)
        cy.append(i)
print(schema[1][1])
coordinates.append(list(zip(cx,cy)))
print(coordinates)       
for coordinate in coordinates:
    neighbors = []
    for x, y in coordinate:
           print(Point(x, y))

           
        #if schema[x][y].isdigit():
           
           ''' n = schema[x][y]
            n = multidigitnumber(n)
            for ny in [-1, 0, 1]:
                for nx in range(-1, len(n)+1):
                    if schema[x+nx][y+ny].isdigit(): 
                        continue
                    elif schema[x+nx][y+ny] != '.':
                        neighbors.append(n)
                    
    print(neighbors)   '''

            
                
   

        
    
  





    

    
    
       
        
    






        

    





        
        
        

                
                  
                
                
                
                
                
                


        

        






             
           
        

            

            
                

            

    
            
            
            
            




            

             
    


         

        





        


    
            


              



