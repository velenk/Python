import random
from math import sqrt
from time import clock

def input_num():
    while True:
        try:
            a = int(input('number:'))
            return a
        except:
            print('error')

def if_pi():
    x, y = random.random(), random.random()
    a = False
    if sqrt(x ** 2 + y ** 2) <= 1:
        a = True
    return a

def main(num):
    hit = 0
    for i in range(num):
        c = if_pi()
        if c:
            hit += 1
    b = 4 * hit / num
    return b

num = input_num()
if num > 10000000:
    num = 10000000
clock()
print('Pi is {}'.format(main(num)))
print('cost time {}s'.format(clock()))
