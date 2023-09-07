import requests

# A GitHub felhasználó neve, akinek az adatait lekéred
github_username = "kobanya"

# Az API végpontja a felhasználó repository-ainak lekérdezéséhez
api_url = f"https://api.github.com/users/{github_username}/repos"

# HTTP GET kérés a felhasználó repository-jainak lekérdezéséhez
response = requests.get(api_url)

# Ellenőrizzük a választ
if response.status_code == 200:
    # A válasz tartalma JSON formátumban érkezik
    repositories = response.json()

    # Létrehozunk egy üres listát a repository-k nevének és nyelvének tárolásához
    repo_info = []

    # Lekérjük az összes repository nevét és nyelvét
    for repo in repositories:
        repo_name = repo["name"]
        if repo["language"]:
            repo_language = repo["language"]
        else:
            repo_language = "Nincs megadva nyelv"
        repo_info.append((repo_name, repo_language))

    # Kiírjuk az összes repository nevét és nyelvét
    for name, language in repo_info:
        print(f"A tároló neve: {name:>30},\t Nyelv: {language}")
else:
    print(f"Hiba történt a GitHub API-val való kommunikáció során. Státuszkód: {response.status_code}")
