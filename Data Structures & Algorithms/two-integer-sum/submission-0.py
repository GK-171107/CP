class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        c = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    c.extend([i, j])
                    if len(c) == 2:
                        break
        return list(c)