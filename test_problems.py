'''Tests cases for Project Euler problems'''

import unittest
import sys
from glob import glob
from time import time


class TestProblems(unittest.TestCase):

    '''Generic class for testing problems of Project Euler'''

    @classmethod
    def setUpClass(cls):
        '''Set up the list for the test times'''

        cls.times = []

    @classmethod
    def tearDownClass(cls):
        '''Print test times'''

        print
        for test_time in cls.times:
            print test_time

    def setUp(self):
        '''Initialize start_time variable'''

        self.start_time = time()

    def tearDown(self):
        '''Calculate time spent in test and add it to the list'''

        time_spent = time() - self.start_time
        test_name = self.id().split('.')[-1]
        self.times.append("%s: %.3fs" % (test_name, time_spent))


def generate_test(problem):
    '''Dinamically generates a test case for a problem'''

    def test_problem(self):
        '''Check whether %s returns the expected result'''

        prob = __import__(problem)
        self.assertEqual(prob.solve(), prob.RESULT)

    test_problem.__doc__ %= problem

    return test_problem


def get_names(nums):
    '''Return the corret module names from the numbers given'''

    files = []

    for num in nums:
        for _ in xrange(3 - len(num)):
            num = '0%s' % num
        files.append('p%s' % num)

    return files


def get_all():
    '''Returns all the file names without the extension containing problems
    in the current directory'''

    files = []

    for f_name in glob('p???.py'):
        files.append(f_name[:4])

    return files


def run_tests(tests):
    '''Creates and runs test cases for the specified problems'''

    problems = []

    if not tests or 'all' in tests:
        problems = get_all()
    else:
        problems = get_names(tests)

    for problem in sorted(problems):
        setattr(TestProblems, 'test_%s' % problem, generate_test(problem))
    unittest.main()

if __name__ == '__main__':
    sys.argv, args = sys.argv[:1], sys.argv[1:]
    run_tests(args)
