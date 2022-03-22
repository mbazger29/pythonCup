import tkinter

canvas = tkinter.Canvas(height=500, width=500)
canvas.pack()

def hore(event):
    global y, pocet_krokov
    canvas.delete('bodka')
    canvas.delete('body')
    canvas.create_line(x, y, x, y-25)
    pocet_krokov = pocet_krokov + 25
    y = y - 25
    canvas.create_oval(x-5, y-5, x+5, y+5, fill='red', tags='bodka')
    canvas.create_text(250, 25, text='Počet krokov: ' + str(pocet_krokov), font='Arial 20', tags='body')
    print(pocet_krokov)

def vlavo(event):
    global x, pocet_krokov
    canvas.delete('bodka')
    canvas.delete('body')
    canvas.create_line(x, y, x-25, y)
    pocet_krokov = pocet_krokov + 25
    x = x - 25
    canvas.create_oval(x-5, y-5, x+5, y+5, fill='red', tags='bodka')
    canvas.create_text(250, 25, text='Počet krokov: ' + str(pocet_krokov), font='Arial 20', tags='body')
    print(pocet_krokov)
    
def vpravo(event):
    pass

def dole(event):
    pass

x = 250   # globálna premenná
y = 250   # globálna premenná
pocet_krokov = 0 # globálna premenná!
canvas.create_oval(x-5, y-5, x+5, y+5, fill='red', tags='bodka')
canvas.create_text(250, 25, text='Počet krokov: ' + str(pocet_krokov), font='Arial 20', tags='body')

canvas.bind_all('<Up>',hore)
canvas.bind_all('<Left>',vlavo)
canvas.bind_all('<Down>',dole)
canvas.bind_all('<Right>',vpravo)

