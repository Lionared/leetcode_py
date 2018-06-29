# -*- coding: utf-8 -*-
import unittest
from Bit import *


class TestBit(unittest.TestCase):
    def test_HammingWeight(self):
        n = 11
        count = HammingWeight(n)
        self.assertEqual(count,3,"TestHammingWeight failed!")