import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import square
from scipy.integrate import quad
from math import*


x=np.arange(-np.pi,np.pi,0.001) #x axis has been chosen from –π to +π, value
#of 1 smallest square along x axis is 0.001
y=square(x) #defining square wave function y=, for − π ≤ x ≤ π


fc=lambda x:square(x)*cos(i*x)  #i :dummy index
fs=lambda x:square(x)*sin(i*x)
n=50 #max value of I, not taken infinity, better result with high value
An=[]
Bn=[]
sum=0

for i in range(n):
   an=quad(fc,-np.pi,np.pi)[0]*(1.0/np.pi)
   An.append(an)
for i in range(n):
   bn=quad(fs,-np.pi,np.pi)[0]*(1.0/np.pi)
   Bn.append(bn) #putting value in array Bn

for i in range(n):
   if i==0.0:
      sum=sum+An[i]/2
   else:
      sum=sum+(An[i]*np.cos(i*x)+Bn[i]*np.sin(i*x))

plt.plot(x,sum,'g') #an, bn
plt.plot(x,y,'r--') #ave
plt.title("fourier series for square wave")

plt.show()