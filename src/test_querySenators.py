import unittest
import querySenators


class test_SenatorInfo(unittest.TestCase):

    def test_getName(self):
        testObj = querySenators.SenatorInfo("WY")
        self.assertEqual(testObj.getName(0), 'John Barrasso')

    def test_getTwitter(self):
        testObj = querySenators.SenatorInfo("TX")
        self.assertEqual(testObj.getTwitter(0), 'SenTedCruz')



if __name__ == "__main__":
    unittest.main()