class Solution(object):
    def pivotIndex(self, nums):
        l_sum = 0   
        total = sum(nums)

        for i in range(len(nums)):
            r_sum = total - nums[i] - l_sum
            if l_sum == r_sum:
                return i
            l_sum += nums[i]
        
        return -1
            
            
