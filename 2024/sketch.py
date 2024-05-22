input = '''MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX'''


def check_vertically(lines_list):
    count = 0
    for i in range(len(lines_list)):
        # print(i)
        for j in range(len(lines_list[i])):
            # print(j)
            if i <= len(lines_list)-3:
                if lines_list[i][j] == 'X':
                    if lines_list[i+1][j] == 'M':
                        if lines_list[i+2][j] == 'A':
                            if lines_list[i+3][j] == 'S':
                                # print(i,j, '  ',i+1,j, '  ',i+2,j, '  ',i+3,j)
                                count += 1
            if i <= len(lines_list)+3:
                if lines_list[i][j] == 'X':
                    if lines_list[i-1][j] == 'M':
                        if lines_list[i-2][j] == 'A':
                            if lines_list[i-3][j] == 'S':
                                # print(i,j, '  ',i-1,j, '  ',i-2,j, '  ',i-3,j)
                                count += 1        
    return count
                    


def check_horizontally(lines_list):
    count = 0
    for i in range(len(lines_list)):
        # print(i)
        for j in range(len(lines_list[i])):
            # print(j)
            if j <= len(lines_list[i])-3:
                if lines_list[i][j] == 'X':
                    if lines_list[i][j+1] == 'M':
                        if lines_list[i][j+2] == 'A':
                            if lines_list[i][j+3] == 'S':
                                # print(i,j, '  ',i,j+1, '  ',i,j+2, '  ',i,j+3)
                                count += 1
            if j <= len(lines_list[i])+3:
                if lines_list[i][j] == 'X':
                    if lines_list[i][j-1] == 'M':
                        if lines_list[i][j-2] == 'A':
                            if lines_list[i][j-3] == 'S':
                                # print(i,j, '  ',i,j-1, '  ',i,j-2, '  ',i,j-3)
                                count += 1                     
    return count              
                    

def check_diagonally(lines_list):
    count = 0
    for i in range(len(lines_list)):
        for j in range(len(lines_list[i])):
            # right up diagonal
            if i < len(lines_list)-3 and j < len(lines_list[i])-3:
                if lines_list[i][j] == 'X':
                    if lines_list[i+1][j+1] == 'M':
                        if lines_list[i+2][j+2] == 'A':
                            if lines_list[i+3][j+3] == 'S':
                                print(i,j, '  ',i+1,j+1, '  ',i+2,j+2, '  ',i+3,j+3)
                                count += 1
            #left up diagonal
            if 0 < i < len(lines_list)-3 and 3 < j < len(lines_list[i])+3:
                if lines_list[i][j] == 'X':
                    if lines_list[i+1][j-1] == 'M':
                        if lines_list[i+2][j-2] == 'A':
                            if lines_list[i+3][j-3] == 'S':
                                
                                
                                print(i,j, '  ',i+1,j-1, '  ',i+2,j-2, '  ',i+3,j-3)
                                count += 1

                        
            #right down diagonal                     
            if i <= len(lines_list)+3 and j <= len(lines_list[i])-3:
                if lines_list[i][j] == 'X':
                    if lines_list[i-1][j+1] == 'M':
                        if lines_list[i-2][j+2] == 'A':
                            if lines_list[i-3][j+3] == 'S':
                                print(i,j, '  ',i-1,j+1, '  ',i-2,j+2, '  ',i-3,j+3)
                                count += 1
            #left down diagonal                     
            if j <= len(lines_list)+3 and j <= len(lines_list[i])+3:
                if lines_list[i][j] == 'X':
                    if lines_list[i-1][j-1] == 'M':
                        if lines_list[i-2][j-2] == 'A':
                            if lines_list[i-3][j-3] == 'S':
                                print(i,j, '  ',i-1,j-1, '  ',i-2,j-2, '  ',i-3,j-3)
                                count += 1
    return count                 
            

lines_list = input.split()

# v_xmases = check_vertically(lines_list)
# h_xmases = check_horizontally(lines_list)
# d_xmases = check_diagonally(lines_list)
# print(v_xmases, h_xmases, d_xmases)
print(lines_list[1])


                

            
            
                       
    
