from ini import *
from random import randint
import string

def reset_status():
    global stre,inte,agi,defe,fai,san,luc,head,arm,weap,foot
    player_name=''
    stre=''
    inte=''
    agi=''
    defe=''
    fai=''
    san=''
    luc=''
    head=''
    arm=''
    weap=''
    foot=''
    return

def random_generate_status():
    global stre,inte,agi,defe,fai,san,luc,head,arm,weap,foot
    stre=str(randint(1,15))
    inte=str(randint(1,15))
    agi=str(randint(2,15))
    defe=str(randint(3,15))
    fai=str(randint(5,15))
    san=str(randint(20,40))
    luc=str(randint(1,10))
    head='Casual Hat'
    arm='Casual Cloth'
    weap='Twig'
    foot='Casual Shoes'
    return

def get_from_array(arr):
    global player_name,stre,inte,agi,defe,fai,san,luc,head,arm,weap,foot
    player_name=arr[0]
    g_stre=arr[1]
    inte=arr[2]
    agi=arr[3]
    defe=arr[4]
    fai=arr[5]
    san=arr[6]
    luc=arr[7]
    head=arr[8]
    arm=arr[9]
    weap=arr[10]
    foot=arr[11]
    return

def Remap(Old_Min,Old_Max,New_Min,New_Max):
    # don't need it now, may be usefull in the future
    return
