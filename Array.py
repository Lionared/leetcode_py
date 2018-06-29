# -*- coding: utf-8 -*-
def TwoSum(nums, target):
    """
    No.1. Two Sum | Easy
	Given an array of integers, return indices of the two numbers such that they add up to a specific target.
	You may assume that each input would have exactly one solution, and you may not use the same element twice.

	Example:
	Given nums = [2, 7, 11, 15], target = 9,
	Because nums[0] + nums[1] = 2 + 7 = 9,
	return [0, 1].

	两数之和:
	给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
	你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    dict = {}
    for index in range(len(nums)): #in python3, range = xrange
        now = nums[index]
        first = target - now
        if first in dict:
            return [dict[first],index]
        dict[now] = index
    else:
        return None

def findMedianSortedArrays(self, nums1, nums2):
    """
    No.4. Median of Two Sorted Arrays | Hard
    There are two sorted arrays nums1 and nums2 of size m and n respectively.
    Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

    Example 1:
    nums1 = [1, 3]
    nums2 = [2]
    The median is 2.0

    两个排序数组的中位数:
    给定两个大小为 m 和 n 的有序数组 nums1 和 nums2 。
    请找出这两个有序数组的中位数。要求算法的时间复杂度为 O(log (m+n)) 。
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    pass

def RemoveElement(nums, val):
    """
    No.27. Remove Element | Easy
    Given an array nums and a value val, remove all instances of that value in-place and return the new length.
    Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
    The order of elements can be changed. It doesn't matter what you leave beyond the new length.

    Example 1:
    Given nums = [3,2,2,3], val = 3,
    Your function should return length = 2, with the first two elements of nums being 2.
    It doesn't matter what you leave beyond the returned length.

    移除元素:
    给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。
    不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
    元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    i, j = 0,0
    for i in range(len(nums)):
        if nums[i] == val:
            continue
        nums[j] = nums[i]
        j += 1
    else:
        return j
