import matplotlib.patches as mpatches
import numpy as np
import matplotlib.pyplot as plt
import aseegg as ag

czestotliwosc1 = 10
czestotliwosc2 = 25
czestotliwosc3 = 40
czestProbkowania = 500
a1 = 5
a2 = 10
a3 = 20
czas = 1
czas2 = 3
t = np.linspace(0, czas, czas * czestProbkowania)
t2 = np.linspace(0, czas2, czas2 * czestProbkowania)
f = np.linspace(0, 256, 3*500)
sygnal=np.concatenate([np.concatenate([a1*np.sin(2*np.pi*czestotliwosc1*t), a2*np.sin(2*np.pi*czestotliwosc2*t)]), a3*np.sin(2*np.pi*czestotliwosc3*t)])
transformata = ag.FFT(sygnal)
przefiltrowany = ag.dolnoprzepustowy(sygnal, czestProbkowania, 15)
transformata2 = ag.FFT(przefiltrowany)

plt.plot(t2, sygnal)
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda [-]")
plt.show()
plt.plot(t2, przefiltrowany)
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda [-]")
plt.show()
plt.stem(f, transformata)
plt.xlabel("Częstotliwość [Hz]")
plt.ylabel("Amplituda [-]")

plt.show()
plt.stem(f, transformata2)
plt.xlabel("Częstotliwość [Hz]")
plt.ylabel("Amplituda [-]")
plt.show()
