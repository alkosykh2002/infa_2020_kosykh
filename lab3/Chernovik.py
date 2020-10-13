import matplotlib.pyplot as plt
import numpy

x = [70000, 100000, 200000, 400000, 1 * 1000000, 1.5 * 1000000, 1.7 * 1000000,
     2.2 * 1000000, 2.5 * 1000000, 2.7 * 1000000, 2.8 * 1000000, 2.9 * 1000000, 3.2 * 1000000, 3.5 * 1000000,
     4.1 * 1000000, 4.5 * 1000000]
y = [0.1, 0.2, 0.4, 0.8, 2.0, 2.8, 3.2, 4.0, 4.1, 4.0, 3.6, 3.2, 2.0, 1.2, 0.4, 0]
arcsin = [0.0] * len(y)
log = [0.0] * len(x)
i = 0
for ex in x:
    log[i] = numpy.log(ex) / numpy.log(10)
    if i < 9:
        arcsin[i] = numpy.arcsin(y[i] / 4.1)
    if i > 8:
        arcsin[i] = numpy.pi - numpy.arcsin(y[i] / 4.1)
    i = i + 1
plt.grid(True)
plt.errorbar(log, arcsin, xerr=0, yerr=0.2, fmt='o-', ecolor='red')
ax = plt.gca()
ax.set_xlabel("lg(f)", fontsize=30, color='black')
ax.set_ylabel("Δφ", fontsize=30, color='black')
plt.show()
print(log)
print(arcsin)
