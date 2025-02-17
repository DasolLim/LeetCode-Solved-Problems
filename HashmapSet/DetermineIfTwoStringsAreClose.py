from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        word1_set = set(word1)
        c1, c2 = [], []

        if len(word1)!=len(word2): return False
        # Count character in both words
        # count1, count2 = Counter(word1), Counter(word2)

        # Check the sets of unique characters 
        # if set(count1.keys()) != set(count2.keys()):
        #     return False

        # return sorted(count1.values()) == sorted(count2.values())

        for c in word1_set:
            # Count & add the sets of unique characters 
            c1.append(word1.count(c))
            c2.append(word2.count(c))

        return sorted(c1)==sorted(c2)
