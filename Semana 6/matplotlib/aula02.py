import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 2*np.pi, 500)
y = np.cos(2*t)
y1 = np.sin(2*t)


plt.figure("Cosseno", figsize=(5, 4))
plt.plot(t, y)
plt.title("Gráfico do cosseno")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")


plt.figure("Seno", figsize=(5, 7))
plt.plot(t, y1)
plt.title("Gráfico do Seno")
plt.xlabel("Tempo 2 (s)")
plt.ylabel("Amplitude 2")

plt.show()
