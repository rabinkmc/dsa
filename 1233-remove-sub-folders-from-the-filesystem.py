from typing import List

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        visited = set()
        def subfolder(path):
            res = ""
            for ch in path:
                if ch == "/":
                    if res in visited:
                        return True
                res += ch
            return False
        ans = []
        for path in folder:
            if not subfolder(path):
                ans.append(path)
            visited.add(path)
        return ans
        
folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
print(Solution().removeSubfolders(folder))
