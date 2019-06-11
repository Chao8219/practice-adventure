import numpy
import random

class CreateGeneralBeing:
    """
    The general idea is, every creature in this world has the following 
    attributes:
    name, level, attack, defense, speed, hp, drops.

    The same creature with same level may have the same base attributes, 
    but they may have various random tiny difference.

    Therefore, when creating a creature, the script would read the db 
    file and get all base values. Then those base data go through a 
    complex computation and a creature object will be instantiated.

    Just remember to del the object once finish using.
    """
    def __init__(self):
        pass

    def __del__(self):
        pass

class CreateFoulBeing(CreateGeneralBeing):
    pass

if __name__ == '__main__':
    print('Please import this module to instantiate classes.')