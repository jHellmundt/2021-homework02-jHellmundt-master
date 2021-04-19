""" Script that finds the first Fibonacci number that has a digit sum higher than 42. """

from fibonacci import fibonacci
from digsum import digsum

def main():

    print("findfib() returns", findfib())


def findfib():
    """ This function returns the first Fibonacci number that has a digit sum higher than 42. """

    n = 0

    # I know its kind of messy
    while True:
        fibo = fibonacci(n)
        if digsum(fibo) >= 42:
            return fibo
        n += 1

if __name__ == "__main__":
    main()
