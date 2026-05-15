class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        total = 0
        count = 0
        for event in events:
            match event:
                case "W":
                    count += 1
                    if count == 10:
                        return [total, count]
                case "WD":
                    total += 1
                case "NB":
                    total += 1
                case _:
                    num = int(event)
                    total += num
        return [total, count]
