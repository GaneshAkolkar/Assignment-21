def print_multiples_of_number(N, num, current=1):
    if N > 0:
        print(num * current, end=' ')
        print_multiples_of_number(N - 1, num, current + 1)
