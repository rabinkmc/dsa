class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        def digit_sum(n):
            rv = 0
            while n:
                rv += n % 10
                n = n // 10
            return rv

        boxes = dict()
        for i in range(lowLimit, highLimit + 1):
            box = digit_sum(i)
            boxes[box] = boxes.get(box, 0) + 1
        balls = sorted(boxes.values())
        return balls[-1]
