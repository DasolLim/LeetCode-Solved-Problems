class Solution(object):
    def largestAltitude(self, gain):
        max_alt = 0
        alt = 0

        for i in range(len(gain)):
            alt += 0 + gain[i]
            max_alt = max(max_alt, alt)

        return max_alt