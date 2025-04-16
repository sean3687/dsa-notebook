import random
# 56. Random Pick with Weight
# Yonghyun
class Solution:
    def __init__(self, w):
        self.expanded = []
        for i in range(len(w)):
            for _ in range(w[i]):
                self.expanded.append(i)

    def pickIndex(self):
        return random.choice(self.expanded)