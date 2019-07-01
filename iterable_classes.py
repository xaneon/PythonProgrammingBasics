class Fibonacci:
    def __init__(self, maximum):
        self.maximum = maximum

    def __iter__(self):
        self.linkezahl = 0
        self.rechtezahl = 1
        return self

    def __next__(self):
        fib = self.linkezahl
        if fib > self.maximum:
            raise StopIteration
        (self.linkezahl,
         self.rechtezahl) = (self.rechtezahl,
                             self.linkezahl +
                             self.rechtezahl)
        return fib

fib_bis_100 = Fibonacci(100)
print(type(fib_bis_100), list(fib_bis_100),
      [fib for fib in fib_bis_100])
fib_bis_200 = iter(Fibonacci(200))
print(next(fib_bis_200), next(fib_bis_200))

menge = {1,2,3}
iterator_m = iter(menge)
try:
    print(next(iterator_m), next(menge))
except TypeError as err:
    print(err)
