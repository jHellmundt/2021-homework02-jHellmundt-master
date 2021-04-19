""" Script that provides Fibonacci functionality. """

def main():

    print("fibonacci(0) =", fibonacci(0))
    print("fibonacci(3) =", fibonacci(3))
    print("fibonacci(10) =", fibonacci(10))

fibo_memory = {}

def fibonacci(n):
    """ This function returns the nth Fibonacci number given that fibonacci(0) = 0. """
    if n in fibo_memory.keys():
        return fibo_memory[n]
    
    if n > 1:
        fibo = fibonacci(n-1) + fibonacci(n-2)
    else:
        fibo = n

    fibo_memory[n] = fibo
    return fibo


if __name__ == "__main__":
    main()
