#文本数字显示

def main():
    num = get_num()
    display(num)

def get_num():
    while True:
        num = input('The Number:')
        if num:
            try:
                int(num)
                return num
            except:
                print('Error')
        else:
            exit()

def display(num):
    zero = ['###','#  #','#  #','#  #','###']
    one = ['    #','    #','    #','    #','    #']
    two = ['###','    #','###','#    ','###']
    three = ['###','    #','###','    #','###']
    four = ['#  #','#  #','###','    #','    #']
    five = ['###','#    ','###','    #','###']
    six = ['###','#    ','###','#  #','###']
    seven = ['###','    #','    #','    #','    #']
    eight = ['###','#  #','###','#  #','###']
    nine = ['###','#  #','###','    #','###']
    Digits = [zero, one, two, three, four, five, six, seven, eight, nine]
    space = ['    ','   ','  ',' ','']
    for row in range(5):
        line = space[row]
        for i in num:
            line = line + Digits[int(i)][row] + '    '
        print(line)

main()
