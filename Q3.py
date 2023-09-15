def print_odd_natural_numbers(N, current=1):
    if N > 0:
        if current % 2 == 1:
            print(current, end=' ')
            print_odd_natural_numbers(N - 1, current + 2)
        else:
            print_odd_natural_numbers(N, current + 1)
