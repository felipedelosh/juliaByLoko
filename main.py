"""
Conjunto de jilia Mandelbrot 11 13 2020

Interfaz grafica que muestra el conjunto de julia en un intervalo

dado un plano XY se va a graficar el fractal [-2, 1] x [-1,1]

Ojo fuera de un disco de radio 2 la sucesion diverge.


colores de convergencia

nro de puntos de convergencia : color

Convergence : White color
Divergence : Black Color


"""

from tkinter import *  # Graph
import os # To know path project
import math # To calculate floor


class Mandelbrot:
    def __init__(self):
        self.screem = Tk()
        self.canvas = Canvas(self.screem, width=1280, height=720, bg='snow') # Draw everythis here
        self.txtScale = Entry(self.canvas)
        self.lblInsertScale = Label(self.canvas, text="Insert a # Scale:")
        self.btnCalcular = Button(self.canvas, text="Calculate >>", command=self.calculate)
        self.pathProject = str(os.path.dirname(os.path.abspath(__file__)))
        """I need two variables to reescale a planXY:
        0,0 ist a first iteration but in the realidad is a point (-2, -2)
        ...
        """
        self.MaxLongAxisX = 2
        self.MaxLongAxisY = 2
        self.sizeOfPlane = 2
        #Try to load a colors.txt
        self.convergenceColors = []
        try:
            path = self.pathProject+'\\colors.txt'
            f = open(path, 'r', encoding='UTF-8')
            for i in f.read().split('\n'):
                if str(i).strip() != "":
                    self.convergenceColors.append(i)
        except:
            self.convergenceColors = ['white', 'snow', 'linen', 'azure','red', 'deep pink', 'blue', 'SlateBlue1', 'green', 'purple', 'black']
        
        # Configure visuals elements and launch interface
        self.launchInterface()


    def launchInterface(self):
        self.screem.title("Julia Mandelbrot by loko")
        self.screem.geometry("1280x720")

        self.canvas.place(x=0, y=0)
        self.lblInsertScale.place(x=20, y=20)
        self.txtScale.place(x=20, y=50)
        self.btnCalcular.place(x=200, y=50)
        # Draw x and y Axis
        #self.canvas.create_line(0, 360, 1280, 360)
        #self.canvas.create_line(640, 0, 640, 720)

        #for i in range(0, len(self.convergenceColors)):
        #    self.canvas.create_rectangle(5+(i*5), 5, 10+(i*10), 10, fill=self.convergenceColors[i])

      
        # Refresh Screem
        self.screem.after(0, self.refreshInterface)
        self.screem.mainloop()

    # Refresh a screem 30ms
    def refreshInterface(self):
        self.screem.after(30, self.refreshInterface)


    def calculate(self):
        """

        1 -> Validate a scale number [2, ?]

        ? IS A POSITIVE NUMBER 
        
        Note I have : i5-7200 and not calculate over 300 too busy
        Calculate a pont(x, y) e Mandelbrot
        
        Region#1 e X[-2 to 2] and Y[-2 to 2]

        a point forfor (0,0) = -2, 2 map of values

        x = ((X/totalPixels)*(sizeOfPlane*2)) - sizeOfPlane


        Note : Ignore all becouse diverge
        x<-1.9
        x>0.5 
        y > 1.5

        """
        self.canvas.delete("pixels")

        if self.validateScale():
            for i in range(1, 240):
                for j in range(1, 140):
                    x = ((i/240)*(self.MaxLongAxisX*2)) - self.sizeOfPlane
                    y = -((j/140)*(self.MaxLongAxisY*2)) + self.sizeOfPlane

                    if self.excludePoint(x, y):
                        self.canvas.create_rectangle(5+(i*5), 5+(j*5), 10+(i*5), 10+(j*5), fill='gray6', tags='pixels')
                    else:
                        lvlConvergence = math.floor(self.levelOfConvergence(x, y))
                        self.canvas.create_rectangle(5+(i*5), 5+(j*5), 10+(i*5), 10+(j*5), fill=self.convergenceColors[lvlConvergence], tags='pixels')  


        else:
            print('Error')

        
       

    def levelOfConvergence(self, x, y):
        """
        felipedelosH
        Calculate a convergence 
        if retruns 1 converge onbe number in K trys

        Zo = 0
        Zn+1 = Zn2 + C
        """
        k = int(self.txtScale.get())
        div = 1
        
        if k > 10:
            div = k/10

        listOfconvergenceNumbers = []
        komplex = complex(x, y)
        Z = 0

        for i in range(0, k):
            Z = (Z*Z) + komplex

            if Z not in listOfconvergenceNumbers:
                listOfconvergenceNumbers.append(Z)

        return (len(listOfconvergenceNumbers)/div)*7


    def validateScale(self):
        try:
            k = int(self.txtScale.get())
            return k >= 2
        except:
            return False

    def excludePoint(self, x, y):
        """
        if point is divergence
        Mandelbrot is only X(-1.9, 0.5] Y[1, -1] for any ponits converge
        so many ponits divergen
        """
        if x<-1.9 or x > 0.5:
            return True

        if y < -1.3 or y > 1.3:
            return True

        if x < -1 and y > 0.6:
            return True

        if x < -1 and y < -0.6:
            return True

        if x < -1.5 and y > 0.05:
            return True

        if x < -1.5 and y < -0.05:
            return True

        if x < -0.3 and y > 0.7:
            return True

        if x < -0.3 and y < -0.7:
            return True

        if x > 0.2 and y > 0.7:
            return True

        if x > 0.2 and y < -0.7:
            return True
        
        return False


m = Mandelbrot()