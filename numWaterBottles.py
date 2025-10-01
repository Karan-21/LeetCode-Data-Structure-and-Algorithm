class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        epsilon = 1e-8
        return int((numBottles * numExchange - epsilon) // (numExchange - 1))
