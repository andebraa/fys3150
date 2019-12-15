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

    plt.loglog(m_val[:-1], x, label='power law, $e^{b}x^a$')

    plt.loglog((m_val[:-1]),(histo[0]), label="Logarithmic histogram values")
    plt.xlabel('money', size = 14)

    plt.title('distribution of wealth with $\\alpha = 0$ and  $10^3$ Monte Carlo cycles,'\
    +'\n with a linear power law $e^{b}x^a$', size=14)
    plt.ylabel('frequency', size=14)





def simple_readfile(filename):

    data = np.loadtxt(filename)

    max = np.max(data)
    step = 30
    bins = int(max/step)
    m_val = np.linspace(0, max, bins)
    histo = np.histogram(data, bins=m_val)


    plt.plot(m_val[:-1],(histo[0]))
    plt.xlabel('money', size=14)
    plt.ylabel('frequency', size=14)




simple_readfile('500-500-0.000000-0.000000histogram_values_to_fit_parametrization-.txt')
simple_readfile('500-500-0.250000-0.000000histogram_values_to_fit_parametrization-.txt')
#simple_readfile('500-500-0.500000-0.000000histogram_values_to_fit_parametrization-.txt')
simple_readfile('500-500-0.900000-0.000000histogram_values_to_fit_parametrization-.txt')
simple_readfile('500-500-0.400000-0.000000histogram_values_to_fit_parametrization-.txt')
plt.legend(['$\lambda = 0$','$\lambda = 0.25$', '$\lambda = 0.5$', '$\lambda = 0.9$', '$\lambda = 0.4$'])
plt.title('histogram values for varying lambda', size=18)
plt.show()



#oppgave B see if you get a straight line etc
def linear_histogram(filename):

    data = np.loadtxt(filename)

    beta = (1.0/500)
    max = np.max(data)
    step = 30
    bins = int(max/step)
    m_val = np.linspace(0, max, bins)
    histo = np.histogram(data, bins=m_val)


    #linear fit:
    mask = histo[0] != 0

    a, b = np.polyfit(((m_val[:-1][mask])), np.log(histo[0][mask]), deg=1)

    x1 = m_val[:-1]*a + b

    wm = beta*np.exp(-beta*m_val[:-1])

    plt.plot(m_val[:-1], np.log(15000000*wm), label='gibbs distribution')
    plt.plot((m_val[:-1]),np.log((histo[0])), label="Logarithmic histogram values")
    plt.plot(m_val[:-1], (x1), label='linear fitting of all non zero values')
    plt.title('Logarithmic histogram values with a linear fit', size=16)
    plt.ylabel('frequency', size=14)
    plt.xlabel('money', size=14)
    plt.legend()
    plt.show()


    """

    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('money', size=14)
    ax1.set_ylabel('frequency', size=14)
    ax1.semilogy((m_val[:-1]),((histo[0])), label="Logarithmic histogram values")
    ax1.tick_params(axis='y')

    ax2 = ax1.twinx()

    color = 'tab:blue'

    ax2.set_ylabel('linear fit values')
    ax2.plot(m_val[:-1], (x1), label='linear fitting of all non zero values')
    ax2.tick_params(axis='y')
    plt.title('Logarithmic histogram values with a linear fit', size=16)
    plt.show()
    """




#oppgave B!
#linear_histogram('500-500_BIG2.txt')


#oppgave C!

"""
tail_fit('500-500_BIG2.txt')
tail_fit('500-500-0.250000_comp.txt')
tail_fit('500-500-0.500000_comp.txt')
tail_fit('500-500-0.900000.txt')
plt.legend(['Power law, $\lambda = 0','$\lambda = 0$','Power law, \lambda = 0.25',\
'$\lambda = 0.25$', 'Power law, \lambda = 0.5','$\lambda = 0.5$','Power law, \lambda = 0.9', '$\lambda = 0.9$'])
plt.show()
"""

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


def model_A():

    for i in ("0.5", "1.0", "1.5", "2.0"):
        data = np.loadtxt("500-500-0.900000-"+i+"00000model_A-.txt")

        max = np.max(data)
        step = 30
        bins = int(max/step)
        m_val = np.linspace(0, max, bins)

        histo = np.histogram(data, bins=m_val)
        mask = histo[0] != 0

        a, b = np.polyfit((np.log(m_val[:-1][mask])[20:]), np.log(histo[0][mask])[20:], deg=1)
        x1 = m_val[:-1]*a + b
        x = np.exp(b)*m_val[:-1]**a

        plt.loglog(m_val[:-1], x , label='power law, $e^{b}x^a$')

        plt.loglog((m_val[:-1]),(histo[0]), 'o', label=i)
        plt.xlabel('money', size = 14)
        plt.legend()
        #plt.title('distribution of wealth with $\\alpha = 0$ and  $10^3$ Monte Carlo cycles,'\
        #+'\n with a linear power law $e^{b}x^a$', size=14)
        plt.ylabel('frequency', size=14)

#model_A()
#plt.show()


