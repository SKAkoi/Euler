def bigfib(n):
    last_two = 0
    last = 1
    current = 1
    total = 0
    while current < n:
        last_two = last
        last = current
        current = last + last_two
        print(str(current) + " = " + str(last) + " + " + str(last_two))
        if current % 2 == 0:
            total += current
    return total
