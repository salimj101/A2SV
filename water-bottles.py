class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        numsum = numBottles
        
        while numBottles >= numExchange:
            newBottles = numBottles // numExchange
            remander = numBottles % numExchange  
            
            numsum += newBottles
            numBottles = newBottles + remander  
        
        return numsum