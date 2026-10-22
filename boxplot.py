import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df_boxplot = pd.read_csv("dados_boxplot.csv")
fig, ax = plt.subplots(figsize=(8,4))

sns.boxplot(
    data=df_boxplot, x="departamento", y="salario",
    palette="Pastel1", ax=ax
)

ax.set_title("Salários por departamento", fontweight = "bold")

plt.tight_layout()
plt.show()