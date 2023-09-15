def print_even_natural_numbers(N, current=2):
    if N > 0:
        print(current, end=' ')
        print_even_natural_numbers(N - 1, current + 2)
