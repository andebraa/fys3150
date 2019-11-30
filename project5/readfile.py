# This Python file uses the following encoding: utf-8


import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def tail_fit(filename):
    data = np.loadtxt(filename)

    max = np.max(data)
    step = 30
    bins = int(max/step)
    m_val = np.linspace(0, max, bins)
    histo = np.histogram(data, bins=m_val)


    #linear fit:
    mask = histo[0] != 0

    a, b = np.polyfit((np.log(m_val[:-1][mask])[50:]), np.log(histo[0][mask])[50:], deg=1)
    x1 = m_val[:-1]*a + b
    x = np.exp(b)*m_val[:-1]**a

    plt.loglog(m_val[:-1], x)


    plt.loglog(np.log(m_val[:-1]),np.log(histo[0]))
    plt.xlabel('money')
    plt.ylabel('frequency')
    plt.show()


def simple_readfile(filename):

    data = np.loadtxt(filename)

    max = np.max(data)
    step = 30
    bins = int(max/step)
    m_val = np.linspace(0, max, bins)
    histo = np.histogram(data, bins=m_val)


    #linear fit:
    mask = histo[0] != 0

    a, b = np.polyfit(((m_val[:-1][mask])), (histo[0][mask]), deg=1)


    plt.plot(m_val[:-1],(histo[0]))
    plt.xlabel('money')
    plt.ylabel('frequency')
    plt.show()

#bare enkle plott:
#simple_readfile('500-500-0.900000.txt')


#oppgave B!
#readfile('500-500_BIG2.txt')


#oppgave C!
tail_fit('500-500_BIG2.txt')
tail_fit('500-500-0.250000_comp.txt')
tail_fit('500-500-0.500000_comp.txt')
tail_fit('500-500-0.900000.txt')
plt.legend(['$\lambda = 0$','$\lambda = 0.25$', '$\lambda = 0.5$', '$\lambda = 0.9$'])


def hist_diff(filename):

    data = np.loadtxt(filename)

    max = np.max(data)
    step = 30
    bins = int(max/step)
    m_val = np.linspace(0, max, bins)

    hist_arr = np.zeros((len(data[0]), len(m_val)-1))
    diff = np.zeros(len(data[:-1,1]))
    hist_arr[0] = np.histogram(data[0], bins = m_val)[0]
    for i in range(1, len(data[0])-1):

        hist_arr[i,:] = np.histogram(data[:i], bins=m_val)[0]
        diff[i]=np.linalg.norm(((hist_arr[i]/i)-(hist_arr[i-1]/(i-1))))


    plt.plot(diff)


#the following code generates the relative difference
"""
hist_diff('500-500_BIG2.txt')
hist_diff('500-500-0.250000_comp.txt')
hist_diff('500-500-0.500000_comp.txt')
hist_diff('500-500-0.900000_comp.txt')
plt.legend(['$\lambda = 0$','$\lambda = 0.25$', '$\lambda = 0.5$', '$\lambda = 0.9$'])
plt.title('relative difference in montecarlo steps', size=18)
plt.xlabel('Monte Carlo steps', size=14)
plt.ylabel('Relative difference', size=14)
plt.show()
"""
"""
dataen som er for høyere m har større usikkerhet, fordi eksempelvis en usikkerhet på 1 for m = 1E3
er veldig lite, men en usikkerhet på 1 er veldig mye mor m = 10.
Det at dataen ikke kan gå til negative verdier gir også feil lineærtilpasning hvis man tar med
data helt til høyre så blir lineærtilpassningen feil
"""
