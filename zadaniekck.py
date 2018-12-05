# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 22:24:17 2018

@author: Adam
"""
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
import matplotlib.pyplot as plt
 
f = 3
A = 1
t = np.linspace(0, 1, 256)
sygnal = A*np.sin(2*np.pi*f*t)
 
plt.subplot(3, 1, 1)
plt.plot(t, sygnal, color = 'blue')
plt.title('Amplituda = 1')
plt.ylabel('wartosc funkcji')
plt.ylim(-1,1)




f = 3
A = 2
t = np.linspace(0, 1, 256)
sygnal = A*np.sin(2*np.pi*f*t)
 
plt.subplot(3, 1, 2)
plt.plot(t, sygnal, color = 'orange')
plt.title('Amplituda = 2')
plt.ylabel('wartosc funkcji')
plt.ylim(-2,2)



f = 3
A = 3
t = np.linspace(0, 1, 256)
sygnal = A*np.sin(2*np.pi*f*t)
 
plt.subplot(3, 1, 3)
plt.plot(t, sygnal, color = 'red')
plt.title('Amplituda = 3')
plt.ylabel('wartosc funkcji')
plt.ylim(-3,3)


plt.xlabel('czas[s]')


plt.tight_layout()

plt.show()


import numpy as np
import matplotlib.pyplot as plt

f = 2
A = 1
t = np.linspace(0, 1, 256)
sygnal = A*np.sin(2*np.pi*f*t)

plt.subplot(3, 1, 1)
plt.plot(t, sygnal, color = 'blue')
plt.title('Czestotliwosc = 2Hz')
plt.ylabel('wartosc funkcji')
plt.ylim(-1,1)




f = 5
A = 2
t = np.linspace(0, 1, 256)
sygnal = A*np.sin(2*np.pi*f*t)

plt.subplot(3, 1, 2)
plt.plot(t, sygnal, color = 'orange')
plt.title('Czestotliwosc = 5Hz')
plt.ylabel('wartosc funkcji')
plt.ylim(-2,2)



f = 10
A = 3
t = np.linspace(0, 1, 256)
sygnal = A*np.sin(2*np.pi*f*t)

plt.subplot(3, 1, 3)
plt.plot(t, sygnal, color = 'red')
plt.title('Czestotliwosc = 10Hz')
plt.ylabel('wartosc funkcji')
plt.ylim(-3,3)


plt.xlabel('czas[s]')


plt.tight_layout()

plt.show()


from numpy import *
import numpy as np
import matplotlib.pyplot as plt

b = 90
f = 3
A = 1
t = np.linspace(0, 1, 256)
sygnal = A*np.sin(2*np.pi*f*t+b)
 
plt.subplot(3, 1, 1)
plt.plot(t, sygnal, color = 'blue')
plt.title('Przesuniecie fazowe = 90')
plt.ylabel('wartosc funkcji')
plt.ylim(-1,1)



b = 180
f = 3
A = 1
t = np.linspace(0, 1, 256)
sygnal = A*np.sin(2*np.pi*f*t+b)
 
plt.subplot(3, 1, 2)
plt.plot(t, sygnal, color = 'orange')
plt.title('Przesuniecie fazowe = 180°')
plt.ylabel('wartosc funkcji')
plt.ylim(-1,1)


b = 270
f = 3
A = 1
t = np.linspace(0, 1, 256)
sygnal = A*np.sin(2*np.pi*f*t+b)
 
plt.subplot(3, 1, 3)
plt.plot(t, sygnal, color = 'red')
plt.title('Przesuniecie fazowe = 270')
plt.ylabel('wartosc funkcji')
plt.ylim(-1,1)


plt.xlabel('czas[s]')


plt.tight_layout()

plt.show()


import numpy as np
import matplotlib.pyplot as plt
 
f1 = 3
f2 = 5
f3 = 2
t = np.linspace(0, 1, 256)
sygnal = np.sin(2*np.pi*f1*t)+np.sin(2*np.pi*f2*t)+np.sin(2*np.pi*f3*t)
plt.plot(t, sygnal)
 

t = np.linspace(0, 1, 8)
sygnal = np.sin(2*np.pi*f1*t)+np.sin(2*np.pi*f2*t)+np.sin(2*np.pi*f3*t)
plt.plot(t, sygnal)
plt.title('Częstotliwosc probkowania = 8')
plt.show()


t = np.linspace(0, 1, 256)
sygnal = np.sin(2*np.pi*f1*t)+np.sin(2*np.pi*f2*t)+np.sin(2*np.pi*f3*t)
plt.plot(t, sygnal)



t = np.linspace(0, 1, 15)
sygnal = np.sin(2*np.pi*f1*t)+np.sin(2*np.pi*f2*t)+np.sin(2*np.pi*f3*t)
plt.plot(t, sygnal, color = 'red')
plt.title('Częstotliwosc probkowania = 15')
plt.show()


t = np.linspace(0, 1, 256)
sygnal = np.sin(2*np.pi*f1*t)+np.sin(2*np.pi*f2*t)+np.sin(2*np.pi*f3*t)
plt.plot(t, sygnal)


t = np.linspace(0, 1, 40)
sygnal = np.sin(2*np.pi*f1*t)+np.sin(2*np.pi*f2*t)+np.sin(2*np.pi*f3*t)
plt.plot(t, sygnal, color = 'black')
plt.title('Częstotliwosc probkowania = 40')
plt.show()



plt.show()



