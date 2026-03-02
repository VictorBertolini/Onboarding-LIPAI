import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 5, 0.1)
y1 = x**2
y2 = np.log(x)

# subplots
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(8, 4))

plt.suptitle("Gráfico de Subplots")
      
axes[0, 0].plot(x, y1)
axes[0, 1].plot(x, y2)

axes[1, 0].plot(x, y1/2)
axes[1, 1].plot(x, y2**2)

plt.show()
