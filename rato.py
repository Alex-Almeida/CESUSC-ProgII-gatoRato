import tkinter
import math

class Rato:
    def __init__(self, canvas, x,y):
        self.img = tkinter.PhotoImage(file='rato.png')
        self.ref = canvas.create_image(x, y,
                                       image=self.img,
                                       anchor=tkinter.NW)
        self.x = x
        self.y = y
        self.vel = 2.5;

    def update(self, canvas, posGato, ultimoClick, ratos):
        if posGato.x > self.x and posGato.x < self.x+32 and posGato.y > self.y and posGato.y < self.y+32:
            canvas.delete(self.ref)
            ratos.remove(self)
        else:
            angulo = math.atan2(
                ultimoClick.y - self.y,
                ultimoClick.x - self.x
            )
            destX = math.cos(angulo)*self.vel
            destY = math.sin(angulo)*self.vel
            canvas.move(self.ref,destX , destY)
            self.x += destX
            self.y += destY