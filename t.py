

import time


def timelevel(a: int, b: list):
    b.append(6)
    print("The a {}".format(a))
    print("The b {}".format(b))

if __name__ == "__main__":
    b=[4,5]
    print("The name is {} {}".format(__name__,timelevel(5, b)))
    print("The b is {}".format(b))