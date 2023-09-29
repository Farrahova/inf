import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(16, 9))
ax1 = fig.add_subplot(311)
ax2 = fig.add_subplot(312)
ax3 = fig.add_subplot(313)

values1 = np.random.normal(0, 10, 1000)
values2 = np.random.normal(0, 10, 2000)
values3 = np.random.normal(0, 10, 7000)

ax1.hist(values1, 50)
ax1.grid()
ax2.hist(values2, 50)
ax2.grid()
ax3.hist(values3, 50)
ax3.grid()

x = [i for i in range(50)]
y = [j ** 1.5 for j in x]

ax2.set_title('second graph')
ax3.set_title('third graph')

plt.show()