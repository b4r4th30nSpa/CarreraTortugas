import turtle
import random

class Circuito():
    corredores =[]
    __posStartY = (-30,-10,10,30)
    __colorTurtle = ('red', 'blue', 'green', 'orange')
    
    
    def __init__(self, width, height):
        self.__screen = turtle.Screen()
        self.__screen.setup(width, height)
        self.__screen.bgcolor('lightgray')
        self.__startLine = -width/2 + 0.03125*width
        self.__finishLine = width/2 - 0.03125*width
        
        self.__createRunners()
        
    def __createRunners(self):
        for i in range(4):
            newTurtle = turtle.Turtle()
            newTurtle.shape('turtle')
            newTurtle.color(self.__colorTurtle[i])
            newTurtle.penup()
            newTurtle.setpos(self.__startLine, self.__posStartY[i])
            self.corredores.append(newTurtle)
            
    def competir(self):  #debe ser invocada abajo
        hayGanador = False
        while not hayGanador:
            for tortuga in self.corredores:
                avance = random.randint(1,6)
                tortuga.fd(avance)
                #if tortuga.xcor() > self.__finishLine:
                if tortuga.pos()[0] >= self.__finishLine:
                    hayGanador = True
                    print('la tortuga de color {} ha ganado!'.format(tortuga.color()[0]))
                    break    
                    
if __name__ == "__main__":     #esto es buena práctica cuando sospechamos que podriamos importar el script

    circuito = Circuito(640,480)
    circuito.competir()
    







