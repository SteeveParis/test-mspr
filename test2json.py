import requests
import json

def get_json_from_github(repository_owner, repository_name, path_to_json):
    # URL de l'API GitHub pour obtenir le contenu du fichier
    api_url = f"https://api.github.com/repos/Hedox1/test-mspr/contents/eeejson.json"

    try:
        # Faire une requête GET à l'API GitHub
        response = requests.get(api_url)

        # Vérifier si la requête a réussi (code 200)
        if response.status_code == 200:
            # Charger le contenu JSON de la réponse
            json_content = json.loads(response.content)

            # Décoder le contenu du fichier base64
            json_data = json.loads(base64.b64decode(json_content['content']).decode('utf-8'))

            return json_data
        else:
            print(f"Erreur lors de la requête à l'API GitHub (code {response.status_code}): {response.text}")
    except Exception as e:
        print(f"Erreur inattendue : {e}")

# Remplacez ces valeurs par celles de votre dépôt et fichier JSON
owner = "Hedox1"
repo = "test-mspr"
json_path = "https://github.com/Hedox1/test-mspr"

# Appel de la fonction pour obtenir les données JSON depuis GitHub
donnees_json = get_json_from_github(owner, repo, json_path)

# Afficher les données extraites
print("Données JSON extraites depuis GitHub:")
print(donnees_json)