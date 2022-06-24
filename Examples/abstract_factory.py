from common import add_source
add_source()

from src.local_module import gof  # nopep8


def main():
    pizza1 = gof.make_pizza(gof.PizzaFactoryA, "high")
    pizza1.check_pizza()

    print("-----")

    pizza2 = gof. make_pizza(gof.PizzaFactoryB, "normal")
    pizza2.check_pizza()


if __name__ == "__main__":
    main()
