from collections import deque

class Solution:
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
        n = len(status)
        visited = [False] * n
        have_key = set()
        have_box = set(initialBoxes)
        queue = deque()

        for box in initialBoxes:
            if status[box] == 1:
                queue.append(box)

        total_candies = 0

        while queue:
            box = queue.popleft()
            if visited[box]:
                continue
            visited[box] = True
            total_candies += candies[box]

            # Pega chaves novas
            for key in keys[box]:
                if key not in have_key:
                    have_key.add(key)
                    if key in have_box and not visited[key]:
                        queue.append(key)

            # Pega novas caixas
            for new_box in containedBoxes[box]:
                if new_box not in have_box:
                    have_box.add(new_box)
                if status[new_box] == 1 or new_box in have_key:
                    if not visited[new_box]:
                        queue.append(new_box)

        return total_candies

        