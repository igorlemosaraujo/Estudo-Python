import pandas as pd
url = 'C:/Users/Igor/Downloads/PessoasSalarios.xlsx'

df1 = pd.read_excel(url)
print(df1.head())
print(df1.shape)