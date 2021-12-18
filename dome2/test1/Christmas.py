import turtle as t
from turtle import *
import random as r
#小董-------小董
#小董-------小董
#小董-------小董
n = 100.0
speed("fastest") #定义速度
screensize(bg='black')  #定义背景颜色
left(90)
forward(3*n)
color("orange","yellow")    #定义星星颜色，外圈为orange，内圈为yellow
begin_fill()
left(126)
#五角星图形
for i in range(5):
    forward(n/5)
    right(144)  # 五角星的角度
    forward(n/5)
    left(72)    #五角星换边(换角度)
end_fill()
right(126)
#圣诞树上的小彩灯
def drawlight():
    #通过随机数生成彩灯，如果彩灯过多可以增大取值范围
    if r.randint(0,30) == 0:
        color('red')     #定义彩灯颜色
        circle(6)   #定义彩灯大小
    else:
        color('dark green') #随机数以外的彩灯全部在下面的空树枝
color("dark green")     #定义树枝颜色
backward(n*4.8)
#画树
def tree(d,s):
    if d <= 0:return
    forward(s)
    tree(d-1,s*.8)
    right(120)
    tree(d-3,s*.5)
    drawlight() #调用彩灯的方法
    right(120)
    tree(d-3,s*.5)
    right(120)
    backward(s)
tree(15,n)
backward(n/2)

#循环画最底层的装饰物
for i in range(120):
    a = 200 - 400 * r.random()
    b = 10 - 20 * r.random()
    up()
    forward(b)
    left(90)
    forward(a)
    down()
    if r.randint(0,1) == 0:
        color('tomato')
    else:
        color('wheat')
    circle(2)
    up()
    backward(a)
    right(90)
    backward(b)
t.color('dark red','red')   #定义字体颜色
t.write("Merry Christmas",align="center",font=("comic sans ms",40,"bold"))
#定义文字、位置、字体、大小
#雪花函数
def drawanow():
    t.ht()  #隐藏笔头
    t.pensize(2)    #定义笔头大小
    for i in range(200):    #画多少雪花
        t.pencolor("write") #定义雪花颜色
        t.pu()  #开始雪花的位置
        t.setx(r.randint(-350,350))#定义雪花出现的位置(x坐标)
        t.setx(r.randint(-100,350))#定义雪花出现的位置(Y坐标)
        t.pd()  #结束雪花的位置
        dens = 6    #定义雪花瓣数
        snowsize = r.randint(1,10)
        #跟五角星同理，画雪花
        for j in range(dens):
            t.fd(int(snowsize))
            t.backward(int(snowsize))
            t.right(int(360/dens))
drawanow()  #调用方法
t.done()

