import pandas as pd

#Charger le fichier avec Pandas et afficher les cinq premières lignes.
df = pd.read_csv("clientsBrut.csv")
print(df.head(5))

#Afficher le nombre de lignes et de colonnes, les types de données et les valeurs manquantes.
print(df.shape)
print(df.dtypes)
print(df.isnull())

#Identifier les doublons exacts.
duplicateRows = df[df.duplicated(subset=df.columns.difference(['id']), keep=False)]
print(duplicateRows)

#Repérer les âges suspects, notamment ceux supérieurs à 120 ans.

#Convertir la colonne salaire en valeurs numériques.

#Uniformiser les noms de villes.

# Décider comment traiter les doublons, l'âge de Paul et les salaires manquants ou invalides.

# Vérifier la qualité du dataset après nettoyage.

# Exporter le résultat dans un fichier clients_clean.csv.

# Rédiger un court bilan des changements effectués et de leurs raisons.