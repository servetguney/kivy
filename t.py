

import time


def timelevel(a: int, b: list):
    b.append(6)
    print("The a {}".format(a))
    print("The b {}".format(b))

def leastlevel(name:str):
    print("The name is {}".format(name))

if __name__ == "__main__":
    b=[4,5]
    print("The name is {} {}".format(__name__,timelevel(5, b)))
    print("The b is {}".format(b))
