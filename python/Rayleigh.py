import numpy as np
import scipy.stats
import scipy.stats as stats
import matplotlib.pyplot as plt
from numpy import random



# Creating dataset
x1 = [-10,10]


Nmeas = 1
Nexp = 1000

mu_experiment = 0
mu_truearr = []
mu_bestarr = []
sigma = 2

for i in range(-100,100):
    mu_true = i//10

    for e in range(0,Nexp):
        mu_best = 0

        for m in range(0,Nmeas):
            z = float(random.normal(mu_true, sigma))
            mu_best += z

np.true_divide(mu_true, Nexp)
mu_bestarr.append(mu_best)
mu_truearr.append(mu_true)


plt.hist2d(mu_truearr,mu_bestarr, bins = 20)
plt.hist(x1, bins =20)
#plt.fill(mu_truearr,mu_bestarr)
plt.show()
