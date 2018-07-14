import turtle as t

def main():
    msg = input_msg()
    t.setup(800, 400, 200, 200)
    t.penup()
    t.fd(-340)
    t.pensize(5)
    t.pencolor('purple')
    for i in msg:
        Draw(i)

def input_msg():
    while True:
        s = input('The number needed to display:')
        if s:
            try:
                x = int(s)
                return s
            except:
                print('Error')
        else:
            exit()

def draw(a):
    t.fd(5)
    if a:
        t.pendown()
    t.fd(40)
    t.penup()
    t.fd(5)
    t.right(90)

def Draw(s):
    s = int(s)
    draw(True) if s in [2, 3, 4, 5, 6, 8, 9] else draw(0)
    draw(True) if s in [0, 1, 3, 4, 5, 6, 7, 8, 9] else draw(0)
    draw(True) if s in [0, 2, 3, 5, 6, 8, 9] else draw(0)
    draw(True) if s in [0, 2, 6, 8] else draw(0)
    t.left(90)
    draw(True) if s in [0, 4, 5, 6, 8, 9] else draw(0)
    draw(True) if s in [0, 2, 3, 5, 6, 7, 8, 9] else draw(0)
    draw(True) if s in [0, 1, 2, 3, 4, 7, 8, 9] else draw(0)
    t.right(180)
    t.fd(20)

main()
