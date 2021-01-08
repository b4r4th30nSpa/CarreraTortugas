import turtle

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
            
    
if __name__ == "__main__":     #esto es buena práctica cuando sospechamos que podriamos importar el script
    circuito = Circuito(640,480)            







