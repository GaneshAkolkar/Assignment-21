def print_squares_of_natural_numbers(N, current=1):
    if N > 0:
        print(current ** 2, end=' ')
        print_squares_of_natural_numbers(N - 1, current + 1)
