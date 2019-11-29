# Davis Arthur
# 11-28-2019
# A Prize No One Can Win

# read in the number of items, and the value for the deal
numitems, deal = str(input()).split()
deal = int(deal)

# read in the prices of each item and sort them from lowest to highest
prices = input().split()
numprices = []
for price in prices:
    numprices.append(int(price))
numprices.sort()
prices = numprices

# if there is only one item or no possible combination...
if len(prices) < 2 or prices[0] + prices[1] > deal:
    print(1)
else:
    max = True
    i = 1
    while i < len(prices):
        value = prices[i] + prices[i - 1]
        if value > deal:
            print(i)
            max = False
            break
        i = i + 1
    if max:
        print(len(prices))
