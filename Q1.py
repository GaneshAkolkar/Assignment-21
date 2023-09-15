def print_natural_numbers(N):
    if N > 0:
        print_natural_numbers(N - 1)
        print(N, end=' ')
