class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        l, i = n-1, 0
        for i in range(1, n):
            if nums[i]<nums[i-1]:
                l = i-1
                break

        for i in range(i+1, n):
            while l>0 and nums[i]<nums[l-1]:
                l-=1

        r, i = 0, n-1
        for i in range(n-2, -1, -1):
            if nums[i]>nums[i+1]:
                r = i+1
                break

        for i in range(i-1, -1, -1):
            while r<n-1 and nums[i]>nums[r+1]:
                r+=1

        return r-l+1 if r-l>0 else 0
