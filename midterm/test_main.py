from unittest import TestCase
from main import Pizza


class TestPizza(TestCase):
    def test_add_topping(self):
        pizza = Pizza("Medium", toppings=[], base_cost=8.0, cost_per_topping=1.5, number_of_toppings_included=2)
        pizza.add_topping("pepperoni")
        pizza.add_topping("mushrooms")
        self.assertEqual(pizza.get_total_cost(), 8.0)

    def test_with_less_than_included_toppings(self):
        pizza = Pizza("Small", toppings=[] ,base_cost=8.0, cost_per_topping=1.5, number_of_toppings_included=2)
        pizza.add_topping("onions")
        self.assertEqual(pizza.get_total_cost(), 8.0)
