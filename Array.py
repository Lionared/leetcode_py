# -*- coding: utf-8 -*-
def twoSum(nums, target):
    """
    No. 1 Two Sum | easy
	给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
	你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。
	Given an array of integers, return indices of the two numbers such that they add up to a specific target.
	You may assume that each input would have exactly one solution, and you may not use the same element twice.
	Example:
	Given nums = [2, 7, 11, 15], target = 9,
	Because nums[0] + nums[1] = 2 + 7 = 9,
	return [0, 1].
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    ret = []
    i, j = 0,1
    for i in range(len(nums)):
        if nums[i] + nums[j] == target:
            ret[0] = nums[i]
            ret[1] = nums[j]
            return ret
        else:
            j += 1

def RemoveElement(nums, val):
    """
    No. 27 Remove Element | easy
    给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。
    不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
    元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
    示例 1:
    给定 nums = [3,2,2,3], val = 3,
    函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。
    你不需要考虑数组中超出新长度后面的元素。
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
