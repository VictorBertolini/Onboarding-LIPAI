import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 100)
y = np.cos(4*x)

plt.figure(figsize=(8, 4))
plt.plot(x, y, color="#F5276C", lw=0.5, marker="X", linestyle="dashed")
plt.grid(True)
plt.title("Gráfico do Cosseno")
plt.xlabel("Eixo do Tempo")
plt.ylabel("Eixo da Amplitude")
plt.show()
