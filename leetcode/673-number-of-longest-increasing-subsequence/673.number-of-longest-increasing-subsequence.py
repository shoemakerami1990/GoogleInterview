class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [1]*n
        longestNum = 1
        longest = 1
        for i in range(1, n):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
            if dp[i]>longest:
                longest = dp[i]
                longestNum = 1
            elif dp[i]==longest:
                longestNum+=1

        return longestNum
