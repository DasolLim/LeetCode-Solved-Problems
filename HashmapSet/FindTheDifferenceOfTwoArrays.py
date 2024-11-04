class Solution(object):
    def findDifference(self, nums1, nums2):
        h_nums1, h_nums2 = set(nums1), set(nums2)
        res1, res2 = set(), set() # does not contain duplicates

        for n in nums1:
            # add if distinct
            if n not in h_nums2:
                res1.add(n)

        for n in nums2:
            # add if distinct
            if n not in h_nums1:
                res2.add(n)

        # convert to hashmap to array
        return [list(res1), list(res2)]
        