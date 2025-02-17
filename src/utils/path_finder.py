import heapq

class PATH_FINDER:
    @staticmethod
    def __heuristic__(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    @staticmethod
    def have_path(start, goal, grid):
        rows, cols = len(grid), len(grid[0])

        if grid[start[0]][start[1]] != 0.0 or grid[goal[0]][goal[1]] != 0.0:
            return False

        open_set = []
        heapq.heappush(open_set, (0, start))
        came_from = {}
        g_score = { (x, y): float('inf') for x in range(rows) for y in range(cols) }
        g_score[start] = 0
        f_score = { (x, y): float('inf') for x in range(rows) for y in range(cols) }
        f_score[start] = PATH_FINDER.__heuristic__(start, goal)

        while open_set:
            _, current = heapq.heappop(open_set)

            if current == goal:
                return True

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                neighbor = (current[0] + dx, current[1] + dy)

                if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
                    if grid[neighbor[0]][neighbor[1]] != 0.0:
                        continue

                    tentative_g_score = g_score[current] + 1

                    if tentative_g_score < g_score[neighbor]:
                        came_from[neighbor] = current
                        g_score[neighbor] = tentative_g_score
                        f_score[neighbor] = tentative_g_score + PATH_FINDER.__heuristic__(neighbor, goal)
                        heapq.heappush(open_set, (f_score[neighbor], neighbor))

        return False
