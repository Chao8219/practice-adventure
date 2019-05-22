import numpy
from random import randint

class PlayerClass:
    """This class is for storing information for one player.

    Attributes:
    name: string 
        player's name, which should be unique.
    attr: ndarray
        player's attributes, which includes stre, inte, agi, defe, fai, 
        san, luc.
    armor: ndarray
        player's armors, which includes head, body, weap, foot
    stre: string
        strength
    inte: string
        intelligence
    agi: string
        agility
    defe: string
        defence
    fai: string
        faith
    san: string
        sanity
    luc: string
        lucy
    head: string
        head-wear
    body: string
        body-wear
    weap: string
        weapon
    foot: string
        foot-wear

    """
    name = ''
    attr = numpy.array(['', '', '', '', '', '', ''], dtype='<U256')
    armor = numpy.array(['', '', '', ''], dtype='<U256')
    stre = ''
    inte = ''
    agi = ''
    defe = ''
    fai = ''
    san = ''
    luc = ''

    head = ''
    body = ''
    weap = ''
    foot = ''
    def __init__(self, name, attr, armor, *args, **kwargs):
        self.name = name
        self.attr = attr
        self.armor = armor
        return
    
    def gen_ran_attr(self, *args, **kwargs):
        """Generate Random Attributes"""
        self.stre = str(randint(1,15))
        self.inte = str(randint(1,15))
        self.agi = str(randint(2,15))
        self.defe = str(randint(3,15))
        self.fai = str(randint(5,15))
        self.san = str(randint(20,40))
        self.luc = str(randint(1,10))
        self.attr[:] = ([self.stre, self.inte, self.agi, self.defe, 
                         self.fai, self.san, self.luc])
        return
    
    def init_armor(self, *args, **kwargs):
        self.head = 'Casual Hat'
        self.body = 'Casual Cloth'
        self.weap = 'Twig'
        self.foot = 'Casual Shoes'
        self.armor[:] = ([self.head, self.body, self.weap, self.foot])

if __name__ == '__main__':
    print('Please import this file to intantiate this class.')