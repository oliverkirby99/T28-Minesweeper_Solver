# used for generating random minesweeper grid
import random

# Create a list for each row
row_0 = []
row_1 = []
row_2 = []
row_3 = []
row_4 = []

# Create a 2D List containing the 5 rows
grid = [row_0, row_1, row_2, row_3, row_4]

# For each row in the grid, get a value of 0/1 until each row has 5 values.
# 0s = # and 1s = -
for row in grid:
    while len(row) < 5:
        value = random.randrange(0, 2)
        if value == 1:
            row.append("#")
        else:
            row.append("-")

# Print out the randomly generated grid
print(f"       --- GRID ---\n")
for row in grid:
    print(row)

input("\nPress enter to see the result...\n")

# Convert all "-" into a 0
for row in grid:
    pos = 0
    for value in row:
        if value == "-":
            row[pos] = 0
        pos += 1

# Define the starting position
current_row = 0
current_col = 0
current_pos = [current_row, current_col]


# Function used to +1 all positions around a "#"
def change_surrounding_values(current_row, current_col):
    # Define all 8 positions around current position
    # North
    nw_pos = [current_row - 1, current_col - 1]
    n_pos = [current_row - 1, current_col]
    ne_pos = [current_row - 1, current_col + 1]
    # equal
    w_pos = [current_row, current_col - 1]
    e_pos = [current_row, current_col + 1]
    # South
    sw_pos = [current_row + 1, current_col - 1]
    s_pos = [current_row + 1, current_col]
    se_pos = [current_row + 1, current_col + 1]

    # By using try, it should avoid any out of range errors
    try:
        if current_col > 0 and current_row > 0:
            grid[nw_pos[0]][nw_pos[1]] += 1
    except:
        pass
    try:
        if current_row > 0:
            grid[n_pos[0]][n_pos[1]] += 1
    except:
        pass
    try:
        if current_col < 4 and current_row > 0:
            grid[ne_pos[0]][ne_pos[1]] += 1
    except:
        pass
    try:
        if current_col > 0:
            grid[w_pos[0]][w_pos[1]] += 1
    except:
        pass
    try:
        if current_col < 4:
            grid[e_pos[0]][e_pos[1]] += 1
    except:
        pass
    try:
        if current_row < 4 and current_col > 0:
            grid[sw_pos[0]][sw_pos[1]] += 1
    except:
        pass
    try:
        if current_row < 4:
            grid[s_pos[0]][s_pos[1]] += 1
    except:
        pass
    try:
        if current_row < 4 and current_col < 4:
            grid[se_pos[0]][se_pos[1]] += 1
    except:
        pass


for row in range(len(grid)):
    for value in grid[row]:
        if value == "#":  # Each # will trigger all values around it to +1 in value
            change_surrounding_values(current_row, current_col)
        else:
            pass
        current_col += 1  # Update current position
    current_row += 1  # Update current position
    current_col = 0  # Update current position

for row in grid:
    pos = 0
    for value in row:  # Convert all int into str
        row[pos] = str(value)
        pos += 1
    print(row)

input("Done!")