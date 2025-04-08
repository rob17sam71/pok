import requests

pokemon = input("input pokemon character:").lower()
url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

req = requests.get(url)
if req.status_code == 200:
    data = req.json()
    print(f"Name is\t\t{data['name']}\nAbilities:")
    abiility = [print(ability['ability']['name']) for ability in data['abilities']]
    

else: 
    print("unknown character")