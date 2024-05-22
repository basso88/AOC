
#Dice configuration:
my_set_of_dice = {'red':12, 'green':13, 'blue':14}

#opening the file input

file = 'cube_game.txt'
input = open(file)

#create a funtion that transfors each list in a list of dictionaries

def game_data_struct(lst):

    extractions = list()
    

    results= lst[1].strip()
    results= results.split(';')

    for result in results:
        result = result.strip()
        pair = result.split(',')

        #create a new dictionay for each result
        d=dict()

        for dice in pair:
            ldice = dice.split()
            #print(ldice)
            d[ldice[1]] = d.get(ldice[1], int(ldice[0]))
        extractions.append(d)
        
    return extractions

               
possible = [] #set the list where possible games will be appended (solution part one)
power = []    #set a list where the power of the best value of dice for each game will be appended (solution part two)

#create a list for each game
for lines in input:
    extractions = []
    lines = lines.strip()
    games = lines.split(':')
    lgames = games[0].split()
    game_id = int(lgames[1])
    #print('game ID', game_id)
    #use the function to create a dictionary for every extractios of dice of each game
    games_dict = game_data_struct(games)
    extractions.append(games_dict)


    for extraction in extractions:
        #create a list of boolean value for each extraction of dice in the game: True if the extraction is possible, esle: False
        bool_val = []
        best_dice = {}
        for game in extraction:
            #create a key in the dictionary (dice color) with value = 0 if the color that is not in the dictionary
            for k in my_set_of_dice:
                if not k in game:
                    game[k] = 0

            
            if game['blue'] <= my_set_of_dice['blue'] and game['red'] <= my_set_of_dice['red'] and game['green'] <= my_set_of_dice['green']:
                res = True
                bool_val.append(res)
            else:
                res= False
                bool_val.append(res)

#---------------------------------- *** Part two logic *** -------------------------------------- #
                
            for k in game:
                if not k in best_dice:
                    best_dice[k] = game[k]
                elif game[k] > best_dice[k]:
                    best_dice[k] = game[k]

        print(best_dice)
        pow = 1
        for col in best_dice:
            if best_dice[col] == 0:
                continue
                
            pow = pow * best_dice[col]
        power.append(pow)   
           
            
# ---------------------------------------------------------------------------------------------------- #  
                

        if not False in bool_val:
            possible.append(game_id)


#sum all the "possible" game IDs (solution part one)

#print(possible)
tot = 0
for id in possible:
  tot += id
  
print(tot)


tot_pow = 0
for pow in power:
    tot_pow += pow

print(tot_pow)
        




        


        