# Matplotlib
## Aluno

Victor Bertolini de Sousa

Github: https://github.com/VictorBertolini/Onboarding-LIPAI


## Aulas

### Aula 01
```python
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 2*np.pi, 100)
y = np.cos(2*t)
print(y)

plt.plot(t, y)
plt.title("Gráfico do cosseno")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.show()
```

### Aula 02
```python
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

```

### Aula 03
```python
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
```

### Aula 04
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 500)
c = np.cos(x)
s = np.sin(x)

plt.figure("Gráficos consenoidais", figsize=(8, 4))
plt.subplots_adjust(
    left=0.12,
    right=0.964,
    top=0.9,
    bottom=0.14,
    wspace=0.438,
    hspace=0.655
)

ax1 = plt.subplot(2, 1, 1)
plt.plot(x, c)
ax1.set_title("Gráfico do Cosseno")
ax1.set_xlabel("Eixo do Tempo")
ax1.set_ylabel("Eixo da Amplitude")


ax2 = plt.subplot(2, 1, 2)
plt.plot(x, s)
ax2.set_title("Gráfico do Seno")
ax2.set_xlabel("Eixo de Tempo")
ax2.set_ylabel("Eixo da Amplitude")

plt.show()
```

### Aula 05
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 5, 0.1)
y1 = x**2
y2 = np.log(x)

# subplots
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2,figsize=(8, 4))

plt.suptitle("Gráfico de Subplots")
      
ax1.plot(x, y1)
ax2.plot(x, y2)

ax3.plot(x, y1**2)
ax4.plot(x, y2/2)

plt.show()
```

### Aula 06
```python
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
```

### Aula 07
```python
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
```

### Aula 08
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 300)
y = np.cos(3*x)

fig, axe = plt.subplots(figsize=(7, 4))
axe.plot(x, y)

axe.set_title("Gráfico do Cosseno", fontsize=16)
axe.set_xlabel("Eixo X", fontsize=14)
axe.set_ylabel("Eixo Y", fontsize=14)

plt.xticks(np.arange(0, 2*np.pi, 0.5))
plt.yticks(np.arange(-1, 1.2, 0.2))


plt.grid(True)
plt.show()
```

### Aula 09
```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.style as st

plt.style.use("seaborn-v0_8-dark-palette")

x = np.linspace(0, 2*np.pi, 300)
y = np.cos(3*x)

fig, axe = plt.subplots(figsize=(7, 4))
axe.plot(x, y)

axe.set_title("Gráfico do Cosseno", fontsize=16)
axe.set_xlabel("Eixo X", fontsize=14)
axe.set_ylabel("Eixo Y", fontsize=14)

plt.xticks(np.arange(0, 2*np.pi, 0.5))
plt.yticks(np.arange(-1, 1.2, 0.2))


plt.grid(True)
plt.show()

print(st.available)
```

### Aula 10
```python
import matplotlib.pyplot as plt
import numpy as np

plt.style.use("ggplot")

x = np.linspace(1, 5, 500)
y = np.log10(x)



fig, axe = plt.subplots(figsize=(7, 4))
axe.plot(x, y, lw=1.2)
axe.plot([0, 2.5], [0.4, 0.4], color="gray", linestyle="--", lw=0.8)
axe.plot([2.5, 2.5], [0, 0.4], color="gray", linestyle="--", lw=0.8)
axe.plot(2.5, 0.4, marker="o", color="red")
axe.set_xticks(np.arange(0, 5.5, 0.5))
plt.show()
```

### Aula 11
```python
import matplotlib.pyplot as plt
import numpy as np

plt.style.use("ggplot")

x = np.linspace(1, 5, 500)
y = np.log10(x)


fig, axe = plt.subplots(figsize=(7, 4))
axe.plot(x, y, lw=1.2)

axe.text(2.6, 0.35, "P(2,5;0.4)")
axe.text(3, 0.42, "Logaritimo $y = log_{10}x$", fontsize=10, bbox=dict(facecolor="red", alpha=0.5))
axe.annotate("P(2,5;0,4)", xy=(2.5, 0.4), fontsize=16, xytext=(0.5, 0.5), arrowprops=dict(facecolor="red"), color="r")


axe.plot([0, 2.5], [0.4, 0.4], color="gray", linestyle="--", lw=0.8)
axe.plot([2.5, 2.5], [0, 0.4], color="gray", linestyle="--", lw=0.8)
axe.plot(2.5, 0.4, marker="o", color="red")
axe.set_xticks(np.arange(0, 5.5, 0.5))
axe.set_title("Gráfico Logaritmico")
axe.set_xlabel("Eixo X")
axe.set_ylabel("Eixo Y")

plt.show()
```

## Exercícios 01
```python
import matplotlib.pyplot as plt
import pandas as pd
```
```python
df = pd.read_csv("../datasets/classification_results_trial_0001.csv")


```python
df
```

```python
categorias = df["real_class"].value_counts()

plt.bar(categorias.index, categorias.values, color="g")

plt.xlabel('Categorias')
plt.ylabel('Quantidades')
plt.title('Quantidade de casos por classe')

plt.show()
```

```python
categorias = df["predicted_class"].value_counts()

plt.bar(categorias.index, categorias.values, color="g")

plt.xlabel('Categorias')
plt.ylabel('Quantidades')
plt.title('Quantidade de casos por classe')

plt.show()
```
```python
data = df["prob_benign"]

plt.hist(data)

plt.xlabel('Probabilidade de ser Benigno')
plt.ylabel('Frequência (Quantidade)')
plt.title('Distribuição da Probabilidade Benigna')

plt.show()

```python
data = df["prob_malign"]

plt.hist(data)

plt.xlabel('Probabilidade de ser Maligno')
plt.ylabel('Frequência (Quantidade)')
plt.title('Distribuição da Probabilidade Maligna')

plt.show()
```

```python
acertos = df[df['real_class'] == df['predicted_class']]
erros = df[df['real_class'] != df['predicted_class']]

plt.scatter(acertos['prob_benign'], acertos['prob_malign'], color='green', label='Acerto', alpha=0.7)

plt.scatter(erros['prob_benign'], erros['prob_malign'], color='red', label='Erro', alpha=0.8, marker='x')

plt.xlabel('Probabilidade Benigno')
plt.ylabel('Probabilidade Maligno')
plt.title('Análise de Acertos vs Erros')

plt.legend()

plt.show()
```

```python
malign_df = df[df['real_class'] == 'malign']
benign_df = df[df['real_class'] == 'benign']

FP = (benign_df["real_class"] != benign_df['predicted_class']).sum()

FN = (malign_df["real_class"] != malign_df['predicted_class']).sum()

tipos_erro = ['Falsos Positivos (FP)', 'Falsos Negativos (FN)']

plt.figure(figsize=(8, 5))
barras = plt.bar(tipos_erro, [FP, FN], color=['orange', 'red'], width=0.6)

plt.bar_label(barras)

plt.ylabel('Quantidade de Erros')
plt.title('Comparação de Erros: FP vs FN')
plt.grid(axis='y', alpha=0.7)

plt.show()
```
## E em contexto médico: qual é mais preocupante e por quê?

O mais grave é o falso positivo, pois o paciente acredita que não tem nenhum problema e isso prejudica agir rapidamente na cura ou tratamento do mesmo, então é um atraso em seu tratamento.


### Exercício 2
```python
import matplotlib.pyplot as plt
import pandas as pd
```
```python
df = pd.read_csv("../datasets/metrics.csv")
```

```python
x = df.index
y1 = df['train_loss']
y2 = df['val_loss']

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))

plt.subplots_adjust(
     wspace=0.438,
)

plt.suptitle("Gráfico de Train e Val Loss")

axes[0].plot(x, y1, color="green")
axes[0].set_xlabel("Epoch")
axes[0].set_ylabel("Train Loss")


axes[1].plot(x, y2, color="darkblue")
axes[1].set_xlabel("Epoch")
axes[1].set_ylabel("Val Loss")


plt.show()
```

```python
x = df.index
y1 = df['train_acc']
y2 = df['val_acc']

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))

plt.subplots_adjust(
     wspace=0.438
)

plt.suptitle("Gráfico de Train e Val Accuracy")

axes[0].plot(x, y1, color="green")
axes[0].set_xlabel("Epoch")
axes[0].set_ylabel("Train Accuracy")

axes[1].plot(x, y2, color="darkblue")
axes[1].set_xlabel("Epoch")
axes[1].set_ylabel("Val Accuracy")

plt.show()
```
