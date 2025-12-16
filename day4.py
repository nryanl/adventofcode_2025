def day4_1():
    f = open("inputs/day4.txt")
    lines = f.read().strip().split('\n')

    grid = []
    acc = 0
    for line in lines:
        grid.append([])
        for char in line:
            grid[-1].append(char)


    row_len = len(grid[0])
    col_len = len(grid)

    while True:
        any_removed = False
        for row_i, row in enumerate(grid):
            for col_i, char in enumerate(row):
                if char == '@':
                    count = 0

                    # Count top 3
                    if row_i > 0:
                        # Count top left
                        if col_i > 0:
                            count += (grid[row_i-1][col_i-1] == '@')
                        # Count top
                        count += (grid[row_i-1][col_i] == '@')
                        # Count top right
                        if col_i < row_len - 1:
                            count += (grid[row_i-1][col_i+1] == '@')

                    # Count left and right
                    if col_i > 0:
                        count += (grid[row_i][col_i-1] == '@')
                    if col_i < row_len - 1:
                        count += (grid[row_i][col_i+1] == '@')

                    # Count bottom 3
                    if row_i < col_len - 1:
                        # Count bottom left
                        if col_i > 0:
                            count += (grid[row_i+1][col_i-1] == '@')
                        # Count bottom
                        count += (grid[row_i+1][col_i] == '@')
                        # Count bottom right
                        if col_i < row_len - 1:
                            count += (grid[row_i+1][col_i+1] == '@')
                    if count < 4:
                        grid[row_i][col_i] = 'x'
                        any_removed = True
                        acc += 1
        if not any_removed:
            break
    print(acc)
day4_1()
