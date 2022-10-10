import pandas as pd

df = pd.read_csv("./datasets/Gapminder.csv", sep=";")

df = df.rename(columns={"country": "pais", "continent": "continente", "year": "ano", "lifeExp": "expectativaVida", "pop": "população", "gdpPercap": "pibPercap"})
print(df.head(10))
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.tail())
print(df.describe())
print(df["continente"].unique())
africa = df.loc[df["continente"] == "Africa"]
print(africa.head(20))
print(africa["continente"].unique())

paisporcontinete = df.groupby("continente")["pais"].nunique()
print(paisporcontinete)

expVidaAno = df.groupby("ano")["expectativaVida"].mean()
print(expVidaAno)
print(df["pibPercap"].mean())