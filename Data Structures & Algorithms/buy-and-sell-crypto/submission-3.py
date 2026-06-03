class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #left_ptr as buy
        #right_ptr as sell

        # if len(prices) <= 1:
        #     return 0
        # elif len(prices) == 2:

        #     buy_ptr = 0
        #     sell_ptr = 1

        #     if prices[buy_ptr] >= prices[sell_ptr]:
        #         return 0
        #     else:
        #         return prices[sell_ptr] - prices[buy_ptr] 
        # else:
        profit = 0
        buy_ptr = 0
        sell_ptr = 1
        
        while sell_ptr < len(prices):
            if prices[sell_ptr] < prices[buy_ptr]:
                buy_ptr += 1 
            else: 
                profit = max(profit, prices[sell_ptr] - prices[buy_ptr])
                sell_ptr += 1 
                
        return profit 

                
            



        