def count(a, b):
    bmi = b / pow(a, 2)
    if bmi < 18.5:
        who, dom = '偏瘦', '偏瘦'
    elif bmi < 24:
        who, dom = '正常', '正常'
    elif bmi < 25:
        who, dom = '正常', '偏胖'
    elif bmi < 28:
        who, dom = '偏胖', '偏胖'
    elif bmi < 30:
        who, dom = '偏胖', '肥胖'
    else:
        who, dom = '肥胖', '肥胖'
    return bmi, who, dom
def main():
    height, weight = eval(input('请输入身高(m)\
和体重(kg)[逗号隔开]:'))
    a = count(height, weight)
    print('BMI数值为:{:.2f}'.format(a[0]) + '\nBMI指标为:国际{},国内{}'.format(a[1], a[2]))
main()
