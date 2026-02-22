def get_area(x1, x2, y1, y2):
    return abs(x1 - x2) * abs(y1 - y2)


class Solution:
    def computeArea(
        self,
        ax1: int,
        ay1: int,
        ax2: int,
        ay2: int,
        bx1: int,
        by1: int,
        bx2: int,
        by2: int,
    ) -> int:
        a1 = get_area(ax1, ax2, ay1, ay2)
        b1 = get_area(bx1, bx2, by1, by2)
        area = a1 + b1
        if ax2 < bx1 or bx2 < ax1:
            return area
        if ay2 < by1 or by2 < ay1:
            return area
        xr, xl = min(ax2, bx2), max(ax1, bx1)
        yr, yl = min(ay2, by2), max(ay1, by1)
        intersection = (xr - xl) * (yr - yl)
        return area - intersection
