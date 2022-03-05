import turtle, random

k = turtle.Turtle()
k.speed(0)

def okno():
    k.fillcolor('white')
    k.begin_fill()
    for i in range(2):
        k.forward(10)
        k.left(90)
        k.forward(20)
        k.left(90)
    k.end_fill()

def poschodie(pocet):
    for i in range(pocet):
        okno()
        k.penup()
        k.forward(10+10)
        k.pendown()
    k.penup()
    k.backward((10+10)*pocet)
    k.pendown()

def n_poschodi(pocet_poschodi, pocet_okien):
    for i in range(pocet_poschodi):
        poschodie(pocet_okien)
        k.penup()
        k.right(90)
        k.forward(10+20)
        k.left(90)
        k.pendown()
    k.penup()
    k.left(90)
    k.forward((pocet_poschodi+1)*20 + (pocet_poschodi)*10 )
    k.right(90)
    k.pendown()
            

def panelak(vyska, pocet_okien):
    farba = '#{:06x}'.format(random.randrange(256**3))
    k.fillcolor(farba)
    k.begin_fill()
    for i in range(2):
        k.forward(pocet_okien*10 + (pocet_okien+1)*10)
        k.right(90)
        k.forward(vyska*20 + (vyska+1)*10)
        k.right(90)
    k.end_fill()
    k.penup()
    k.forward(10)
    k.right(90)
    k.forward(10 + 20)
    k.left(90)
    k.pendown()
    n_poschodi(vyska, pocet_okien)
    k.penup()
    k.backward(10)
    k.left(90)
    k.forward(10)
    k.right(90)
    k.pendown()

panelak(4, 5)















