import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df_linhas = pd.read_csv("dados_linhas.csv")
df_linhas["data"] = pd.to_datetime(df_linhas["data"], format="%Y-%m-%d")
sns.set_theme(style="whitegrid")

fig, ax = plt.subplots(figsize=(10, 4))

sns.lineplot(
    data=df_linhas[df_linhas["data"].dt.year == 2026],
    x="loja", y="vendas",
    marker="o", color="#2563eb", linewidth=2, ax=ax
)

ax.set_title("Vendas das lojas por data", fontweight="bold")
ax.set_xlabel("Loja")
ax.set_ylabel("Vendas")

plt.tight_layout()
plt.show()