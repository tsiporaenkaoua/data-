import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("client.csv")

print("---------------Rapport clients---------------------")
# nombre total de clients
shape = df.shape
print(f"Nombre total de clients : {shape[1]}")
# âge moyen
print(f"age moyen : {df["age"].mean()}")
# achat moyen
print(f"achat moyen : {df["achat"].mean()}")
# le client qui a acheté le plus
idx_max = df["achat"].idxmax()
client_max = df.loc[idx_max]
print(f"Le client qui a acheté le plus est : { client_max["nom"]} pour {client_max["achat"]}€ d'achat")
# la ville avec le plus de clients
print(f"Ville principale : {df["ville"].value_counts().idxmax()}")
# le nombre de clients actifs
clients_actifs = df["statut"].value_counts()
print(f"Clients actifs : {clients_actifs["Actif"]}")


#GRAPHIQUE

plt.bar(df["nom"], df["achat"])
plt.xlabel("Clients")
plt.ylabel("Achats")
plt.title("Achats clients")
plt.show()