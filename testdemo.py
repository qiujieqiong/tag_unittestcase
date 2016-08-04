#/usr/bin/env python
#encoding:utf-8

import unittest
import sys
from time import sleep
from dogtail.tree import *
from Infos import *
import pyautogui


def exit_launcher():
    name = get_actived_win_name()
    if name=='dde-launcher':
        print 'launcher opened!'
        pyautogui.press('esc')

class My_test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.screenWidth, cls.screenHeight = pyautogui.size()

    @classmethod
    def tearDown(cls):
        pass
    @tag("57636")
    def test_launcher_start_up1(self):
        app = root.application(appName='dde-dock', description='/usr/bin/dde-dock')
        app.child('Launcher').click()
        name = get_actived_win_name()
        self.assertEqual(name,'dde-launcher')
        exit_launcher()

    def test_launcher_start_up2(self):
        pyautogui.press('winleft')
        name = get_actived_win_name()
        self.assertEqual(name,'dde-launcher')
        exit_launcher()
    @tag('57646')
    def test_launcher_start_up3(self):
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
    @tag('57649')
    def test_launcher_start_up4(self):
        pyautogui.hotkey('ctrl','alt','t')
        sleep(2)
        name = get_actived_win_name()
        self.assertEqual(name,'Deepin Terminal')
        pyautogui.typewrite('dde-launcher -s',interval=0.25)
        pyautogui.press('enter')
        name = get_actived_win_name()
        self.assertEqual(name,'dde-launcher')
        exit_launcher()
        pyautogui.hotkey('alt','f4')
    #@tag('57646')


    #@tag('57649')


    #@tag('57652')


    #@tag('57720')


    #@tag('57722')


    #@tag('57724')


def suite():
    suite = unittest.TestSuite()
    casesID = get_data()
    if '57636' in casesID:
        suite.addTest(My_test('test_launcher_start_up'))
    if '57646' in casesID:
        suite.addTest(My_test('test_launcher_start_up3'))
    if '57649' in casesID:
        suite.addTest(My_test('test_launcher_start_up4'))
    if '57652' in casesID:
        suite.addTest(My_test('test_method4'))
    if '57720' in casesID:
        suite.addTest(My_test('test_method5'))
    if '57722' in casesID:
        suite.addTest(My_test('test_method6'))
    if '57724' in casesID:
        suite.addTest(My_test('test_method7'))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='suite',verbosity=2)
