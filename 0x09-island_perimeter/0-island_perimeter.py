#!/usr/bin/python3

def island_perimeter(grid):
    ''' Calculates the primater of the land perimeter in the grid

    Args:
        grid(2D list): 2d array
    Returns:
        (int): perimarer of land
    '''
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    def is_outside_or_water(i, j):
        """ Checks if the nebouring area is land or water or outside
        Args:
            (i, j): location in 2d array
        Retrun:
            bool: true if water or outide else if it is land false
        """
        # check if the neibouring location is outside
        # if it is return true
        if (i < 0 or i >= rows or j < 0 or j >= cols):
            return True
        # other wise check if its water
        # if is return true
        return grid[i][j] == 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                if is_outside_or_water(i - 1, j):  # left side
                    perimeter += 1
                if is_outside_or_water(i + 1, j):  # Right side
                    perimeter += 1
                if is_outside_or_water(i, j + 1):  # up
                    perimeter += 1
                if is_outside_or_water(i, j - 1):  # down
                    perimeter += 1
    # return the final perimeter
    return perimeter
