import turtle as t
import time as ti
#import locale

def drawline(draw):
    drawGap()
    t.pendown() if draw else t.penup()
    t.fd(40)
    drawGap()
    t.right(90)

def drawGap():
    t.penup() 
    t.fd(5)

def drawDigit(digit):
    drawline(True) if digit in (2,3,4,5,6,8,9) else drawline(False)
    drawline(True) if digit in (0,1,3,4,5,6,7,8,9) else drawline(False)
    drawline(True) if digit in (0,2,3,5,6,8,9) else drawline(False)
    drawline(True) if digit in (0,2,6,8) else drawline(False)
    t.left(90)
    drawline(True) if digit in (0,4,5,6,8,9) else drawline(False)
    drawline(True) if digit in (0,2,3,5,6,7,8,9) else drawline(False)
    drawline(True) if digit in (0,1,2,3,4,7,8,9) else drawline(False)
    t.penup()
    t.left(180)
    t.fd(40)

def drawDate(date):
    t.pencolor("red")
    for i in date:
        if i == '-':
            t.write("年",font = ('Arial',18, "normal"))
            t.pencolor("green")
            t.fd(40)
        elif i == '=':
            t.write("月",font = ('Arial',18, "normal"))
            t.pencolor("blue")
            t.fd(40)
        elif i == '+':
            t.write("日",font = ('Arial',18,"normal"))
        else:
            drawDigit(eval(i))

def main():
    t.speed(0) #fastest:0 fast10 normal6 slow3 slowest1
    t.setup(1000,350,200,200)
    t.penup()
    t.fd(-400)
    t.pensize(5)
    
    #locale.setlocale(locale.LC_CTYPE,'chinese')
    #drawDate(ti.strftime("%Y年%m月%d日",ti.gmtime()))
    
    drawDate(ti.strftime("%Y-%m=%d+",ti.gmtime()))
    t.hideturtle() 
    t.done()

main()
