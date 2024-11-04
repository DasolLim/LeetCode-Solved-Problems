class Solution(object):
    def maxArea(self, height):
        n = len(height)
        l = 0
        r = n - 1
        max_area = 0

        while l < r:
            w = r - l 
            # h = min(height[l], height[r])
            # area = w * h 
            
            if height[l] < height[r]: # calculate using min(height[l], height[r])
                area = w * height[l]
                l += 1
            else:
                area = w * height[r]
                r -= 1

            # max_area = max(max_area, area)
            if area > max_area:
                max_area = area

            # if height[l] < height[r]:
            #     l += 1
            # else: 
            #     r -= 1

        return max_area
        