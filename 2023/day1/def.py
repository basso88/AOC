
#example = 'nfsbf4ji6bihg23biu7kjg9'

def only_int(str):
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    inlist = list()
    n = ''
    for ch in example:
        if ch in numbers:
            inlist.append(ch)
        else: continue    
    nstr = n.join(inlist)
    return(int(nstr[0]+nstr[-1]))
    
    
#print(only_int(example))


example = '''two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen'''

def converter(string):

    dnums = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6',
         'seven':'7', 'eight':'8', 'nine':'9', 'zero':'0'}
    part_w = ''
    count = 0
    matches = []
    for ch in string: 
        part_w = part_w + ch
        count = count + 1
        for k in dnums:
            if part_w == k or part_w == dnums[k]:
                matches.append(dnums[k])
                nstr = ''.join(matches)
                num = int(nstr[0]+nstr[-1])
                part_w = part_w[count:]
    return(num)        


 #--------------------------------------------------------------------------------#



def convert(string):

    dnums = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6',
            'seven':'7', 'eight':'8', 'nine':'9', 'zero':'0'}


    first_n = ''
    last_n  = ''
    for n in range(len(string)):
        for k in dnums:
            
            if string.startswith(k):
                first_n = (dnums[k])
                break
            elif string.startswith(dnums[k]):
                    first_n = (dnums[k])
                    break
        else:
            string = string[1:]
        
    for n in range(len(string)):
        for k in dnums:
            
            if string[::-1].startswith(k[::-1]):
                last_n = (dnums[k])
                break
            elif string[::-1].startswith(dnums[k]):
                    last_n = (dnums[k])
                    break
        else:
            string = string[:-1]
    
    coordinate = first_n + last_n
    return int(coordinate)

          
           

                          

lst = example.split('\n')   
for line in lst:
    print(convert(line))

            
        

    
                  
                 
                


 





      
      
            

            
          
    
        


       

    
       
 
         

    
      
        


    

    

    
    
    
     


        
             
        


        

#lst = example.split('\n')
#print(lst)

#for word in lst:

    
        

    


                      





        

  

    
 



