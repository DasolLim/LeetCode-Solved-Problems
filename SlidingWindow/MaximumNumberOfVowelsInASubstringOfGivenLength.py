class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = {'a', 'e', 'i', 'o', 'u'}
        l, count, result = 0, 0, 0

        for r in range(len(s)):

            if s[r] in vowel:
                count += 1

            if r - l + 1 > k:
                if s[l] in vowel:
                    count -= 1
                l += 1
            result = max(result, count)
            
        return result



                


        
