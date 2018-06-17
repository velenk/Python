import turtle as t

def main():
    num = input_msg()
    start()
    for i in range(3):
        draw(num, 600)
        t.right(120)

def input_msg():
    while True:
        msg = input('The Koch Number:')
        if msg:
            try:
                num = int(msg)
                if num > 5:
                    num = 5
                if num < 1:
                    num = 1
                return num
            except:
                print('Error')
        else:
            break

def start():
    t.setup(1200, 1200, 0, 0)
    t.pensize(3)
    t.pencolor('blue')
    t.speed(100)
    t.up()
    t.left(90)
    t.fd(200)
    t.right(90)
    t.fd(-500)
    t.down()

def draw(a, s):
    if a == 0:
        t.fd(s)
    else:
        for angle in [0, 60, -120, 60]:
            t.left(angle)
            draw(a-1, s/3)

main()
