# This Python file uses the following encoding: utf-8


import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt('500-500_BIG2.txt')

max = np.max(data)
step = 30
bins = int(max/step)
m_val = np.linspace(0, max, bins)
histo = np.histogram(data, bins=m_val)
# m0 = 500
# w = lambda m : 1/m0 * np.exp(-m/m0)
mask = histo[0] != 0
a, b = np.polyfit(m_val[:-1][mask], np.log(histo[0][mask]), deg = 1)
x = m_val[:-1]*a +b

plt.plot(m_val[:-1], x)

plt.plot(m_val[:-1], np.log(histo[0]))
# plt.plot(m_val[:-1], np.log(w(m_val[:-1])))

plt.show()



#for i in range(len(data)[0]):
    #histo = np.histogram(data[i])


"""
dataen som er for høyere m har større usikkerhet, fordi eksempelvis en usikkerhet på 1 for m = 1E3
er veldig lite, men en usikkerhet på 1 er veldig mye mor m = 10.
Det at dataen ikke kan gå til negative verdier gir også feil lineærtilpasning hvis man tar med
data helt til høyre så blir lineærtilpassningen feil
"""
