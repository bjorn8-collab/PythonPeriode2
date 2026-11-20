print("welkom bij de shop")
player_name = input("hoe heet je? ")
player_gold = 100
inventory = []

print(f"hoi {player_name} je hebt {player_gold} goud")

shop_items = ["zwaard", "schild", "drankje", "boog"]
print("\ndit is te koop")
for item in shop_items:
    print(item)

while True:
    print("\n--- shop ---")
    print("1. koop zwaard (50 goud)")
    print("2. koop schild (40 goud)")
    print("3. koop drankje (20 goud)")
    print("4. koop boog (60 goud)")
    print("5. bekijk je spullen")
    print("6. stoppen")

    choice = input("\nwat kies je? ")
    match choice:
        case "1":
            item = "zwaard"
            price = 50

        case "2":
            item = "schild"
            price = 40

        case "3":
            item = "drankje"
            price = 20

        case "4":
            item = "boog"
            price = 60

        case "5":
            if inventory == []:
                print("je hebt nog niks gekocht")
            else:
                print("je spullen:")
                for item in inventory:
                    print(f"- {item}")
            continue

        case "6":
            print(f"doei {player_name}")
            print(f"je hebt nog {player_gold} goud")
            break

        case _:
            print("kies iets van 1 tot 6")
            continue

    if player_gold >= price:
        player_gold = player_gold - price
        inventory.append(item)
        print(f"je hebt een {item} gekocht")
        print(f"goud over: {player_gold}")
    else:
        print("je hebt te weinig goud")
