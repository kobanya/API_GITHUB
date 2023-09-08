import requests

resp = requests.get('http://127.0.0.1:5000/termek')

# Ellenőrizzük a válasz státuszkódját
if resp.status_code == 200:
    termek_lista = resp.json()

    # A termek_lista egy lista, így végig kell menni rajta
    for termek in termek_lista:
        # Ellenőrizzük, hogy a "termék neve" kulcs létezik a termékben
        if 'termék neve' in termek:
            termek_neve = termek['termék neve']
            print(f"Termék neve: {termek_neve}")
        else:
            print("Nincs 'termék neve' kulcs a termékben.")
else:
    print(f"Hiba történt a kérés során. Státuszkód: {resp.status_code}")
