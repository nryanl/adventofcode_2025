def day3_1():
    f = open("inputs/day3.txt")
    banks = f.read().strip().split('\n')


    # Iterate once over the bank. If at any point we find a new max_1,
    # set max_2 to the number to the right and continue.
    # The objective is to find the biggest first digit
    # and biggest second digit
    acc = 0
    for bank in banks:
        max_1 = -1
        max_2 = -1

        n = len(bank)
        for i in range(0, n):
            bat = int(bank[i])
            if i != n - 1:
                print(bat, end="")
            if i != n - 1 and bat > max_1:
                max_1 = bat
                max_2 = int(bank[i+1])
                continue
            if bat > max_2:
                max_2 = bat



        print((max_1 * 10) + max_2)
        acc += (max_1 * 10) + max_2

    print(acc)

day3_1()
