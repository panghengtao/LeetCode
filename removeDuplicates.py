# -*- coding: utf-8 -*-
__author__ = "PANGHENGTAO"
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums :
            return 0
        tail = 0
        for i in range(len(nums)):
            if nums[i] != nums[tail]:
                tail += 1
                nums[tail] = nums[i]
        return tail + 1