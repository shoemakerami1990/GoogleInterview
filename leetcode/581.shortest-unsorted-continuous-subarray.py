class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        l, i = 0, 0
        for i in range(1, n):
            if nums[i]<nums[i-1]:
                l = i
                break

        for i in range(i, n):
            while l>=0 and nums[i]<nums[l]:
                l-=1

        r, i = n-1, n-1
        for i in range(n-2, -1, -1):
            if nums[i]<nums[i+1]:
                r = i
                break

        for i in range(i, -1, -1):
            while r<n and nums[i]>nums[r]:
                r+=1

        return r-l+1
