class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """
        Basic idea is we check each maximum capacity until we find a capacity which satisfies the condition.

        We can make it more efficient by binary searching
        """

        def can_ship(capacity):
            day = 0
            next_idx = 0
            daily_sum = 0

            while next_idx < len(weights):

                if daily_sum + weights[next_idx] <= capacity:
                    daily_sum += weights[next_idx]
                    next_idx += 1
                elif weights[next_idx] > capacity:
                    return False
                else:
                    day += 1
                    daily_sum = 0

            return day <= days


        max_capacity = sum(weights)
        min_capacity = 0


        while min_capacity < max_capacity:
            mid_capacity = (max_capacity + min_capacity) // 2

            if can_ship(mid_capacity):
                print(f"Can can_ship in {mid_capacity}")
                max_capacity = mid_capacity
            else:
                min_capacity = mid_capacity + 1

        return min_capacity

