#/usr/bin/env python

import unittest
import testdemo
import re

suite1 = testdemo.suite()

alltests = unittest.TestSuite((suite1))

if __name__ == '__main__':
	with open('test.result_bak', 'w') as logf:
		unittest.TextTestRunner(stream=logf,verbosity=2).run(alltests)
	logf.close()
	with open('test.result_bak', 'r') as f1:
		lines = f1.readlines()
	buff = ''
	for line in lines:
		if line.find('#') and line.find('...') == -1:
			continue
		else:
			index = line.find('#')
			line = line[index+1:-1].replace('...','')
			if line.find('ok') != -1:
				line = line.replace('ok','Pass')
			elif line.find('FAIL') != -1:
				line = line.replace('FAIL','Fail')
			line = re.sub(' +',' ',line)
			print line
			buff+=line+'\n'
	f1.close()
	with open('test.result', 'w') as f2:
		f2.write(buff)
	f2.close()
