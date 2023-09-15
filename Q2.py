def print_natural_numbers_reverse(N):
    if N > 0:
        print(N, end=' ')
        print_natural_numbers_reverse(N - 1)
