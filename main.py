from pokemon import Pokemon

if __name__ == "__main__":
    bulbasaur_lv1 = Pokemon(
        "bulbasaur",
        1,
        "grass",
        "blue",
        "male",
        level=1
    )

    bulbasaur_lv10 = Pokemon(
        "bulbasaur",
        1,
        "grass",
        "green",
        "male",
        level=10
    )

    print("Nivel 1:", bulbasaur_lv1)
    bulbasaur_lv1.attack()
    print("Nivel 10:", bulbasaur_lv10)
