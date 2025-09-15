"""
Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
"""


class Solution(object):
    def findMaxAverage(self, nums, k):
        avg=0
        max=0
        sum=0
        for i in range(4):
            sum=nums[i]+sum
        max=sum

        for i in range(k,nums+1):
            sum




s=Solution()
nums = [1,12,-5,-6,50,3]
k = 4
s.findMaxAverage(nums,k)