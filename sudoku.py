from pprint import pprint

grid = [
    [0,0,0,0,0,0,0,0,0],
    [0,1,2,0,3,4,5,6,7],
    [0,3,4,5,0,6,1,8,2],
    [0,0,1,0,5,8,2,0,6],
    [0,0,8,6,0,0,0,0,1],
    [0,2,0,0,0,7,0,5,0],
    [0,0,3,7,0,5,0,2,8],
    [0,8,0,0,6,0,7,0,0],
    [2,0,7,0,8,3,6,1,5]
]
#first let's print sudoku before solving it.
pprint(grid)

#let's make function that checks if value given at position will be right or not.
#If value is valid at that position then it will return True else it will return False.
def possible(y,x,n):
    global grid
    for i in range(0,9):
        if grid[y][i] == n:
            return False
    for i in range(0,9):
        if grid[i][x] == n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j] == n:
                return False
    return True

#Let's check function is working or not.
#Let's see at position 4,4 can we put 6 or not
pprint(possible(4,4,6))

#Let's make function which will do backtracking. ( will use recursion also )
def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1,10):
                    if possible(y,x,n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    pprint(grid)

 #let's solve this sudoku
solve() 
