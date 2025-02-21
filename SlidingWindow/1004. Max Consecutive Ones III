class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # l, cnt_zero, result = 0,0,0

        # for r in range(len(nums)):
        #     if nums[r] == 0:
        #         cnt_zero += 1

        #     while cnt_zero > k:
        #         if nums[l] == 0:
        #             cnt_zero -= 1
        #         l += 1
        #     one_length = r - l + 1

        #     result = max(result, one_length)

        # return result

# Time Complexity: O(n)
# Space Complexity: O(1)

        l = 0
        for r in range(len(nums)):
            if nums[r] == 0: 
                k -= 1
            if k < 0:
                if nums[l] == 0: 
                    k += 1
                l += 1
        
        return r - l + 1

# Time Complexity: O(n)
# Space Complexity: O(1)             
