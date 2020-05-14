#Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you can sell it.

#For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.

def max_profit(stock_price):
	price_diff=[]
	for index,price1 in enumerate(stock_price):
		for price2 in stock_price[index+1:]:
			diff=price2-price1
			#print(diff)
			price_diff.append(diff)
	
	print(price_diff)		
	return max(price_diff)
	
stock_price=[9, 11, 8, 5, 7, 10]
print(max_profit(stock_price))
