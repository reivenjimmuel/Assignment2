apple_cost = 20 #Price of an Apple
orange_cost = 25 #Price of an Orange
print('Enter the amount of apples that you want to buy: ')
apple = int(input())
print('Enter the amount of oranges that you want to buy: ')
orange = int(input())
total = (apple_cost*apple + orange_cost*orange)
print(f'The total amount is Php.{total}.')