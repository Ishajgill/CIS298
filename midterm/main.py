#write a function sum_of_values_in_white_squares_minus_values_in_black_squares( some_2d_list )
# that returns the sum of all values in white square positions minus the sum of all values in black square positions

# s_list = [
# [ 1, 2, 3, 4 ], # 1 and 3 are on white squares
# [ 5, 6, 7, 8 ], # 6 and 8 are on white squares
# [ 2, 5, 7, 9 ] ] # 2 and 7 are on white squares
#
# #would add 1, 3, 6, 8, 2, 7 and subtract 2, 4, 5, 7, 5, 9
#
# def sum_of_values_in_white_squares_minus_values_in_black_squares(some_2d_list):
#     white_squares = [s_list[0][0], s_list[0][2], s_list[1][1], s_list[1][3], s_list[2][0], s_list[2][2]]
#     black_squares = [s_list[0][1], s_list[0][3], s_list[1][0], s_list[1][2], s_list[2][1], s_list[2][3]]
#
#     sum_white_squares = sum(white_squares)
#     sum_black_squares = sum(black_squares)
#     result = sum_white_squares - sum_black_squares
#     return result
# answer = sum_of_values_in_white_squares_minus_values_in_black_squares(s_list)
# print(f"The answer is {answer}")





# class Pizza:
#     def __init__(self,size:str,toppings:[str],base_cost:float,number_of_toppings_included:int,cost_per_topping:float):
#         self.size = size
#         self.toppings = toppings
#         self.base_cost = base_cost
#         self.number_of_toppings_included = number_of_toppings_included
#         self.cost_per_topping = cost_per_topping
#     def add_topping( self,topping : str ) :
#         self.toppings.append(topping)
#
#     def get_total_cost(self) -> float:
#         extra_toppings = len(self.toppings) - self.number_of_toppings_included
#         if extra_toppings < 0:
#             extra_toppings = 0
#         extra_cost = extra_toppings * self.cost_per_topping
#         total = self.base_cost + extra_cost
#         return total
# pizza = Pizza(
#     size="Large",
#     toppings=[],
#     base_cost=10.00,
#     number_of_toppings_included=2,
#     cost_per_topping=1.50
# )
#
# for topping in ["pepperoni", "mushrooms", "olives", "jalapenos"]:
#     pizza.add_topping(topping)
#
# total_price = pizza.get_total_cost()
# print(f"Total cost: ${total_price:.2f}")
#
import pandas as pd
import matplotlib.pyplot as plt
csv_file = "yearly_balances.csv"
data = pd.read_csv(csv_file)
# Used AI to look up how to plot data using MatPlotLib
plt.figure(figsize=(10, 6))
plt.plot(data["Year"], data["Cash"], label="Cash")
plt.plot(data["Year"], data["Stocks"], label="Stocks")
plt.plot(data["Year"], data["Bonds"], label="Bonds")
plt.plot(data["Year"], data["Savings"], label="Savings")
plt.xlabel("Year")
plt.ylabel("Amount")
plt.title("Retirement savings ")
plt.xticks(data["Year"])
plt.legend()
plt.show()
