import turtle as tu
import math
import sys
from PyQt5 import QtWidgets, uic, QtCore, QtGui
import os


tm = 0.3
ux = 0
uy = 0
dx = 0
dy = 0
g = 9.8
v = 0
a = 0
l = []

dir = os.getcwd()+'\\'
_translate = QtCore.QCoreApplication.translate

class Form(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi(dir+'system.ui')
        self.ui.setWindowTitle(_translate("Dialog", "포물선 궤적"))
        self.ui.pushButton.clicked.connect(self.draw)
        self.ui.window_width.setValue(600)
        self.ui.window_height.setValue(600)
        self.ui.ball_width.setValue(0.3)
        self.ui.ball_height.setValue(0.3)
        self.ui.pushButton_2.hide()



        self.ui.show()


    def draw(self):
        w = self.ui.window_width.value()
        h = self.ui.window_width.value()
        x = self.ui.ball_width.value()
        y = self.ui.ball_height.value()
        windowinit(w,h,x,y)
        global a
        global v
        v = self.ui.velocity.value()
        a = math.radians(self.ui.angle.value())
        px = self.ui.hor_pos.value() / 100
        py = self.ui.ver_pos.value() / 100
        px *= (tu.window_width()/2)
        py *= (tu.window_height()/2)
        draw_pos(px,py)


def draw_pos(x,y):
    index = len(l) - 1
    tu.hideturtle()
    tu.setpos(x,y)
    tu.showturtle()
    tu.stamp()

    def isinWindow():
        r = False
        if dy > (tu.window_height() / 2):
            r = True
        elif dy < -(tu.window_height() / 2):
            r = True
        elif dx < -(tu.window_width() / 2):
            r = True
        elif dx > (tu.window_width() / 2):
            r = True
        return r

    hl = -(tu.window_height() / 2)
    ux=v*math.cos(a)
    uy=v*math.sin(a)
    while True:
        uy = uy + (-1*g)*tm
        dy = tu.ycor() + (uy*tm) - (g*tm**2) / 2
        dx = tu.xcor() + (ux*tm)
        if dy > hl:
            tu.goto(dx,dy)
            #print(self.dx,self.dy)
            tu.stamp()
        else:
            break
        #if isinWindow():
        #    break
    l[index].mainloop()

def windowinit(w,h,x,y):
    tu.setup(w,h)
    tu.shape("circle")
    tu.shapesize(x,y,0)
    tu.penup()
    global l
    l.append(tu.Screen())
    #s.exitonclick()
    #self.s.onscreenclick()
    #draw_pos(0,0)
    #s.listen()

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    form = Form()
    sys.exit(app.exec_())