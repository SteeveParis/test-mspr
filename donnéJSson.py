import json

def ecrire_dans_json(data, chemin_fichier):
    with open(chemin_fichier, 'w') as f:
        json.dump(data, f, indent=4)

# Exemple de données à écrire dans le fichier JSON
donnees = {
    "nom": "Remi",
    "age": 21,
    "ville": "PERDROVILLE"
}

# Chemin du fichier JSON à créer
chemin_fichier_json = "donnees.json"

# Appel de la fonction pour écrire les données dans le fichier JSON
ecrire_dans_json(donnees, chemin_fichier_json)

print("Données écrites dans le fichier JSON avec succès !")
