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

def if_e():
    a = True
    string = '0123456789'
    for i in range(10):
        n = len(string)
        x = random.randint(0, n-1)
        if i == int(string[x]):
            a = False
            return a
        string = string[:x] + string[x+1:]
    return a

def main(num):
    hit = 0
    for i in range(num):
        c = if_e()
        if c:
            hit += 1
    e = num / hit
    return e

num = input_num()
if num > 100000:
    num = 100000
clock()
print('e is {}'.format(main(num)))
print('cost time {}s'.format(clock()))
