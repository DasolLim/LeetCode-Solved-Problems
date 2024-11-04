# Move Zeros Solution
class Solution(object):
    def moveZeroes(self, nums):
        l = 0 
        # use right to iterate
        for r in range(len(nums)):
            if nums[r]:
                #swap
                nums [l], nums[r] = nums[r], nums[l]
                # increment
                l += 1
        return nums

        