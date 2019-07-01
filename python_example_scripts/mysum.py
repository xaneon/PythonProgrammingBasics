def funktion(n, m=1):
    if n == m:
        return m
    else:
        return n + funktion(n - 1, m)


# print mysum(5,2)
if __name__ == '__main__':
    print(funktion(3))
    print(funktion(3, 2))
