""" Script that provides digit sum functionality. """

def main():

    print("digsum(0) =", digsum(0))
    print("digsum(12) =", digsum(12))
    print("digsum(333) =", digsum(333))
    print("digsum(9173) =", digsum(9173))


def digsum(number):
    """ This function returns the digit sum of a given int number. """
    return sum([int(x) for x in str(number)])


if __name__ == "__main__":
    main()
