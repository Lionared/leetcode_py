import unittest
from Array import twoSum,RemoveElement

class TestArray(unittest.TestCase):
    def test_init(self):
        pass

    def test_twoSum(self):
        nums = [2, 7, 11, 15]
        target = 9
        found = twoSum(nums,target)
        self.assertEqual(found,[2,7],"twoSum test failed!")

    def test_RemoveElement(self):
        array = [0,1,2,2,3,0,4,2]
        value = 2
        newLength = RemoveElement(array, value)
        self.assertEqual(newLength,5,"Removed array Element and new length is not 5")
