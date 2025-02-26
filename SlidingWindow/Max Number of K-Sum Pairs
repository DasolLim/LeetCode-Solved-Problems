class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        result = 0

        for x in nums:
            if d[k-x] > 0:
                result += 1
                d[k-x] -= 1
            else:
                d[x] += 1
            
        return result


