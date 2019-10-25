import random
from ..models import Character


def battle(ch1: Character, ch2: Character) -> Character:
    """
    Make battle with two players, winner calc from character's BP (battle power)
    :param ch1: First character
    :param ch2: Second character
    :return: Winner character
    """
    bp1 = ch1.bp
    bp2 = ch2.bp

    ratio = bp1 / bp2
    random_percent = random.randint(1, 100)

    # difference
    # df2 = abs(bp1 - bp2) / max(bp1, bp2)

    # if bp's are equal - random winner
    if ratio == 1:
        if random_percent <= 50:
            return ch1
        else:
            return ch2

    # if one of bp's higher more then 25%, then auto winner
    # ratio 1.25 and 0.8 equal to 25% difference max(a,b)/min(a,b)
    if ratio >= 1.25:
        return ch1
    if ratio <= 0.8:
        return ch2

    # random seed + percent from bigger bp
    if random_percent <= 50 * ratio:
        return ch1
    else:
        return ch2
