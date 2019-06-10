import random as rnd


def random_block():
    persent = rnd.random()
    if persent > 0.93:
        return rnd.randint(-2, -1)
        pass
    else:
        return rnd.randint(1, 7)
