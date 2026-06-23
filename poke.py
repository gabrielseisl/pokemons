import requests



def info():
    pokemon = input("Qual Pokémon deseja pesquisar? ").lower().lstrip()
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        print("---Informações gerais ---")
        print("nome:", dados["name"])
        print("número:", dados["id"])
        print("altura:", dados["height"])
        print("peso:", dados["weight"])
        print("---Tipos---")
        for item in dados ["types"]:
            print("-",item ["type"]["name"])

        print("---Status---")
        for stat in dados ["stats"]:
            print("-",stat["stat"]["name"],":",stat["base_stat"])






def lista():
    quantidade= input("Quantos Pokemons Você quer ver? ")
    pokemonsdisponiveisURL=f"https://pokeapi.co/api/v2/pokemon?limit={quantidade}"
    respostadisponivel= requests.get(pokemonsdisponiveisURL)
    if respostadisponivel.status_code == 200:
        dados = respostadisponivel.json()
        print("---Pokemons---")
        for pokemon in dados ["results"]:
            print("-", pokemon["name"])


def batalha():

    pokemon1 = input("pokemon: ").lower().strip()
    pokemon2 = input("segundo pokemon: ").lower().strip()

    url1 = f"https://pokeapi.co/api/v2/pokemon/{pokemon1}"
    url2 = f"https://pokeapi.co/api/v2/pokemon/{pokemon2}"

    resposta1 = requests.get(url1)
    resposta2 = requests.get(url2)

    if resposta1.status_code == 200 and resposta2.status_code == 200:

        info1 = resposta1.json()
        info2 = resposta2.json()

        pontos1 = 0
        pontos2 = 0

        print("---", info1["name"], "---")
        for stat in info1["stats"]:
            print("-", stat["stat"]["name"], ":", stat["base_stat"])
            pontos1 += stat["base_stat"]

        print("Total:", pontos1)

        print("---", info2["name"], "---")
        for stat in info2["stats"]:
            print("-", stat["stat"]["name"], ":", stat["base_stat"])
            pontos2 += stat["base_stat"]

        print("total:", pontos2)

        print("--- Resultado ---")

        if pontos1 > pontos2:
            print(info1["name"], "venceu a batalha,massa")

        elif pontos2 > pontos1:
            print(info2["name"], "venceu a batalha,massa")

        else:
            print("empate")

    else:
        print("pokémon não existe")

while True:
    print("menu")
    print("1-ver pokemons")
    print("2-escolher pokemon para ver status")
    print("3-batalha")
    print("0-sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        lista()

    elif opcao == "2":
        info()

    elif opcao == "3":
        batalha()

    elif opcao == "0":
        break

    else:
        print("opção inválida")