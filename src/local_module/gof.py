# AbstractFactory
amount_dict: dict = {"high": 1.2, "normal": 1.0, "low": 0.8}


class PizzaFactory:
    pass


def make_pizza(PizzaFactory: PizzaFactory, amount_str):
    pizza = PizzaFactory()
    amount = amount_dict[amount_str]
    pizza.pizza_materials = []
    pizza.pizza_materials.append(pizza.add_dough(amount))
    pizza.pizza_materials.append(pizza.add_source(amount))
    pizza.pizza_materials.append(pizza.add_topping(amount))
    return pizza


class PizzaFactoryA(PizzaFactory):
    def __init__(self):
        pass

    def check_pizza(self):
        for pizza_material in self.pizza_materials:
            pizza_material.check()

    @classmethod
    def add_dough(Class, amount=1):
        return Class.WheatDough(amount)

    @classmethod
    def add_source(Class, amount=1):
        return Class.TomatoSource(amount)

    @classmethod
    def add_topping(Class, amount=1):
        return Class.CornTopping(amount)

    class WheatDough:
        def __init__(self, amount=1):
            self.amount = amount

        def check(self):
            print(f"Wheat(amount: {self.amount})")

    class TomatoSource:
        def __init__(self, amount=1):
            self.amount = amount

        def check(self):
            print(f"Tomato(amount: {self.amount})")

    class CornTopping:
        def __init__(self, amount=1):
            self.amount = amount

        def check(self):
            print(f"Corn(amount: {self.amount})")


class PizzaFactoryB(PizzaFactory):
    def __init__(self):
        pass

    def check_pizza(self):
        for pizza_material in self.pizza_materials:
            pizza_material.check()

    @classmethod
    def add_dough(Class, amount=1):
        return Class.RiceFlourDough(amount)

    @classmethod
    def add_source(Class, amount=1):
        return Class.BasilSource(amount)

    @classmethod
    def add_topping(Class, amount=1):
        return Class.CheeseTopping(amount)

    class RiceFlourDough:
        def __init__(self, amount=1):
            self.amount = amount

        def check(self):
            print(f"FlourDough(amount: {self.amount})")

    class BasilSource:
        def __init__(self, amount=1):
            self.amount = amount

        def check(self):
            print(f"Tomato(amount: {self.amount})")

    class CheeseTopping:
        def __init__(self, amount=1):
            self.amount = amount

        def check(self):
            print(f"Cheese(amount: {self.amount})")
