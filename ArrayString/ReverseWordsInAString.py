
class Solution(object):
    def reverseWords(self, s):
        reverse = [word for word in s.split(" ") if word]
        return " ".join(reverse[::-1])