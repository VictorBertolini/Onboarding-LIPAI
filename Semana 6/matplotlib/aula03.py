import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(-np.pi, np.pi, 100)

y = np.cos(t)
y1 = np.sin(t)


plt.figure("Gráfico", figsize=(6, 4))
plt.plot(t, y)
plt.plot(t, y1)
plt.title("Gráficos do Seno e Cosseno")
plt.xlabel("Eixo de tempo")
plt.ylabel("Eixo da Amplitude")
plt.grid()
plt.show()


