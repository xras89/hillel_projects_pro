# CRUD (Create Read Update Delete) operations

# Database representation
team: list[dict] = [
    {"name": "John", "age": 20, "number": 1},
    {"name": "Mark", "age": 33, "number": 3},
    {"name": "Cavin", "age": 31, "number": 12},
]


# Application source code
def repr_players(players: list[dict]):
    for player in players:
        print(
            f"\t[Player {player['number']}]: {player['name']},{player['age']}"
        )


def player_update(name: str, age: int, number: int) -> dict:
    for player in team:
        if player["number"] == number:
            player["name"] = name
            player["age"] = age


def player_add(name: str, age: int, number: int) -> dict:
    for player in team:
        if player["number"] == number:
            print(
                "We already have that player's number on the team,"
                " plese input another number"
            )
            return player
    else:
        player: dict = {
            "name": name,
            "age": age,
            "number": number,
        }
        team.append(player)

    return player


def player_delete(number: int) -> None:
    global team
    team = [d for d in team if d.get("number") != number]


def main():
    operations = ("add", "del", "repr", "exit", "upd")

    while True:
        operation = input("Please enter the operation: ")
        if operation not in operations:
            print(f"Operation: '{operation}' is not available\n")
            continue

        if operation == "exit":
            print("Bye")
            break
        elif operation == "repr":
            repr_players(team)
        elif operation == "add":
            user_data = input(
                "Enter new player information[name,age,number]: "
            )
            # Input: 'Clark,19,22'
            user_items: list[str] = user_data.split(",")
            # Result: ['Clark', '19', '22']
            name, age, number = user_items
            try:
                player_add(name=name, age=int(age), number=int(number))
            except ValueError:
                print("Age and number of player must be integers\n\n")
                continue
        elif operation == "upd":
            repr_players(team)
            num_user_upd = int(
                input("Enter the number of the player you want to update: ")
            )
            list_of_num = [item["number"] for item in team]
            if num_user_upd in list_of_num:
                new_input_name_age = input(
                    "Enter new player information [name, age]: "
                ).split(",")
                new_name, new_age = new_input_name_age
                try:
                    player_update(new_name, int(new_age), num_user_upd)
                except ValueError:
                    print(
                        "Please enter an integer for the player's age and number\n\n"  # noqa
                    )
                    continue
                repr_players(team)
            else:
                print(
                    "This player's number isn't on the list."
                    " Use the 'add' function or select another player's number"
                )
                continue
        elif operation == "del":
            num_user_del = int(
                input("Enter the number of the player you want to delete: ")
            )
            player_delete(num_user_del)
        else:
            raise NotImplementedError


if __name__ == "__main__":
    main()
