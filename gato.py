import tkinter
import math


class Gato:
    def __init__(self, canvas, x,y):
        self.img = tkinter.PhotoImage(file='gato.png')
        self.ref = canvas.create_image(x, y,
                                       image=self.img,
                                       anchor=tkinter.NW)
        #self.ref = canvas.create_rectangle(
        #    x,y,x+10, y+10, fill="#66FF66")
        self.x = x
        self.y = y
        self.vel = 5;

    def update(self, canvas, diffTime, ultimoClick):
        angulo = math.atan2(
            ultimoClick.y - self.y,
            ultimoClick.x - self.x
        )
        destX = math.cos(angulo)*self.vel
        destY = math.sin(angulo)*self.vel
        canvas.move(self.ref,destX , destY)
        self.x += destX
        self.y += destY