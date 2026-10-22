import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df_dispersao = pd.read_csv("dados_dispersao.csv")
fig, ax = plt.subplots(figsize=(8,4))

sns.scatterplot(
    data=df_dispersao, x="altura_cm", y="peso_kg",
    hue="sexo", alpha=0.8, ax=ax
)
sns.regplot(data=df_dispersao, x="altura_cm", y="peso_kg", scatter=False, color="gray", ax=ax)

ax.set_title("Dispersão de peso e altura por gênero", fontweight = "bold")
plt.tight_layout()
plt.show()