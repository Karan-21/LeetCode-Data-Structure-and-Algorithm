class Solution:
    def robotSim(self, commands, obstacles):
        st = set()
        
        for x, y in obstacles:
            st.add((x, y))

        dir = [(0,1), (1,0), (0,-1), (-1,0)]

        x = y = 0
        d = 0
        maxDist = 0

        for cmd in commands:
            if cmd == -1:
                d = (d + 1) % 4
            elif cmd == -2:
                d = (d + 3) % 4
            else:
                for _ in range(cmd):
                    nx = x + dir[d][0]
                    ny = y + dir[d][1]

                    if (nx, ny) in st:
                        break

                    x, y = nx, ny
                    maxDist = max(maxDist, x*x + y*y)

        return maxDist
