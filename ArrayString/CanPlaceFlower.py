class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        # for base case of [0,0,1]
        f = [0] + flowerbed + [0]

        for i in range(1, len(f) -1): # skip first and last
            # adjacent 0s
            if f[i-1] == 0 and f[i] == 0 and f[i+1] == 0:
                f[i] = 1
                n -= 1
                # early return
                if n <= 0:
                    return True
                
        return n <= 0

                
        