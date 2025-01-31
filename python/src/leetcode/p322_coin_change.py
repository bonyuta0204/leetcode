class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        if amount == 0:
            return 0
        min_coins = [-1 for _ in range(amount + 1)]

        for i in coins:
            if i < len(min_coins):
                min_coins[i] = 1

        for i in range(amount + 1):
            if min_coins[i] > 0:
                continue

            valids = []
            for c in coins:
                if i - c > 0 and min_coins[i - c] > 0:
                    valids.append(min_coins[i - c])
            if valids:
                min_coins[i] = min(valids) + 1
        return min_coins[-1]

