def monkey(n):
    peach = 1
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return 2 * monkey(n-1) + 2
    
