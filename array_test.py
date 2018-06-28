import unittest
from Array import twoSum,RemoveElement

class TestArray(unittest.TestCase):
    def test_init(self):
        pass

    def test_twoSum(self):
        nums = [5,7,2,4,3,6,1]
        target = 5
        found = twoSum(nums,target)
        self.assertEqual(found,[2,4],"twoSum test failed!")

    def test_RemoveElement(self):
        array = [0,1,2,2,3,0,4,2]
        value = 2
        newLength = RemoveElement(array, value)
        self.assertEqual(newLength,5,"Removed array Element and new length is not 5")
