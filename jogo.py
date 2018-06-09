#O Gato é uma IA que correrá atrás do rato mais próximo que não está em uma casa    OK
#A casa é criar pelo usuário ao clicar na tela.  OK
#A casa deverá durar apenas 10 segundos  OK
#O usuário só poderá colocar 5 casas ao mesmo tempo no jogo. OK
#O jogo começa com 6 Ratos  OK
#O jogador perde quando todos os ratos morreram  OK

#O Rato deve fugir do gato e se esconder em uma casa que esteja vaga OK ?
#O jogador ganha se conseguir salvar pelo menos 1 rato por 2 min

#------------------------------------------------------------------------

import random
import time
import tkinter
import math

from gato import Gato
from ponto import Ponto
from casa import Casa
from rato import Rato

#------------------------------------------------------------------------

tk = tkinter.Tk()
canvas = tkinter.Canvas(tk, width=800, height=800)
canvas.pack()

gato = Gato(canvas, random.randint(0,800), random.randint(0,800))

ratos = [
    Rato(canvas, random.randint(0,800), random.randint(0,800)),
    Rato(canvas, random.randint(0,800), random.randint(0,800)),
    Rato(canvas, random.randint(0,800), random.randint(0,800)),
    Rato(canvas, random.randint(0,800), random.randint(0,800)),
    Rato(canvas, random.randint(0,800), random.randint(0,800)),
    Rato(canvas, random.randint(0,800), random.randint(0,800))
]

casas = []

continua = True
ultimoClick = Ponto(0,0)

#------------------------------------------------------------------------

def CriaCasa():
    if len(casas) < 5:
        casas.append(Casa(canvas, ultimoClick.x, ultimoClick.y))

#------------------------------------------------------------------------
#Função de callback para quando clicar com o Mouse
def callback(event):
    if continua:
        ultimoClick.x = event.x
        ultimoClick.y = event.y
        CriaCasa()

#------------------------------------------------------------------------

def PosRatoMaisProximo():
    minDist = 1.18973149536e+4932
    posRato = Ponto(0, 0)

    for rato in ratos:
        dist = math.hypot(rato.x - gato.x, rato.y - gato.y)
        if (dist < minDist):
            minDist = dist
            posRato.x = rato.x
            posRato.y = rato.y

    return posRato

#------------------------------------------------------------------------

def PosCasaMaisProxima(rato):
    minDist = 1.18973149536e+4932
    posCasa = Ponto(0, 0)

    for casa in casas:
        dist = math.hypot(casa.x - rato.x, casa.y - rato.y)
        if (dist < minDist):
            minDist = dist
            posCasa.x = casa.x
            posCasa.y = casa.y

    return posCasa


#------------------------------------------------------------------------

canvas.bind("<Button-1>", callback)
ultimoTempo = time.time()
vitoria = False

while 1:
    while continua:
        diffTime = int((time.time() - ultimoTempo)*500)
        ultimoTempo = time.time()

        gato.update(canvas, diffTime/1000,PosRatoMaisProximo())

        for casa in casas:
            casa.update(canvas, casas)

        posGato = Ponto(gato.x, gato.y)
        for rato in ratos:
            rato.update(canvas, posGato, PosCasaMaisProxima(rato), ratos)

        continua = len(ratos) > 0

        tk.update()
        time.sleep(0.03)

    textoFinal = "Voce perdeu!"
    if vitoria:
        textoFinal = "Voce ganhou!"

    mylabel = canvas.create_text((400, 400), text=textoFinal)

    tk.update()