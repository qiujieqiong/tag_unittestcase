#/usr/bin/env python
#encoding:utf-8

import unittest
import sys
from time import sleep
from dogtail.tree import *
from dogtail.predicate import GenericPredicate
from Infos import *
import pyautogui


class My_test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.screenWidth, cls.screenHeight = pyautogui.size()

    @classmethod
    def tearDown(cls):
        pass
    @tag("57636")
    def test_launcher_start_up(self):
        #startup1
        app = root.application(appName='dde-dock', description='/usr/bin/dde-dock')
        app.child('Launcher').click()
        name = get_actived_win_name()
        self.assertEqual(name,'dde-launcher')
        exit_launcher()

        #startup2
        pyautogui.press('winleft')
        name = get_actived_win_name()
        self.assertEqual(name,'dde-launcher')
        exit_launcher()

        #startup3
        pyautogui.moveTo(self.screenWidth/2, self.screenHeight/2)
        pyautogui.click(button='right')
        pyautogui.press('c')
        pyautogui.moveTo(0, self.screenHeight)
        launcher_coor = getHotAreaLauncherCoor()
        pyautogui.moveTo(launcher_coor)
        pyautogui.click()
        pyautogui.press('esc')
        pyautogui.moveTo(0, self.screenHeight)
        name = get_actived_win_name()
        self.assertEqual(name,'dde-launcher')
        exit_launcher()

        #startup4
        pyautogui.hotkey('ctrl','alt','t')
        if GetInfo().loop():
            print "Deepin Terminal Opend!"
            name = get_actived_win_name()
            self.assertEqual(name,'Deepin Terminal')
        else:
            raise Exception("Deepin Terminal did not opened!")
        sleep(1)
        pyautogui.typewrite('dde-launcher -s\n',interval=0.25)
        sleep(1)
        name = get_actived_win_name()
        self.assertEqual(name,'dde-launcher')
        exit_launcher()
        pyautogui.hotkey('alt','f4')

    @tag('57646')
    def test_launcher_search(self):
        launcherSearchDeepin()
        deepinItems = getdeepinItems()
        exit_launcher()
        items = getLauncherItems()
        self.assertListEqual(deepinItems,items)

    @tag('57649')
    def test_launcher_operation(self):
        #open

        imageviewer_rightKey()
        pyautogui.press('o')
        if GetInfo().loop():
            print "Deepin Store Opened!"
            name = get_actived_win_name()
            self.assertIn('Deepin Store', name)
            if name != 'dde-desktop':
                pyautogui.hotkey('alt','f4')
        else:
            raise Exception("Deepin Store did not opened!")

        #send to desktop
        imageviewer_rightKey()
        pyautogui.press(['down','down','enter'])
        exit_launcher()
        desktopfiles = getDesktopFiles()
        self.assertIn('eog.desktop', desktopfiles)

        #remove from desktop
        imageviewer_rightKey()
        pyautogui.press(['down','down','enter'])
        exit_launcher()
        desktopfiles = getDesktopFiles()
        self.assertNotIn('eog.desktop', desktopfiles)

        #undock
        imageviewer_rightKey()
        pyautogui.press(['down','down','down','enter'])
        exit_launcher()
        apps = getDockedApps()
        self.assertNotIn('eog', apps)

        #dock
        imageviewer_rightKey()
        pyautogui.press(['down','down','down','enter'])
        exit_launcher()
        apps = getDockedApps()
        self.assertIn('eog', apps)

        #add to startup
        imageviewer_rightKey()
        pyautogui.press(['down','down','down','down','enter'])
        exit_launcher()
        feild = getStartupInfo()
        self.assertEqual(feild, 'Hidden=false')
        imageviewer_rightKey()
        pyautogui.press(['down','down','down','down','enter'])
        exit_launcher()
        feild = getStartupInfo()
        self.assertEqual(feild, 'Hidden=true')

        #uninstall
        imageviewer_rightKey()
        pyautogui.press(['down','down','down','down','down','enter'])
        clickUnintallBtn()
        exit_launcher()
        if GetInfo().loop():
            items = getLauncherItems()
            self.assertNotIn('Image Viewer',items)
            
    @tag('57652')
    def test_launcher_classify(self):
        pyautogui.press('winleft')
    	name = get_actived_win_name()
    	sleep(2)
    	if name == 'dde-launcher':
            clickToggleBtn()
            mode = getLauncherMode()
            self.assertEqual('\'category\'',mode)
            clickToggleBtn()
            mode = getLauncherMode()
            self.assertEqual('\'free\'',mode)
            exit_launcher()
        else:
            raise Exception('launcher Did not opened!')


    #@tag('57720')


    #@tag('57722')


    #@tag('57724')


def suite():
    suite = unittest.TestSuite()
    casesID = get_data()
    if '57636' in casesID:
        suite.addTest(My_test('test_launcher_start_up'))
    if '57646' in casesID:
        suite.addTest(My_test('test_launcher_search'))
    if '57649' in casesID:
        suite.addTest(My_test('test_launcher_operation'))
    if '57652' in casesID:
        suite.addTest(My_test('test_launcher_classify'))
    '''
    if '57720' in casesID:
        suite.addTest(My_test('test_launcher_classify'))
    if '57722' in casesID:
        suite.addTest(My_test('test_launcher_search'))
    if '57724' in casesID:
        suite.addTest(My_test('test_method7'))
    '''
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='suite',verbosity=2)
