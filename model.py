from random import randint
from time import sleep
import curses
import atexit

def exit_handler():
    curses.endwin()

atexit.register(exit_handler)
console = curses.initscr()

SIZE = 60
NUM_INIT = 300
MIN_DIST = 2

grid = [['.' for i in range(SIZE)] for j in range(SIZE)]

def print_grid(grid):
    console.clear()
    for i, line in enumerate(grid):
        console.addstr(i, 0, ''.join(line))
        #print(''.join(line))
    console.refresh()

def init():
    for _ in range(NUM_INIT):
        i, j = randint(0, SIZE-1), randint(0, SIZE-1)
        sex = randint(0, 1)
        grid[i][j] = 'M' if sex == 0 else 'F'

def step():
    count_M, count_F, count_NO = 0, 0, 0

    for i in range(SIZE):
        for j in range(SIZE):
            if grid[i][j]=='.':
                count_NO += 1
            else:

                if grid[i][j]=='M':
                    count_M += 1
                else:
                    count_F += 1
                rand = randint(0, 10)
                if rand<=2:
                    grid[i][j] ='.'
                replication(i,j)
    return count_M, count_F, count_NO


def replication(pos_i, pos_j):
    s = grid[pos_i][pos_j]
    for i in range(max(0,pos_i-MIN_DIST), min(SIZE,pos_i+MIN_DIST+1)):
        for j in range(max(0,pos_j-MIN_DIST), min(SIZE,pos_j+MIN_DIST+1)):
            if i!= pos_i and j!=pos_j:
                if s != grid[i][j]:
                    create_prob = randint(0,20)
                    if create_prob <= 2:
                        a, b = randint(0, SIZE-1), randint(0, SIZE-1)
                        sex = randint(0, 1)
                        grid[a][b] = 'M' if sex == 0 else 'F'

init()
print_grid(grid)
for i in range(100):
    m,f, no = step()
    print_grid(grid)
    s = 'M: ' + str(m) + ' F: ' + str(f) + ' NO: '+ str(no) + ' TIME:' + str(i)
    console.addstr(SIZE+1, 0, s)
    console.refresh()
    sleep(0.5)
curses.endwin()
