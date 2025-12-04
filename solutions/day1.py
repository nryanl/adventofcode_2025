#!/usr/bin/env python3
def day1():
    # Set initial dial position
    dial_pos = 50

    # The number of times we pass zero
    num_zeroes = 0

    # Process each turn
    f = open("inputs/day1.txt")
    for line in f:
        # Parse the magnitude of the turn
        num = int(line[1:])

        # Determine direction of dial turn
        match line[0]:
            case 'L':
                dial_pos -= num
            case 'R':
                dial_pos += num
        dial_pos %= 100

        # Check our current position
        if dial_pos == 0:
            num_zeroes += 1

    print(num_zeroes)

day1()
