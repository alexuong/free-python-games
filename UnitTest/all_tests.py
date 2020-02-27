"""
all_test.py calls all tests within the UnitTest directory.

"""

import glob
import unittest


def create_test_suite():
    # Automatically add all tests
    test_file_strings = glob.glob('UnitTest/test_*.py')
    module_strings = ['UnitTest.'+str[9:len(str)-3] for str in test_file_strings]
    suites = [unittest.defaultTestLoader.loadTestsFromName(name, module=None) \
        for name in module_strings]
    # Single Test Syntax
    #suites = unittest.defaultTestLoader.loadTestFromName('UnitTest.test_utils', \
    #    module=None)
    testSuite = unittest.TestSuite(suites)
    return testSuite