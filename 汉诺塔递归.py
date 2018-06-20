#汉诺塔递归
def main():
    num = get_num()
    move(num, 'A', 'B', 'C')

def get_num():
    while True:
        msg = input('The Layer Number:')
        if msg:
            try:
                num = int(msg)
                if num < 1:
                    num = 1
                elif num >10:
                    num = 10
                return num
            except:
                print('Error')
        else:
            exit()

def move(num, a, b, c):
    if num == 1:
        print(str(a) + ' to ' + str(c))
    else:
        move(num-1, a, c, b)
        print(str(a) + ' to ' + str(c))
        move(num-1, b, a, c)

main()
