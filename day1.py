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

        # Calculate old and new position
        old_pos = dial_pos
        new_pos_no_mod = dial_pos + num if line[0] == 'R' else dial_pos - num

        # Calculate number of wraps
        # new_pos_no_mod >= 100                (wrap on first rotation)
        # new_pos_no_mod <  0 and old_pos > 0  (wrap on first rotation)
        # new_pos_no_mod <  0 and old_pos == 0 (no wrap on first rotation)
        # new_pos_no_mod == 0                  (no wrap, we landed exactly on 0)
        match [old_pos, new_pos_no_mod]:
            case _ if new_pos_no_mod >= 100:
                # WRAP RIGHT (from ZERO or POSITIVE)
                # cross 0 at 100, 200, 300, ...
                num_zeroes += new_pos_no_mod // 100
            case _ if new_pos_no_mod < 0 and old_pos > 0:
                # WRAP LEFT (from STRICTLY POSITIVE)
                # cross at 0, then count additional wraps
                num_zeroes += 1 + ((-new_pos_no_mod) // 100)
            case _ if new_pos_no_mod < 0 and old_pos == 0:
                # WRAP LEFT (from ZERO): only count additional wraps
                num_zeroes += (-new_pos_no_mod) // 100
            case _ if new_pos_no_mod == 0:
                # If this case is hit, there's no wrap and we landed exactly on zero.
                num_zeroes += 1

        # Set new dial position
        dial_pos = new_pos_no_mod % 100

    print(num_zeroes)

day1()
