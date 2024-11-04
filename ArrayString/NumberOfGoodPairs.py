class Solution(object):
    def numIdenticalPairs(self, nums):
        n = len(nums)
        counter = Counter(nums)
        good_pairs = 0

        for i, n in enumerate(nums):
            counter[n] -= 1
            good_pairs += counter[n]

        return good_pairs
        