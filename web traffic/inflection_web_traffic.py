import numpy as n
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

data = sp.genfromtxt("C:/Users/Home/Documents/Python scripts/ML/resources/ch01/data/web_traffic.tsv", delimiter="\t")

x = data[:, 0]
y = data[:, 1]
x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]

inflection = 3.5*7*24 #calculate the inflection point in hours
xa = x[:inflection] #data before the inflection point
ya = y[:inflection]
xb = x[inflection:] # data after
yb = y[inflection:]

#sp.sum(sp.isnan(y))
plt.scatter(x, y, s=10)
plt.title("Web traffic over last month")
plt.xlabel("Time")
plt.ylabel("Hits/Hour")
plt.xticks([w * 7 * 24 for w in range(10)], ['week %i' % w for w in range(10)])

plt.autoscale(tight=True)
plt.grid(True, linestyle='-', color='0.75')

def error(f, x, y):
       return sp.sum((f(x) - y) ** 2)

fa = sp.poly1d(sp.polyfit(xa, ya, 1))
fb = sp.poly1d(sp.polyfit(xb, yb, 1))

fa_error = error(fa, xa, ya)
fb_error = error(fb, xb, yb)

print ("Error inflection=%f" % (fa_error + fb_error))

fx = sp.linspace(0, x[-1], 1000)

plt.plot(fx, fa(fx), linestyle='solid', color='green')
plt.plot(fx, fb(fx), linestyle='dashdot', color='black')

plt.show()
