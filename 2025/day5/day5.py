input = "/Users/marco/Developer/advent_of_code/2025/day5/input.txt"
fhandl = open(input)
database = fhandl.read()
database = database.split()

range_ids = [x for x in database if "-" in x]
ingredient_ids = [x for x in database if "-" not in x]

fresh_ingredients = []
for ing_id in ingredient_ids:
    for range_id in range_ids:
        part = range_id.split("-")
        i = int(part[0])
        e = int(part[1])
        if i <= int(ing_id) <= e:
            if int(ing_id) in fresh_ingredients:
                continue
            else:
                fresh_ingredients.append(int(ing_id))
            
            
print(len(fresh_ingredients))

# fresh_ids = []

# for range_id in range_ids[:1]:
#     part = range_id.split("-")
#     i = int(part[0])
#     e = int(part[1])
#     for id in range(i, e+1):
#         if int(id) in fresh_ids:
#             continue
#         else:
#             fresh_ids.append(id)

# print(len(fresh_ids))


