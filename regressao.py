import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df_regressao = pd.read_csv("dados_regressao.csv")
fig, ax = plt.subplots(figsize=(8, 4))

sns.scatterplot(
    data=df_regressao, x="renda_mensal", y="gasto_mensal",
    hue="gasto_mensal", alpha=0.8, ax=ax
)
sns.regplot(data=df_regressao, x="renda_mensal", y="gasto_mensal", scatter=False, color="gray", ax=ax)

ax.set_title("Relação entre renda_mensal e gasto_mensal", fontweight="bold")
plt.tight_layout()
plt.show()