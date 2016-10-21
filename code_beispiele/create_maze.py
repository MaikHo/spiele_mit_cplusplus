
import random

def create_grid_string(dots, xsize, ysize):
    """
    Creates a grid of size (xx, yy) 
    with the given positions of dots.
    """
    grid = ""
    for y in range(ysize):
        for x in range(xsize):
            grid += "." if (x, y) in dots else "#"
        grid += "\n"
    return grid


def get_all_dot_positions(xsize, ysize):
    """Returns a list of (x, y) tuples covering all positions in a grid"""
    return [(x,y) for x in range(1, xsize-1) for y in range(1, ysize-1)]


def get_neighbors(x, y):
    """Returns a list with the 8 neighbor positions of (x, y)"""
    return [
        (x, y-1), (x, y+1), (x-1, y), (x+1, y),
        (x-1, y-1), (x+1, y-1), (x-1, y+1), (x+1, y+1)
        ]

def create_maze(xsize, ysize):
    """Returns a xsize*ysize maze as a string"""
    positions = get_all_dot_positions(xsize, ysize)
    dots = set()
    while positions != []:
        x, y = random.choice(positions)
        neighbors = get_neighbors(x, y)
        free = [nb in dots for nb in neighbors]
        if free.count(True) < 5:
            dots.add((x, y))
        positions.remove((x, y))
    maze = create_grid_string(dots, xsize, ysize)
    return maze

print(create_maze(12, 12))
