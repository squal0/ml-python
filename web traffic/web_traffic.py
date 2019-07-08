import numpy as n
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

data = sp.genfromtxt("C:/Users/Home/Documents/Python scripts/ML/resources/ch01/data/web_traffic.tsv", delimiter="\t")

x = data[:, 0]
y = data[:, 1]
x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]

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

fp1 = sp.polyfit(x, y, 1)
fp2 = sp.polyfit(x, y, 2)
fp3 = sp.polyfit(x, y, 3)
fp10 = sp.polyfit(x, y, 10)
fp17 = sp.polyfit(x, y, 17)

f1 = sp.poly1d(fp1)
f2 = sp.poly1d(fp2)
f3 = sp.poly1d(fp3)
f10 = sp.poly1d(fp10)
f17 = sp.poly1d(fp17)

plot_lines = []
plot_lines.extend([f1, f2, f3, f10, f17])

print error(f1, x, y)
print error(f2, x, y)
print error(f3, x, y)
print error(f10, x, y)
print error(f17, x, y)

fx = sp.linspace(0, x[-1], 1000)

plt.plot(fx, f1(fx), linewidth=4, linestyle='solid')
plt.plot(fx, f2(fx), linestyle='dashdot')
plt.plot(fx, f3(fx), linestyle='dashed', color='blue')
plt.plot(fx, f10(fx), linestyle='dotted', color='purple')
plt.plot(fx, f17(fx), linestyle='solid', color='red')

legend = plt.legend(plot_lines[0],
                       ["degree1","degree2","degree3","degree10","degree17"], loc="upper left")

plt.legend([l[0] for l in plot_lines], loc="upper left")
plt.gca().add_artist(legend)

plt.show()
