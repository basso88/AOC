input = "/Users/marco/Developer/advent_of_code/2025/day7/input.txt"
filehandl = open(input)
diagram = filehandl.read()
diagram_rows = diagram.split()

diagram_list= []

for row in diagram_rows:
    ch_list = []
    for ch in row:
        ch_list.append(ch)
    diagram_list.append(ch_list)

path_count = 0

for i in range(len(diagram_list)):
    for j in range(len(diagram_list[0])):

        if i+1 < len(diagram_list) and j+1 < len(diagram_list[0]) and j-1 >= 0:
            
            if diagram_list[i][j] == 'S':
                diagram_list[i+1][j] = 1

            if isinstance(diagram_list[i][j], int):
                if diagram_list[i+1][j] == '.':
                    diagram_list[i+1][j] = diagram_list[i][j]

            if diagram_list[i][j] == '^':

                # go to the left
                if isinstance(diagram_list[i-1][j], int):
                    if isinstance(diagram_list[i][j-1], int):
                        diagram_list[i][j-1] += diagram_list[i-1][j]
                        diagram_list[i+1][j-1] = diagram_list[i][j-1]
                    else:
                        diagram_list[i][j-1] = diagram_list[i-1][j]
                        diagram_list[i+1][j-1] = diagram_list[i-1][j]

                #go to the right
                if isinstance(diagram_list[i-1][j], int):
                    if isinstance(diagram_list[i][j+1], int):
                        diagram_list[i][j+1] += diagram_list[i-1][j]
                        diagram_list[i+1][j+1] = diagram_list[i][j+1]                
                    else:
                        diagram_list[i][j+1] = diagram_list[i-1][j]
                        diagram_list[i+1][j+1] = diagram_list[i-1][j]


for ch in diagram_list[-1]:
    if not ch == ".":
        path_count += ch

print(path_count)

