# scatter_plot.py
# Coded by Marco Fringuelli
import matplotlib.pyplot as plt
from random import choice
# This code is to generate a view of a scatter plot of any two variables (features)
# Here it is a random values generation, the function 'shuffle_vect' can be substituted with a deterministic one

def shuffle_vect(dim):
    # Function to generate a randomly ordered integers vector
    # Wrote it because the 'random.shuffle()' function works in place, does not return a vector
    vector = []
    base = [i for i in range(dim)]
    done = False
    while not done:
        val = choice(base)
        if val not in vector:
            vector.append(val)
        if len(vector) == dim:
            done = True
    #print vector
    return vector

class scatter_plot():
    """A simple scattering diagram plotter"""
    def __init__(self,x_min,x_max,y_min,y_max):
        self.xm = x_min
        self.xM = x_max
        self.ym = y_min
        self.yM = y_max

    def set(self, rangein):
        self.range = rangein
        self.vect = [i for i in range(self.range)]
        self.f2_sig = shuffle_vect(self.range)
        self.f2_bkg = shuffle_vect(self.range)
        self.f1_sig = shuffle_vect(self.range)
        self.f1_bkg = shuffle_vect(self.range)

    def show(self,color1,color2,label1,label2,xlabel,ylabel):
        self.color1 = color1
        self.color2 = color2
        self.label1 = label1
        self.label2 = label2
        self.xlabel = xlabel
        self.ylabel = ylabel
        f1s = [i for i in self.f1_sig if i>self.xM/2]
        f2s = [i for i in self.f2_sig if i>self.yM/2]
        f1b = [i for i in self.f1_bkg if i>self.xM/2]
        f2b = [i for i in self.f2_bkg if i>self.yM/2]
        print f1s, f2s
        plt.xlim(self.xm, self.xM) #Sets domains
        plt.ylim(self.ym, self.yM)
        #plt.xticks(())
        #plt.yticks(())
        plt.scatter(f2s, f1s, color = self.color1, label = self.label1) # Plot attributes
        plt.scatter(f2b, f1b, color = self.color2, label = self.label2)
        plt.legend() # Plot legend
        plt.xlabel(self.xlabel) # Variable names
        plt.ylabel(self.ylabel)
        plt.show()

#------------MAIN--------------#
sp = scatter_plot(0,1000,0,1000)
rangein = 1000
sp.set(rangein)
sp.show('g','r','Label1','Label2','Feature1','Feature2')
