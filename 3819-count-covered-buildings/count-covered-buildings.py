class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        result = 0
        dx = {}
        dy = {}

        for building in buildings:
            x, y = building[0], building[1]
            if x not in dx:
                dx[x] = []
            dx[x].append(y)
            if y not in dy:
                dy[y] = []
            dy[y].append(x)

        for x, l in dx.items():
            l.sort()
            if len(l) > 2:
                for y in l[1:-1]:
                    dy[y].sort()
                    result += (
                        len(dy[y]) > 2 and dy[y][0] != x and dy[y][len(dy[y]) - 1] != x
                    )
        return result
