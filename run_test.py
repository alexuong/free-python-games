"""
This is the main for free-python-games unit testing suite.

This script calls all_tests.py, and generates the test runner.
"""
import unittest
from UnitTest.all_tests import create_test_suite
import getpass
import socket
import datetime

logfile = 'UnitTestResults.txt'
f = open(logfile, 'w')
f.write('''
********************************************************************************
********************free-python-games Unit Testing******************************
********************************************************************************
''')
f.write('Username:                  ' + getpass.getuser() + '\n')
f.write('Computer Name:             ' + socket.gethostname() + '\n')
f.write('Run Date:                  ' + str(datetime.datetime.today()) + '\n')
testSuite = create_test_suite()
test_runner = unittest.TextTestRunner(stream=f, verbosity=2).run(testSuite)
f.close()

if __name__ == '__main__':
    unittest.main()