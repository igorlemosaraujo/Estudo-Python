import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("seaborn")

df = pd.read_excel("./datasets/AdventureWorks.xlsx")

print(df.head())
print(df.shape)
print(df.dtypes)

print(df["Valor Venda"].sum())

df["Custo"] = df["Custo Unitário"].mul(df["Quantidade"])

print(df.head())


