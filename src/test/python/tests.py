import unittest
import suites

if __name__ == '__main__':
   suite = unittest.TestSuite()
   suite.addTest(suites.smallibs.suitcase.cases.suite())
   suite.addTest(suites.smallibs.suitcase.matchers.suite())
   unittest.TextTestRunner(verbosity=2).run(suite)
