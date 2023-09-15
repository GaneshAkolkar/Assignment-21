def print_odd_natural_numbers_reverse(N, current):
    if N > 0:
        if current % 2 == 1:
            print_odd_natural_numbers_reverse(N - 1, current - 2)
            print(current, end=' ')
        else:
            print_odd_natural_numbers_reverse(N, current - 1)
