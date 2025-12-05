#!/usr/bin/env python3
def day2():
    # Parse ID ranges into a list
    ## Open file
    f = open("inputs/day2.txt")

    ## Stringify, split into list
    ranges = f.read().strip().split(",")

    # For each range, run a double pointer algorithm to find
    # repeating sequences.
    #
    # 1. Parse the range into `lower` and `upper`
    # 2. For each number in the range, convert to string `int_str`
    # 3. Initialize `p1` to int_str[0] and `p2` to int_str[n / 2],
    #    where n is the length of the string
    # 4. Compare char by char. Break if a mismatch is hit,
    #    add to accumulator otherwise
    #
    # Note: We only need to check numbers with digit lengths `d` that satisfy:
    #       d >= 2         (Numbers two digits or more)
    #       d %  2 == 0    (Numbers of even length digits)
    # This is a consequence of the repeating sequence invariant; If a sequence
    # `s` repeats, then the original number must be of length 2s.
    acc = 0
    for r in ranges:
        [lower, upper] = map(int, r.split("-"))
        for candidate in range(lower, upper + 1):
            # Convert to string
            candidate_string = str(candidate)
            n = len(candidate_string)

            # Skip valid IDs, see note
            if not (n >= 2 and n % 2 == 0):
                continue

            # Initialize two pointers
            p1 = candidate_string[0]
            p2 = candidate_string[n//2]

            # Loop until mismatch
            j = 0
            while p1 == p2:
                j += 1
                next1 = 0 + j
                next2 = n//2 + j

                # Success condition
                # If we reach the end of the string and no mismatch
                # is found, we have an invalid ID.
                if next2 >= n:
                    acc += candidate
                    break

                # Advance pointers
                p1 = candidate_string[next1]
                p2 = candidate_string[next2]
    print(acc)

day2()
