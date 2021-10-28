import numpy


def func1():
    speed = [99, 86, 87, 88, 86, 103, 87, 94, 78, 77, 85, 86]
    x = numpy.median(speed)
    return x


def func2():
    ages = [5, 31, 43, 48, 50, 41, 7, 11, 15, 39, 80, 82, 32, 2, 8, 6, 25, 36, 27, 61, 31]
    x = numpy.percentile(ages, 75)
    print(x)
    return x


def add(x,y):
    return x+y

def product (x,y=2):
    return x * y
