#/usr/bin/env python
#encoding:utf-8

import subprocess
from time import sleep
import json
from Xlib import X,display
from dogtail.tree import *
import pyautogui
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class GetInfo:

	def __init__(self):
		self.d = display.Display()
		self.root = self.d.screen().root
		self.root.change_attributes(event_mask = X.SubstructureNotifyMask)

	def loop(self):
		window_changed = False
		while True:
			event = self.d.next_event()
			if event.type == X.MapNotify:
				window_changed = True
				break
		return window_changed

def exit_launcher():
    name = get_actived_win_name()
    if name=='dde-launcher':
        print 'launcher opened!'
        pyautogui.press('esc')

def getDockedApps():
	apps = subprocess.check_output(["gsettings get com.deepin.dde.dock docked-apps"],shell=True).decode().split("\n")
	apps = [ n for n in apps if len(n.strip()) > 0]
	apps = ''.join(apps)
	return apps

def getDesktopFiles():
	userPath = os.path.expanduser('~')
	absDesktopPath = userPath + '/桌面'
	files = subprocess.check_output(["ls " +absDesktopPath],shell=True).decode().split("\n")
	files = [ n for n in files if len(n.strip()) > 0]
	files = ''.join(files)
	return files

def getStartupInfo():
	userPath = os.path.expanduser('~')
	absAutostartupPath = userPath + '/.config/deepin.eog'
	feild = subprocess.check_output(["cat " +absAutostartupPath+"|grep hidden"],shell=True).decode().split("\n")
	feild = [ n for n in feild if len(n.strip()) > 0]
	feild = ''.join(feild)
	return feild

def getLauncherItems():
	items = []
	launcherobj = root.application(appName='dde-launcher', description='/usr/bin/dde-launcher')
	launcheritems = launcherobj.child('all',roleName='list').children
	for i in range(len(launcheritems)):
		items.append(launcheritems[i].name)
	print items
	return items
def getdeepinItems():
	deepinItems = ['Deepin Cloud Print', 'Deepin Boot Maker', 'Deepin User Feedback', 'Deepin Terminal', 'Deepin Store',
					'Deepin Music', 'Deepin Screenshot', 'Remote Assistance', 'Multitasking View', 'Show Desktop', 'Control Center']
	return deepinItems

def getLauncherMode():
	mode = subprocess.check_output(["gsettings get com.deepin.dde.launcher display-mode"],shell=True).decode().split("\n")
	mode = [ n for n in mode if len(n.strip()) > 0]
	mode = ''.join(mode)
	return mode

def clickUnintallBtn():
	launcherobj = root.application(appName='dde-launcher', description='/usr/bin/dde-launcher')
	launcherobj.child('Confirm').click()

def clickToggleBtn():
	launcherobj = root.application(appName='dde-launcher', description='/usr/bin/dde-launcher')
	launcherobj.child('mode-toggle-button').click()

def launcherSearchDeepin():
	pyautogui.press('winleft')
	name = get_actived_win_name()
	sleep(2)
	if name == 'dde-launcher':
		launcherobj = root.application(appName='dde-launcher', description='/usr/bin/dde-launcher')
		launcherobj.child('search-edit').text = 'deepin'
	else:
		raise Exception("dde-launcher did not opened!")

def imageviewer_rightKey():
	pyautogui.press('winleft')
	name = get_actived_win_name()
	sleep(2)
	if name == 'dde-launcher':
		launcherobj = root.application(appName='dde-launcher', description='/usr/bin/dde-launcher')
		launcherobj.child('Image Viewer').click(3)
	else:
		raise Exception("dde-launcher did not opened!")


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
