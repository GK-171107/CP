class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s = sorted(set(nums))
        longest = 1
        current = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1] + 1:
                current += 1
            else:
                current = 1
            longest = max(longest, current)
        return longest