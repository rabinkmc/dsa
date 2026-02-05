from typing import List


class Solution:
    def maxArea(self, coords: List[List[int]]) -> int:
        xmin = 1000001
        ymin = 1000001
        xmax = 0
        ymax = 0
        xaxis = {}
        yaxis = {}

        area = -1
        for x, y in coords:
            xmin = min(xmin, x)
            ymin = min(ymin, y)
            xmax = max(xmax, x)
            ymax = max(ymax, y)

        for x, y in coords:
            if x not in yaxis:
                yaxis[x] = (y, y)
            else:
                cmin, cmax = yaxis[x]
                yaxis[x] = (min(y, cmin), max(y, cmax))
                base = abs(yaxis[x][1] - yaxis[x][0])
                height = max(abs(x-xmin), abs(x-xmax))
                area = max(area, base * height)

            if y not in xaxis:
                xaxis[y] = (x, x)
            else:
                cmin, cmax = xaxis[y]
                xaxis[y] = (min(x, cmin), max(x, cmax))
                base = abs(xaxis[y][1] - xaxis[y][0])
                height = max(abs(y-ymin), abs(y-ymax))
                area = max(area, base * height)

        if area <= 0:
            return -1
        return area

        

coords = [[1,1],[1,2],[3,2],[3,3]]
coords = [[1, 1], [6, 10], [6, 5]]
print(Solution().maxArea(coords))
