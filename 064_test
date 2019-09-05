64.题目：利用ellipse 和 rectangle 画图。。

#### Answer

from tkinter import *

if __name__ == '__main__':
    canvas = Canvas(width=400, height=600, bg='white')
    left = 20
    right = 50
    top = 50

    for i in range(15):
        canvas.create_oval(250-right, 250-left, 250+right, 250+left)
        canvas.create_oval(250-20, 250-top, 250+20, 250+top)
        canvas.create_rectangle(20-2*i, 20-2*i, 10*(i+2), 10*(i+2))
        right += 5
        left += 5
        top += 10
    canvas.pack()
    mainloop()
