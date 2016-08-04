#/usr/bin/env python
#encoding:utf-8

import subprocess
import json



def tag(*args, **kwargs):
    """Decorator that adds attributes to classes or functions
    for use with the Attribute (-a) plugin. It also renames functions!
    """
    def wrap_ob(ob):
        for id in args:
            setattr(ob, id, True)
            #using __doc__ instead of __name__ works for class methods tests
            ob.__doc__ = '#'.join([ob.__name__, id])
            #ob.__name__ = '_'.join([ob.__name__, name])

        return ob

    return wrap_ob

def get_data():
    with open('lava-test.json','r') as f:
        info = json.load(f)
        casesID = info['actions'][2]['parameters']['testdef_repos'][0]['parameters']['CASE_ID']
    f.close()
    return casesID

def get_actived_win_name():
	winName = subprocess.check_output(["xdotool getactivewindow getwindowname"],shell=True).decode().split("\n")
	winName = [ n for n in winName if len(n.strip()) > 0]
	winName = ''.join(winName)
	return winName

def getHotAreaLauncherCoor():
    up = 973
    left = 30
    width_item = 50
    height_item = 26
    item_x = left+width_item/2
    item_y = up+height_item/2
    return (item_x,item_y)
