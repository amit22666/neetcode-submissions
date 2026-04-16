class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Step 1: Define a function that takes prices (list of integers) as input

        # Step 2: Initialize a variable min_price with a very large value 
        # (this will track the lowest price seen so far)
        min_price = prices[0]


        # Step 3: Initialize a variable max_profit with 0 
        # (because if no transaction is possible, profit should be 0)
        max_profit = 0

        # Step 4: Loop through each price in prices
        for cur_price in prices:

            # Step 4.1: If the current price is less than min_price, update min_price 
            # (because this could be a better buying day)
            if cur_price < min_price:
                min_price = cur_price
            # Step 4.2: Otherwise, calculate profit = current price - min_price 
            # (this is the profit if we bought at min_price and sold today)
            profit = cur_price - min_price
            # Step 4.3: If profit is greater than max_profit, update max_profit
            if profit > max_profit:
                max_profit = profit
        # Step 5: After the loop ends, return max_profit
        return max_profit

        