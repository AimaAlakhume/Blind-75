def maxProfit(prices):

	if len(prices) == 1: #edge case
		return 0
	
	buyDay, sellDay = 0, 1 #left, right pointers
	maxProfit = 0

	while sellDay < len(prices):
		if prices[buyDay] < prices[sellDay]:
			newProfit = sellDay - buyDay
			maxProfit = max(maxProfit, newProfit)
		else:
			sellDay = buyDay
		sellDay += 1

	return maxProfit
