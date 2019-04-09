import unittest
import sys

sys.path.append("./src")
from querySenators import SenatorInfo


class test_SenatorInfo(unittest.TestCase):

    def setUp(self):
        self.testObj = SenatorInfo("TX")
    
    def tearDown(self):
        pass

    def test_getName(self):
        self.assertEqual(self.testObj.getName(0), 'Ted Cruz')
        self.assertEqual(self.testObj.getName(1), 'John Cornyn')
        self.assertEqual(self.testObj.getName(2), '')

    def test_getTwitter(self):      
        self.assertEqual(self.testObj.getTwitter(0), 'SenTedCruz')

if __name__ == "__main__":
    unittest.main()