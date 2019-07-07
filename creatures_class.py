import numpy
import random
import object_read

class BuildCreature:
    """
    The general idea is, every creature in this world has the following 
    ten attributes:
    id, name, attack, defense, speed, hp, skill 1, skill 2, drop 1, drop 2.

    Additionally, the object should also have level attribute.

    The same creature with same level may have the same base attributes, 
    but they may have various random tiny difference.

    Therefore, when creating a creature, the script would read the db 
    file and get all base values. Then those base data go through a 
    complex computation and a creature object will be instantiated.

    Just remember to del the object once finish using.
    """

    def __init__(self, file_path, creature_id, creature_level=1):
        """
        Constructor

        Parameters
        ----------
        file_path: string
            The relative location of the db file.

        creature_id: integer
            The unique creature id.

        creature_level: integer or string
            The creature level.
        """
        self.id = creature_id
        self.level = creature_level
        one_creature = object_read.read_one_creature_by_id(file_path, 
                                                            creature_id)
        self.name = one_creature[1]
        self.attack = one_creature[2]
        self.defense = one_creature[3]
        self.speed = one_creature[4]
        self.hp = one_creature[5]
        self.skill1 = one_creature[6]
        self.skill2 = one_creature[7]
        self.drop1 = one_creature[8]
        self.drop2 = one_creature[9]

    def __del__(self):
        pass

if __name__ == '__main__':
    print('Please import this module to instantiate classes.')