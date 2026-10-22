import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df_frequencia = pd.read_csv("dados_frequencia.csv")
fig, ax = plt.subplots(figsize=(8,4))

sns.countplot(
    data=df_frequencia, x="tipo_atendimento",
   
)


ax.set_ylabel("Frequência")
plt.show()