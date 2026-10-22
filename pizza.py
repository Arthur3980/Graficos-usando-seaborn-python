import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df_pizza = pd.read_csv("dados_pizza.csv")
faturamento = [45000.0, 32000.0, 21000.0, 8000.0, 14000.0]
canal_venda = ["Site", "Loja Física","Aplicativo","Telefone","Parceiros"]
cores = sns.color_palette("Set2")

fig, ax = plt.subplots(figsize=(6, 6))

ax.pie(
    faturamento, labels=canal_venda, autopct="%1.1f%%",
    startangle=90, colors=cores,
    # wedgeprops=dict(width=0.6, edgecolor="white") # Rosca
)

ax.set_title("Distribuição de faturamento por canal de venda", fontweight="bold")
plt.tight_layout()
plt.show()