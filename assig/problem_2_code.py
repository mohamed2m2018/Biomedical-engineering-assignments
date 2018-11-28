from __future__ import division
import matplotlib.pyplot as plt
import numpy as np



text_file = open("Data2.txt", "r")

lines = text_file.read().split('\n')
del lines[-1]

lines= list(map(float,lines))




def diff(list):
    diffSignal=[]
    max=len(lines)-2
    const=1/(8*(1/512))
    for index in range (2,max) :
             diffSignal.append(
                const*(
                    -1*lines[index-2]
                    -2*lines[index-1]
                    +2*lines[index+1]
                    +1*lines[index+2]
                    )
             )


    return diffSignal

diffSignal=diff(list)
plt.plot(diffSignal)
plt.show()

def square (diffSignal):
        squaredSignal=[]

        for element in diffSignal :
                squaredSignal.append(element*element)


        return squaredSignal

squaredSignal=square(diffSignal)

plt.plot(squaredSignal)
plt.show()

def smooth (squaredSignal):
        smoothedSignal=[]
        add=0
        for index in range (30,len(squaredSignal)-31):
                        for count in range (0,31) :
                                add+=(1/31 *(squaredSignal[index-count]))
                        smoothedSignal.append(add)
                        add=0

        return smoothedSignal


smoothedSignal=smooth(squaredSignal)

plt.plot(smoothedSignal)
plt.show()

def shift(smoothedSignal,shiftAmount):
        shiftedSignal=[]

        for values in range (0,shiftAmount):
                shiftedSignal.append(0)

        for index in range (0,len(smoothedSignal)):
                shiftedSignal.append(smoothedSignal[index])

        return shiftedSignal


def autoCorrelate(smoothedSignal):
        add=0
        shiftedSignal=[]
        autocorr=[]
        for i in range (0,2000):
                shiftedSignal=shift(smoothedSignal,i)
                for j in range (0,len(smoothedSignal)):
                        add+=smoothedSignal[j]*shiftedSignal[j]
                autocorr.append(add)
                add=0
        return autocorr


autocorr=autoCorrelate(smoothedSignal)
plt.plot(autocorr)
plt.show()

def findPeaks(autocorr):
    add=0
    for element in autocorr:
        if(element>np.mean(autocorr)):
            add+=1
    return add
print(findPeaks(autocorr))
