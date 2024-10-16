56.题目：画图，学用circle画圆形。

import turtle  # 导入turtle库

t = turtle.Pen()

for i in range(10):
    t.penup()
    t.goto(0, -50*i)
    t.pendown()
    t.circle(50+50*i)

turtle.done()
