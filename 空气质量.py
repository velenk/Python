pm = eval(input('请输入pm2.5的值:'))
def test(a):
    t = ''
    if a >=75:
        t += '污染，不宜'
    elif a >=35:
        t += '良好，适度'
    else:
        t += '优质，快去'
    return t
def main():
    t = test(pm)
    print('空气' + t + '户外活动')
main()
