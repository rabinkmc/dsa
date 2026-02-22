from typing import List
from collections import defaultdict


class Solution:
    def mostPopularCreator(
        self, creators: List[str], ids: List[str], views: List[int]
    ) -> List[List[str]]:
        n = len(creators)
        view_count = dict()
        tops = dict()
        max_views = 0
        for creator, id, view in zip(creators, ids, views):
            if creator in view_count:
                view_count[creator] += view
                case1 = (view == tops[creator][0]) and id < tops[creator][1]
                case2 = view > tops[creator][0]
                if case1 or case2:
                    tops[creator] = (view, id)
            else:
                view_count[creator] = view
                tops[creator] = (view, id)
            max_views = max(max_views, view_count[creator])
        out = []
        for creator, views in view_count.items():
            if views == max_views:
                top = tops[creator][1]
                out.append([creator, top])
        return out


creators = ["alice", "bob", "alice", "chris"]
ids = ["one", "two", "three", "four"]
views = [5, 10, 5, 4]
ans = Solution().mostPopularCreator(creators, ids, views)
print(ans)
