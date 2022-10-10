import pandas as pd
import matplotlib

df1 = pd.read_excel("./datasets/Aracaju.xlsx")
df2 = pd.read_excel("./datasets/Fortaleza.xlsx")
df3 = pd.read_excel("./datasets/Natal.xlsx")
df4 = pd.read_excel("./datasets/Recife.xlsx")
df5 = pd.read_excel("./datasets/Salvador.xlsx")

df = pd.concat([df1,df2,df3,df4,df5])

# print(df.head())
# print(df.tail())
# print(df.sample(5))

# print(df.dtypes)

df["LojaID"] = df["LojaID"].astype("object")

# print(df.dtypes)

# print(df.head())

# print(df.isnull().sum())

df["Receita"] = df["Vendas"].mul(df["Qtde"])

df["Receita/Vendas"] = df["Receita"] / (df["Vendas"])

# print(df["Receita"].max())
# print(df["Receita"].min())

# print(df.nlargest(3,"Receita"))
# print(df.nsmallest(3,"Receita"))

somaReceita = df.groupby("Cidade")["Receita"].sum()

# print(df.sort_values("Receita", ascending=False).head(10))

# print(somaReceita)
# print(df.head())

##Trabalhando com datas
df["Data"] = df["Data"].astype("int64")
# print(df.dtypes)

df["Data"] = pd.to_datetime(df["Data"])
# print(df.dtypes)

receita_por_ano = df.groupby(df["Data"].dt.year)["Receita"].sum()
# print(receita_por_ano)
df["ano_Venda"] = df["Data"].dt.year
df["mes_Venda"], df["dia_Venda"] = (df["Data"].dt.month, df["Data"].dt.day)

# print(df["Data"].min())
# print(df["Data"].max())
df["diferença_Dias"] = df["Data"] - df["Data"].min()
df["trimestre_Venda"] = df["Data"].dt.quarter
vendas_Marco_19 = df.loc[(df["Data"].dt.year == 2019) & (df["Data"].dt.month == 3)]

# print(vendas_Marco_19)
# print(df.sample(5))

grafico = df["LojaID"].value_counts(ascending=False)
grafico.plot.bar()

