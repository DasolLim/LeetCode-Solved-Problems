from collections import deque

class RecentCounter:

    def __init__(self):
        self.q = deque()

    def ping(self, t):
        self.q.append(t)
        # Remove all elements that are outside the [t - 3000, t] range
        while self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)

# Example usage:
# obj = RecentCounter()
# param_1 = obj.ping(t)
