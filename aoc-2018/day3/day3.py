import sys

lines = open(sys.argv[1]).readlines()
n = 1000
grid = [[0 for _ in range(n)] for _ in range(n)]
square_inches = 0

def day3():
    count = 0
    for claim in lines:
        indices = claim.split()[2].split(',')
        lengths = claim.split()[3].split('x')
        i, j = map(int, [indices[0], indices[1][:-1]])
        length_x, length_y = map(int, [lengths[0], lengths[1]])
        for x in range(length_x):
            for y in range(length_y):
                if grid[i + x][j + y] < 2:
                    grid[i + x][j + y] += 1
                    if grid[i + x][j + y] == 2:
                        count += 1
    
    for claim in lines:
        claim_id = claim.split()[0][1:]
        indices = claim.split()[2].split(',')
        lengths = claim.split()[3].split('x')
        i, j = map(int, [indices[0], indices[1][:-1]])
        length_x, length_y = map(int, [lengths[0], lengths[1]])
        prod = 1
        for x in range(length_x):
            for y in range(length_y):
                prod *= grid[i + x][j + y]
        if prod == 1:
            print(claim_id)
        
    return count

print(day3())
