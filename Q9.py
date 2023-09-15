def print_cubes_of_natural_numbers(N, current=1):
    if N > 0:
        print(current ** 3, end=' ')
        print_cubes_of_natural_numbers(N - 1, current + 1)
