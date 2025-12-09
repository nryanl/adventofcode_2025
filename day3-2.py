def day3_2():
    f = open("inputs/day3.txt")
    banks = f.read().strip().split('\n')

    # monotonic stack pattern
    acc = 0
    for bank in banks:
        k = len(bank) - 12
        stack = []
        remaining = 12

        for digit in bank:
            while k > 0 and stack and stack[-1] < digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        acc += int(''.join(stack[:remaining]).lstrip('0'))

    print(acc)
day3_2()
