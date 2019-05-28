import numpy
import random

class CreatePlayer:
    """This class is for storing information for one player.

    Attributes:
    name: string 
        player's name, which should be unique.
    attr: ndarray
        player's attributes, which includes stre, inte, agi, defe, fai, 
        san, luc.
    armor: ndarray
        player's armors, which includes head, body, weap, foot
    stre: float
        strength
    inte: float
        intelligence
    agi: float
        agility
    defe: float
        defence
    fai: float
        faith
    san: float
        sanity
    luc: float
        lucy
    head: string
        head-wear
    body: string
        body-wear
    weap: string
        weapon
    foot: string
        foot-wear
    health_value: float
        health value point, which ranges from 0 to 100
    """
    name = ''
    attr = numpy.zeros((1, 7))
    armor = numpy.array(['', '', '', ''], dtype='<U256')
    stre = 0.0
    inte = 0.0
    agi = 0.0
    defe = 0.0
    fai = 0.0
    san = 0.0
    luc = 0.0

    head = ''
    body = ''
    weap = ''
    foot = ''

    health_value = 100.0
    def __init__(self, name, new_born=True, *args):
        self.name = name
        if new_born is True:
            self.gen_ran_attr()
            self.init_armor()
        else:
            self.assign_values(*args)
        return
    
    def gen_ran_attr(self, *args, **kwargs):
        """Generate Random Attributes"""
        self.stre = random.uniform(1,15)
        self.inte = random.uniform(1,15)
        self.agi = random.uniform(2,15)
        self.defe = random.uniform(3,15)
        self.fai = random.uniform(5,15)
        self.san = random.uniform(20,40)
        self.luc = random.uniform(1,10)
        self.attr[:] = (self.stre, self.inte, self.agi, self.defe, 
                        self.fai, self.san, self.luc)
        return
    
    def init_armor(self, *args, **kwargs):
        self.head = 'Casual Hat'
        self.body = 'Casual Cloth'
        self.weap = 'Twig'
        self.foot = 'Casual Shoes'
        self.armor[:] = (self.head, self.body, self.weap, self.foot)
    
    def assign_values(self, player_info_list):
        self.name = player_info_list[0]
        self.stre = player_info_list[1]
        self.inte = player_info_list[2]
        self.agi = player_info_list[3]
        self.defe = player_info_list[4]
        self.fai = player_info_list[5]
        self.san = player_info_list[6]
        self.luc = player_info_list[7]
        self.attr[:] = (self.stre, self.inte, self.agi, self.defe, 
                        self.fai, self.san, self.luc)
        self.head = player_info_list[8]
        self.body = player_info_list[9]
        self.weap = player_info_list[10]
        self.foot = player_info_list[11]
        self.armor[:] = (self.head, self.body, self.weap, self.foot)

if __name__ == '__main__':
    print('Please import this file to intantiate this class.')