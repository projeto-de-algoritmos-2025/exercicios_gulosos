class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        def get_cost(digits):
            pos = startAt
            cost = 0
            for d in digits:
                if d != pos:
                    cost += moveCost
                    pos = d
                cost += pushCost
            return cost

        min_cost = float('inf')

        # Tentar todas as combinações de minutos de 0 até 99
        for minutes in range(100):
            seconds = targetSeconds - minutes * 60
            if 0 <= seconds <= 99:
                time_str = f"{minutes:02d}{seconds:02d}".lstrip("0")
                if not time_str:
                    time_str = "0"
                digits = [int(ch) for ch in time_str]
                min_cost = min(min_cost, get_cost(digits))

        return min_cost
