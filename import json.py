import git

def get_git_info(repository_path):
    # Ouvrir le dépôt Git
    repo = git.Repo(repository_path)

    # Obtenir des informations générales sur le dépôt
    repo_info = {
        "url": repo.remotes.origin.url,
        "branche_actuelle": repo.active_branch.name,
        "dernier_commit": str(repo.head.commit),
        "auteurs": [commit.author.name for commit in repo.iter_commits()]
    }

    return repo_info

# Chemin vers le répertoire Git local
epath = "https://github.com/Hedox1/test-mspr"

# Appel de la fonction pour obtenir les informations
informations = get_git_info(epath)

# Afficher les informations récupérées
print("Informations du dépôt Git :")
print("URL du dépôt :", informations["url"])
print("Branche actuelle :", informations["branche_actuelle"])
print("Dernier commit :", informations["dernier_commit"])
print("Auteurs :", informations["auteurs"])
