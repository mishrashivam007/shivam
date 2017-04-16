from tkinter import *
mainwindow=Tk()
canvas = Canvas(mainwindow, width = 1000, height = 1000,bg="pink")
canvas.pack()
def menu1():
    canvas.delete("all")
    canvas.create_rectangle(3,3,400,300,width=9)
def menu2():
    canvas.delete("all")
    canvas.create_oval(3,3,100,100,fill="red")
def menu3():
    canvas.delete("all")
    canvas.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
def menu4():
    canvas.delete("all")
    canvas.create_text(30, 290, anchor=W, text="shivam and janhavi",font="-weight bold")
def menu5():
    quit()
def menu6():
    canvas.delete("all")
    x0 = 15
    y0 = 75
    x1 = 95
    y1 = 150

    x2 = 5
    y2 = 24
    x3 = 30
    y3 = 50

    x4 = 2
    y4 = 10
    x5 = 12
    y5 = 20

    x6 = 605
    y6 = 150
    x7 = 665
    y7 = 200

    x8 = 605
    y8 = 150
    x9 = 665
    y9 = 200

    x10 = 605
    y10 = 150
    x11 = 665
    y11 = 200

    i = 0
    deltax = 2
    deltay = 3
    deltax1 = 3
    deltay1= 4
    deltax2=4
    deltay2=5

    deltax3 = 2
    deltay3 = 3
    deltax4 = 3
    deltay4= 4
    deltax5=4
    deltay5=5

    canvas.create_text(500, 400, text="By_SHIVAM_MISHRA",font="-weight bold")


    which = canvas.create_oval(x0,y0,x1,y1,fill="red", tag='redBall')
    which = canvas.create_oval(x2,y2,x3,y3,fill="pink", tag='pinkBall')
    which = canvas.create_oval(x4,y4,x5,y5,fill="black", tag='blackBall')
    canvas.create_text(40, 320,anchor=W, text="BALLS OF DIFFERENT SHAPE SO DFFERENT SPEED",font="-weight bold")

    which = canvas.create_oval(x6,y6,x7,y7,fill="red", tag='redBall1')
    which = canvas.create_oval(x8,y8,x9,y9,fill="pink", tag='pinkBall1')
    which = canvas.create_oval(x10,y10,x11,y11,fill="black", tag='blackBall1')
    canvas.create_text(642, 320,anchor=W, text="BALLS OF SAME SHAPE SO SAME SPEED",font="-weight bold")

    canvas.create_rectangle(3,3,400,300,width=9)
    canvas.create_rectangle(602,3,998,300,width=9)

    ########################### FOR SECOND RECTANGLE ############################################

    while True:
        canvas.move('redBall1', deltax3, deltay3)
        canvas.after(0)
        canvas.update()
        if x7 >= 998:
            deltax3 = -2
        if x6 < 602:
            deltax3 = 2
        if y7 > 300:
            deltay3 = -3
        if y6 < 0:
            deltay3 = 3
        x6 += deltax3
        x7 += deltax3
        y6 += deltay3
        y7 += deltay3
        canvas.move('pinkBall1', deltax4, deltay4)
        canvas.after(0)
        canvas.update()
        if x9 >= 998:
            deltax4 = -2
        if x8 < 602:
            deltax4 = 2
        if y9 > 300:
            deltay4 = -3
        if y8 < 0:
            deltay4 = 3
        x8 += deltax4
        x9 += deltax4
        y8 += deltay4
        y9 += deltay4

        canvas.move('blackBall1', deltax5, deltay5)
        canvas.after(0)
        canvas.update()
        if x11 >= 998:
            deltax5 = -3
        if x10 < 602:
            deltax5 = 3
        if y11 > 300:
            deltay5 = -2
        if y10 < 0:
            deltay5 = 2
        x10 += deltax5
        x11 += deltax5
        y10 += deltay5
        y11 += deltay5

    ########################### FOR FIRST RECTANGLE #############################################
        canvas.move('redBall', deltax, deltay)
        canvas.after(2)
        canvas.update()
        if x1 >= 400:
            deltax = -2
        if x0 < 0:
            deltax = 2
        if y1 > 300:
            deltay = -3
        if y0 < 0:
            deltay = 3
        x0 += deltax
        x1 += deltax
        y0 += deltay
        y1 += deltay
        canvas.move('pinkBall', deltax1, deltay1)
        canvas.after(0)
        canvas.update()
        if x3 >= 400:
            deltax1 = -6
        if x2 < 0:
            deltax1 = 6
        if y3 > 300:
            deltay1 = -5
        if y2 < 0:
            deltay1 = 5
        x2 += deltax1
        x3 += deltax1
        y2 += deltay1
        y3 += deltay1

        canvas.move('blackBall', deltax2, deltay2)
        canvas.after(-4)
        canvas.update()
        if x5 >= 400:
            deltax2 = -10
        if x4 < 0:
            deltax2 = 10
        if y5 > 300:
            deltay2 = -9
        if y4 < 0:
            deltay2 = 9
        x4 += deltax2
        x5 += deltax2
        y4 += deltay2
        y5 += deltay2


    
label1=Label(mainwindow,text="change")
label1.pack()
menubar=Menu(mainwindow)
filemenu=Menu(menubar)
filemenu.add_command(label="Rectangle",command=menu1)
filemenu.add_command(label="Circle",command=menu2)
filemenu.add_command(label="Line",command=menu3)
filemenu.add_command(label="creater's name",command=menu4)
menubar.add_cascade(label="Shapes",menu=filemenu)
menubar.add_command(label="Quit",command=menu5)
menubar.add_command(label="Animation",command=menu6)
mainwindow.config(menu=menubar)
mainloop()
