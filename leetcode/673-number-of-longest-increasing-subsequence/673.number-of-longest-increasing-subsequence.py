class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n==0: return 0
        dp = [1]*n
        dpNum = [1]*n
        longest = 1
        for i in range(1, n):
            for j in range(i):
                if nums[i]>nums[j]:
                    if dp[i]<dp[j]+1:
                        dp[i]=dp[j]+1
                        dpNum[i]=dpNum[j]
                    elif dp[i]==dp[j]+1:
                        dpNum[i]+=dpNum[j]
            longest = max(longest, dp[i])

        return sum(dpNum[i] for i, l in enumerate(dp) if l==longest)
