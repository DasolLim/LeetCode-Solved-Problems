class Solution(object):
    def findMaxAverage(self, nums, k):
        # n = len(nums)
        # cur_avg = 0
        # max_avg = 0

        if k == 1 and len(nums) == 1:
            return nums[0]/float(k)

        # initial sliding window array average 0 -> k
        # for i in range(k):
        #     cur_avg += nums[i]
        # max_avg = cur_avg/float(k)

        cur_window = sum(nums[:k])    
        max_window = cur_window

        # k -> len(nums) by adding next int and removing 'first' int
        for i in range(k, len(nums)):
            cur_window += nums[i] - nums[i-k] # add the next integers and remove the 'first' integers
            max_window = max(max_window, cur_window)
    
        return max_window/float(k)

            
            

        