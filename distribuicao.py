import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df_distribuicao = pd.read_csv("dados_distribuicao.csv")
fig, ax = plt.subplots(figsize=(8,4))

sns.histplot(
    data=df_distribuicao, x="idade",
    bins=15, kde=True,
    color="#2563eb", ax=ax
)

ax.set_title("Distribuição das idades", fontweight = "bold")
ax.set_ylabel("Frequência")

plt.tight_layout()
plt.show()