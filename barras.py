import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df_barras = pd.read_csv("dados_barras.csv")
fig, ax = plt.subplots(figsize=(8,4))

sns.barplot(
    data=df_barras, x="categoria", y="vendas_medias",
    hue="regiao", palette="Set2", errorbar=None, ax=ax
)

ax.set_title("Vendas médias das categorias por região", fontweight = "bold")
ax.set_ylabel("Médias das categorias")

plt.tight_layout()
plt.show()