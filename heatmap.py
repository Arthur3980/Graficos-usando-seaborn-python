import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df_heatmap = pd.read_csv("dados_heatmap.csv")


dia_semana = {"Segunda": 1, "Terça": 2, "Quarta-feira": 3, "Quinta-feira": 4, "Sexta-feira": 5, "Sábado": 6, "Domingo": 7}
df_heatmap["dia_semana"] = df_heatmap["dia_semana"].map(dia_semana)
df_heatmap["horario"] = pd.to_datetime(df_heatmap["horario"], format="%H:%M").dt.hour
matriz_corr = df_heatmap.corr()



fig, ax = plt.subplots(figsize=(8,4))


sns.heatmap(
    matriz_corr, annot=True, fmt=".2f",
    cmap="coolwarm", linewidths=.5, ax=ax
)

ax.set_title("Matriz de movimento de clientes", fontweight = "bold")

plt.tight_layout()
plt.show()