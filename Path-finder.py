import curses
from curses import wrapper
import queue
import time

# maze for finding path.
maze = [
    ["#", "#", "#", "#", "#", "#", "#", "O", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]

# Function for printing the Maze.
def Print_Maze(maze, stdscr, path = []):
    # assiging colors
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)

    # printin the maze
    for i,row in enumerate(maze):
        for j,value in enumerate(row):
            if (i,j) in path:
                stdscr.addstr(i, j*2, "X", RED)
            
            else:
                stdscr.addstr(i, j*2, value, BLUE)


# function for finding the starting point on the maze.
def Find_start(maze, start_point):
    for i,row in enumerate(maze):
        for j,value in enumerate(row):
            if value == start_point:
                return (i,j)
    return None

# Function going to return the valid neigbhors of current position.
def get_neigbhors(row, col, maze):
    pos = [-1, 0, 1, 0, -1]
    neigbhors = []
    n = len(maze)
    m = len(maze[0])
    for i in range(len(pos)-1):
        r, c = row + pos[i], col + pos[i+1]
        # condition for checking wheather the neigbhor is valid or not.
        if(r >= 0 and r < n and c >= 0 and c < m and maze[r][c] != "#"):
            neigbhors.append((r,c))
    return neigbhors


# Function for finding the shortest path using BFS.
def Find_path(stdscr, maze):

    # set which will store the visited positions.
    visited = set()

    # starting and ending point in the maze.
    start_point = "O"
    end_point = "X"

    # getting the co-ordinates of start point.
    start = Find_start(maze,start_point)
    visited.add(start)

    # queue for BFS.
    q = queue.Queue()
    q.put([start])

    while not q.empty():
        path = q.get()
        row, col = path[-1]

        # Printing Maze with the paths getting while doing BFS.
        stdscr.clear()
        Print_Maze(maze, stdscr, path)
        time.sleep(0.5)
        stdscr.refresh()
        
        # Checking wheather we reached to the end point or not.
        if maze[row][col] == end_point:
            return

        # adding the new paths in the queue.
        neigbhors = get_neigbhors(row, col, maze)
        for neigbhor in neigbhors:
            # checking wheather the neigbhor is already visited or not.
            if neigbhor in visited:
                continue
            
            # updating path
            new_path = path+[neigbhor]
            q.put(new_path)
            visited.add(neigbhor)


def main(stdscr):
    # intializing the colours
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    Find_path(stdscr, maze)
    stdscr.getch()

if __name__ == "__main__":
    wrapper(main)