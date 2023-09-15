def print_even_natural_numbers_reverse(N, current):
    if N > 0:
        print_even_natural_numbers_reverse(N - 1, current - 2)
        print(current, end=' ')
