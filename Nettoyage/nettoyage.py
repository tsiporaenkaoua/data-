import pandas as pd

#visualiser les valeurs manquantes
df = pd.DataFrame({
    "nom": ["Alice", "Marc", "Sarah"],
    "age": [25, None, 32],
    "ville": ["Paris", None, "Lyon"]
})

print(df.isnull().sum())


#supprimer les doublons
df = pd.DataFrame({
    "nom": ["Alice", "Marc", "Alice"],
    "age": [25, 30, 25]
})

df = df.drop_duplicates()
print(df)


#remplacer une valeur manquante
df = pd.DataFrame({
    "age": [20, 30, None, 40]
})

df["age"] =df["age"].fillna(df["age"].median())
print(df)


#Normaliser les valeurs
df = pd.DataFrame({
    "ville": [" paris ", "LYON", "Lyon "]
})
df["ville"] = df["ville"].str.strip().str.capitalize()#strip enleve les espace ant et apres
print(df)


#modifier les types et traiter les valeurs impossibles a convertir
df = pd.DataFrame({
    "salaire": ["3000", "3500", "inconnu"]
})

df["salaire"] = pd.to_numeric(df["salaire"], errors="coerce") #coerce remplace les valeurs non convertibles par NaN

print(df)



# Nettoyage
# -valeurs manquantes
# - Supprimer doublons
# - valeurs incohérentes (client de 450 ans)
# -Normaliser les textes

#donnée manquante (svt NaN) comment les gérer :

# - Supprimer une ligne incomplete (Si quelques lignes sont inutilisables et que le volume de données est suffisant)
# - Remplacer par une valeur (par exemple la médiane) si la colonne est importante
# - Si l'absence d'info a un sens conserver ou créer une catégore inconnu

# En machine learning, les règles de remplacement doivent être apprises sur les données d'entraînement, puis appliquées aux autres données pour éviter les fuites d'information.
