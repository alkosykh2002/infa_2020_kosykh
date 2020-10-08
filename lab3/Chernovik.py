
import matplotlib.pyplot as plt

x = [6.85, 7.0, 7.06, 7.14, 7.19, 7.23, 7.28, 7.32, 7.36, 7.41, 7.48]
y = [4.8, 4.6, 4.4, 4.2, 4.0, 3.8, 3.6, 3.4, 3.2, 3.0, 2.8]
sred = [0.0] * 11
i = 0
for ex in x:
    sred[i] = 28.8 - 3.47 * x[i]
    i = i + 1
plt.plot(x, y)
plt.plot(x, sred)
xerr = 0.01
yerr = 0.2
plt.grid(True)
plt.errorbar(x, y, xerr=xerr, yerr=yerr, fmt='o-', ecolor='red')
plt.show()
