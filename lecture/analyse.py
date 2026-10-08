import pandas as pd

df = pd.read_csv("client.csv")

print(df)
print(df.head)

#nb lignes et colonnes
print(df.shape)
df.info()

#selectionner une colonne
print(df["achat"])

#selectionner une ligne (iloc(position) ou loc(index))
print(df.iloc[1])

#moyenne
print(df["age"].mean())

#max pour les pour les valeurs numériques
print(df["achat"].max())

#Pour compter une valeur qui reviens le plus de fois
print(df["ville"].value_counts())