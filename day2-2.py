#!/usr/bin/env python3

def divisors(n: int) -> list[int]:
    factors = {1}
    max_p  = int(n ** 0.5)
    p, inc = 2,1
    while p <= max_p:
        while n % p==0:
            factors.update([f * p for f in factors])
            n //= p
            max_p = int(n**0.5)
        p, inc = p + inc, 2
    if n > 1:
        factors.update([f * n for f in factors])

    return sorted(factors)


def day2():
    # Parse ID ranges into a list
    ## Open file
    f = open("inputs/day2.txt")

    ## Stringify, split into list
    ranges = f.read().strip().split(",")

    # For each range, run a multiple pointer algorithm
    # to find repeating sequences.
    #
    # 1. Parse the range into `lower` and `upper`
    # 2. For each number in the range:
    #    a. convert to string `candidate_str`
    #    b. For each divisor `d` of `n = len(candidate_str)`,
    #       i.  Initialize the pattern string of the first n/d
    #           characters
    #       ii. Check if it repeats
    acc = 0
    divisors_of = []
    for r in ranges:
        [lower, upper] = map(int, r.split("-"))
        for candidate in range(lower, upper + 1):
            # Convert to string
            candidate_string = str(candidate)
            n = len(candidate_string)

            # If we have not computed the divisors of n, add them to divisors_of
            # This memoizes the divisors of a given length
            if len(divisors_of) < n:
                for i in range (len(divisors_of), n + 1):
                    divisors_of.append(divisors(i))

            for d in divisors_of[n]:
                match d:
                    case _ if d == n:
                        continue
                    case _ if d > 1:
                        chunks = [candidate_string[i:i+d] for i in range(0, len(candidate_string), d)]
                        if all(chunk == chunks[0] for chunk in chunks[1:]):
                            acc += candidate
                            break
                    case 1:
                        c = candidate_string[0]
                        if all(x == c for x in candidate_string):
                            acc += candidate
                            break
    print(acc)

day2()
