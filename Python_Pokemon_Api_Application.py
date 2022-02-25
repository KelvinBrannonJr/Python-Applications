import requests

while True:
    pick_a_pokemon = input("Type the name of a pokemon, or 'quit': ").lower()
    if pick_a_pokemon == 'quit':
        break
    url = f"https://pokeapi.co/api/v2/pokemon/{pick_a_pokemon}"
    pokemon_request = requests.get(url)

    if pokemon_request.status_code == 200:
        pokemon_response = pokemon_request.json()
        print(f"Pokemon name:\t{pokemon_response['name']}")

        for ability in pokemon_response['abilities']:
            print("Ability: ",ability['ability']['name'])
    else:
        print("Sorry that pokemon was not found...")







    
