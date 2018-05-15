class Solution:
    def twoSum(self, nums, target):
        for i in nums:
            if target-i in nums[nums.index(i)+1:]:
                break
        return [nums.index(i),nums.index(i)   +    nums[nums.index(i)+1:].index(target-i) + 1]

#supporting code
print(Solution.twoSum(10,[3,2,1,3],6))