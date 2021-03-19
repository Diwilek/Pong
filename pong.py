import turtle


def ustawieniaOkna(okno):    #ustawienia okna
    okno.title('Gra pong')
    okno.setup(width=1000, height=800)
    okno.tracer(0)
    okno.colormode(255)
    okno.bgcolor('khaki')

class Dlugopis():

    def __init__(self):
        self.zolwik = turtle.Turtle()
        self.zolwik.hideturtle()
        self.zolwik.color('white')
        self.zolwik.shapesize(stretch_wid = 10, stretch_len = 1)
        self.zolwik.penup()
        self.zolwik.goto(0, 350)
        self.zolwik.write('Gracz A: 0 Gracz B: 0',align = 'Center', font=('Arial',30))

    def wypisz(self, punkty_A, punkty_B):
        self.zolwik.clear()
        self.zolwik.write('Gracz A {} Gracz B: {}' .format(punkty_A,punkty_B) ,align = 'Center')

class Paletka():        #ustawienia paletki

    def __init__(self, pozycja):
        self.zolwik = turtle.Turtle()
        self.zolwik.shape('square')
        self.zolwik.color('white')
        self.zolwik.shapesize(stretch_wid = 10, stretch_len = 1)
        self.zolwik.penup()
        self.zolwik.goto(pozycja, 0)

    def gora(self):  #ustawiamy paletke w górę i w dół
        y = self.zolwik.ycor()
        y += 30
        if y < 330:
            self.zolwik.sety(y)

    def dol(self):
        y = self.zolwik.ycor()
        y -= 30
        if y > -330:
            self.zolwik.sety(y)

class Pilka():      #ustawienia Piłki

    def __init__(self,a,b,dlugopis):
        self.zolwik = turtle.Turtle()
        self.zolwik.shape('circle')
        self.zolwik.color('white')
        self.zolwik.penup()
        self.zolwik.goto(0, 0)
        self.dx = 1
        self.dy = 1
        self.a = a
        self.b = b
        self.dlugopis = dlugopis
        self.punkty_A = 0
        self.punkty_B = 0

    def ruch(self):
        self.zolwik.setx(self.zolwik.xcor() + self.dx)
        self.zolwik.sety(self.zolwik.ycor() + self.dy)    #od tego miejsca w którym jestes przemiesc sie o tyle pikseli ile wynosi ,,dy,,

    def zderzenia(self):   #gora i dol
        if self.zolwik.ycor() > 390:
            self.zolwik.sety(390) #limit
            self.dy *= -1  # po zderzeniu ze scianka pileczka obraca kierunek
        if self.zolwik.ycor() < -390:
            self.zolwik.sety(-390)
            self.dy *= -1

        #lewo i prawo

        if self.zolwik.xcor() > 490:
            self.zolwik.setx(490)
            self.dx *= -1
            self.punkty_A += 1
            self.dlugopis.wypisz(self.punkty_A,self.punkty_B)

        if self.zolwik.xcor() < -490:
            self.zolwik.setx(-490)
            self.dx *= -1
            self.punkty_B += 1
            self.dlugopis.wypisz(self.punkty_A,self.punkty_B)

        #paletki

        if self.zolwik.xcor() < -430 and abs(self.zolwik.ycor() - self.a.zolwik.ycor()) < 50:    #jest dalej niz 430 i roznica miedzy wspolrzednymi y < 50
            self.zolwik.goto(-420, self.zolwik.ycor())
            self.dx *= -1  #odwracamy prędkość

        if self.zolwik.xcor() > 430 and abs(self.zolwik.ycor() - self.b.zolwik.ycor()) < 50:
            self.zolwik.goto(420, self.zolwik.ycor())
            self.dx *= -1


def bind(okno, a, b):  #dobieramy przyciski z klawiatury aby wykonać czynność paletką

        okno.listen()
        okno.onkeypress(a.gora, 'w')
        okno.onkeypress(a.dol, 's')
        okno.onkeypress(b.gora, 'Up')
        okno.onkeypress(b.dol, 'Down')


def gra(okno):

    a = Paletka(-450)   #lewa paletka
    b = Paletka(450)    #prawa paletka
    d = Dlugopis()
    pilka = Pilka(a,b,d)
    bind(okno, a, b)   #łączy nam zdarzenie wciskania na klawiturze a i b
    while True:
        okno.update()
        pilka.ruch()
        pilka.zderzenia()


def main():
    okno = turtle.Screen()
    ustawieniaOkna(okno)
    gra(okno)


main()