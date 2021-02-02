class Solution(object):
    def mostCompetitive(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        N = len(nums)
        stack = []
        
        for i, n in enumerate(nums):
            rem_n = N - i
            while stack and stack[-1] > n and rem_n > k - len(stack):
                stack.pop()
            if len(stack) < k:
			    stack.append(n)
        return stack
