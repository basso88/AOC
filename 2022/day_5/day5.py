class Crate:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        
    def __str__(self):
        return f'{self.name}: {self.x},{self.y}'
    

def crates_stack(crates_list, x):       # takes in the list of all crates and the x coordinate and returns a list of the crates of that coordinate
    crates_stack = []
    for crate in crates_list:
        if crate.x == x:
            crates_stack.append(crate)
    return crates_stack


def sort_by_y(crates_list):     # takes in the list of crates objects and sorts them by their y attribute 
    return sorted(crates_list, reverse=True, key=lambda crate: crate.y)


    #takes in a list of a stack of crates on a x coordinated and the num of wanted crates, and returns a list of those crates
def wanted_crates(crates_stack, crates_number=int):
    selected_crates = []
    count = 0
    for crate in sort_by_y(crates_stack[-(crates_number):]):
        crate.y = crates_number - count
        selected_crates.append(crate)
        count += 1
    return selected_crates



# def move_crates


    



input = 'input.txt'
fhandle = open(input)

lines = fhandle.readlines()

crates_list = []

for i, line in enumerate(reversed(lines[:9])):
    y = i
    for j, ch in enumerate(line):
        x = lines[8][j]
        if ch in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K' ,'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'W', 'X', 'Y', 'Z']:
            c = Crate(ch, int(x), y)
            crates_list.append(c)
    
            

new_crates_list = crates_list
for line in lines[:11]:
    if line.startswith('move'):
        line_list = line.split()
        crates_number = int(line_list[1])
        current_x_position = int(line_list[3])
        new_x_position = int(line_list[5])
        # print(crates_number, current_y, new_y)

        
        
        stack = crates_stack(new_crates_list, current_x_position)
        crates_to_move = wanted_crates(stack, crates_number)
        wanted_new_position = crates_stack(crates_list, new_x_position)
        for cr in crates_to_move:
            cr.x = new_x_position
            try:
                cr.y += (sort_by_y(wanted_new_position)[0]).y
            except:
                cr.y 
            # new_crates_list.append(cr)
            # print(cr)
        
        # new_crates_list.remove(crates_to_move)
# print(new_crates_list)

for n in range(1, 10):
    for c in sort_by_y(crates_stack(new_crates_list, n)):
        print(c)
    
print('\n\n')

for n in range(1,10):
    print(sort_by_y(crates_stack(new_crates_list, n))[0])