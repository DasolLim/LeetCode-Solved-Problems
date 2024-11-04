class Solution(object):
    def isSubsequence(self, s, t):

        # empty string
        if not s:  
            return True

        r = 0

        for c in range(len(t)):
            if s[r] == t[c]:
                r += 1
            
            # if all s is in t
            if r == len(s):
                return True
        
        # check if s is in t
        return r == len(s)
