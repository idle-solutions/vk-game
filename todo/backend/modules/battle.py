import random


def battle():
    player_1 = {
        "id": 123123,
        "nickname": "Vasya",
        "level": 7,
        "power": 6,
        "health": 40,
    }
    player_2 = {
        "id": 1123444,
        "nickname": "Petya",
        "level": 8,
        "power": 6,
        "health": 40,
    }
    bp1 = player_1["level"] * 100
    bp2 = player_2["level"] * 100

    diff = bp1 / bp2
    r1 = random.randint(1, 100)
    winner = ""

    if diff == 1:
        if r1 <= 50:
            winner = player_1["nickname"]
        else:
            winner = player_2["nickname"]

    if diff >= 1.25:
        winner = player_1["nickname"]
    if diff <= 0.8:
        winner = player_2["nickname"]

    else:
        if r1 <= 50 * diff:
            winner = player_1["nickname"]
        else:
            winner = player_2["nickname"]

    return winner


for i in range(20):
    battle()
