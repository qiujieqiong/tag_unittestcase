#/usr/bin/env python
#encoding:utf-8

import unittest
import sys
import json
#from nose.plugins.attrib import attr

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

class My_test(unittest.TestCase):
    @tag("57636")
    def test_method1(self):
        self.assertEqual(1,1)

    @tag('57646')
    def test_method2(self):
        self.assertEqual(1,1)

    @tag('57649')
    def test_method3(self):
        self.assertEqual(1,1)

    @tag('57652')
    def test_method4(self):
        self.assertEqual(1,1)

    @tag('57720')
    def test_method5(self):
        self.assertEqual(1,1)

    @tag('57722')
    def test_method6(self):
        self.assertEqual(1,1)

    @tag('57724')
    def test_method7(self):
        self.assertEqual(1,2)

def suite():
    suite = unittest.TestSuite()
    casesID = get_data()
    if '57636' in casesID:
        suite.addTest(My_test('test_method1'))
    if '57646' in casesID:
        suite.addTest(My_test('test_method2'))
    if '57649' in casesID:
        suite.addTest(My_test('test_method3'))
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
