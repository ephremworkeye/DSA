# input [20, 30, 10, 50, 25, 45] output = 40
# input [45, 10, 25, 30, 35, 43] output = 33

# brute force solution for this is 
# def stock_sales_once(A):
#     max_profit = 0
#     for i in range(len(A)):
#         for j in range(i+1, len(A)):
#             max_profit = max(max_profit, A[j]-A[i])
#     return max_profit

# print(stock_sales_once([20, 30, 10, 50, 25, 45]))
# print(stock_sales_once([45, 10, 25, 30, 35, 43]))

# optimal solution
def stock_sales_once(A):
    max_profit, min_price_so_far = 0, float('inf') # we can replace min_price_so_far = float('inf')
    for price in A:
        daily_profit = price - min_price_so_far
        max_profit = max(max_profit, daily_profit)
        min_price_so_far = min(min_price_so_far, price)
    return max_profit

print(stock_sales_once([20, 30, 10, 50, 25, 45]))
print(stock_sales_once([45, 10, 25, 30, 35, 43]))
print(stock_sales_once([45, 35, 25, 15, 10, 5]))

