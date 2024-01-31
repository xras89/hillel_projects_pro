from typing import Generator


class Player:
    def __init__(self, first_name: str, last_name: str):
        self.first_name: str = first_name
        self.last_name: str = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


team: list[Player] = [
    Player("John", "Smith"),
    Player("Marry", "Smith"),
    Player("Jack", "Hill"),
    Player("Nick", "Doe"),
    Player("John", "Doe"),
    Player("Marry", "Doe"),
]


for player in team:
    print(player)

# Output:
# John Smith
# Marry Smith
# Jack Hill
# Nick Doe
# John Doe

print("*" * 15)


def dedup(collection) -> Generator[str, None, None]:
    # TODO: Complete this function
    uniq_name = []
    for player in collection:
        if player.first_name not in uniq_name:
            uniq_name.append(player.first_name)
            yield player


for player in dedup(team):
    print(player)

# Expected Output:
# John Smith
# Marry Smith
# Jack Hill
# Nick Doe

# Explaination:
# The dedup function should return a generator
# that yields the unique players in the team.
# The uniqueness of a player is determined by its first name only

# Объяснение:
# Функция dedup должна возвращать генератор,
# который выдает уникальных игроков в команде.
# Уникальность игрока определяется только его первым именем
