class Solution(object):
    def uniqueOccurrences(self, arr):
        # Counter(): count the occurrences of elements
        # Ex: arr = [1,2,2,1,1,3]
        # counter = {{1:3, 2:2, 1:1}} <- dictionary 
        # since dictionary allow duplicates
        counter = Counter(arr)

        # if no Counter()
        # counter = {}
        # for i in arr:
        #     if i in counter():
        #         counter[i] += 1
        #     else:
        #         counter[i] = 1

        h = set()

        # iterate through the occurences, counter.values()
        # check for duplicate
        for i in counter.values():
            if i in h:
                return False
            else:
                h.add(i)

        return True
        