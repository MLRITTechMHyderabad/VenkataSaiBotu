import numpy as np
stock_prices = np.random.randint(100,501,(30,5))
average_stock_prices = np.mean(stock_prices, axis=0)
print("Average stock prices: ",average_stock_prices)
max_price = np.max(stock_prices)
min_price = np.min(stock_prices)
max_price_loc = np.where(stock_prices == max_price)
print("Highest price recorded :",max_price,"at Day",max_price_loc[0][0]+1,",Company",max_price_loc[1][0]+1)
normalized_prices = (stock_prices - min_price) / (max_price - min_price)
print('Normalized prices :',normalized_prices)
risky = np.where(stock_prices < 200)
#print(risky[0],risky[1])

risky_inestment_days = {}
for i in range(len(risky[0])):
    if risky[0][i]+1 in risky_inestment_days :
        risky_inestment_days[risky[0][i]+1] = [risky_inestment_days[risky[0][i]+1],stock_prices[risky[0][i]][risky[1][i]]]
    else :
       risky_inestment_days[risky[0][i]+1] = stock_prices[risky[0][i]][risky[1][i]]

for day in risky_inestment_days :
    print("Day ",day," : ", risky_inestment_days[day])