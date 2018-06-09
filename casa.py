import tkinter
import time


class Casa:
    def __init__(self, canvas, x,y):
        self.img = tkinter.PhotoImage(file='casa.png')
        self.ref = canvas.create_image(x, y,
                                       image=self.img,
                                       anchor=tkinter.NW)
        self.x = x
        self.y = y
        self.tempo = time.time()

    def update(self, canvas, casas):
        elapsed_time = time.time() - self.tempo
        if elapsed_time > 10:
            canvas.delete(self.ref)
            casas.remove(self)