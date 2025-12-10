def day9_1():
    f = open("inputs/day9.txt")
    raws = f.read().strip().split('\n')
    pairs = [tuple(map(int, raw.split(','))) for raw in raws]

    max_a = -1
    for i in range(len(pairs)):
        for j in range(i+1, len(pairs)):
            a_1 = (abs(pairs[i][0] - pairs[j][0]) + 1) \
                * (abs(pairs[i][1] - pairs[j][1]) + 1)
            if a_1 > max_a:
                max_a = a_1
    print(max_a)

day9_1()
