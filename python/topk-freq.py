from typing import List
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        pq = []
        for key, value in Counter(words).items():
            heapq.heappush(pq, (-value, key))
        return [heapq.heappop(pq)[1] for _ in range(k)]

words = ["i","love","leetcode","i","love","coding"]
k = 2
# words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
# k = 4
ans = Solution().topKFrequent(words, k)
print(ans)
        
