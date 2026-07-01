class Solution:
    def calPoints(self, operations: List[str]) -> int:
        points = []
        while operations:
            curr = operations.pop(0)
            match curr:
                case "+":
                    points.append(points[-1] + points[-2])
                case "D":
                    points.append(points[-1] * 2)
                case "C":
                    points.pop(-1)
                case _:
                    points.append(int(curr))

        return sum(points)