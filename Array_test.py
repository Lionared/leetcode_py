# -*- coding: utf-8 -*-
import unittest
from Array import *


class TestArray(unittest.TestCase):
    def test_init(self):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_TwoSum(self):
        nums = [5,7,2,4,3,6,1]
        target = 5
        found = TwoSum(nums,target)
        self.assertEqual(found,[2,4],"test_TwoSum failed!")

    def test_RemoveElement(self):
        array = [0,1,2,2,3,0,4,2]
        value = 2
        newLength = RemoveElement(array, value)
        self.assertEqual(newLength,5,"test_RemoveElement failed!")
