# Press the green button in the gutter to run the script.
from Car import Car
from Ford import Ford
from Sedan import Sedan

if __name__ == '__main__':
    sedan = Sedan(240, 2000, "Black", 3)

    ford1 = Ford(320, 3000, "Blue", 2000, 300)
    ford2 = Ford(310, 2800, "White", 2005, 250)

    car = Car(200, 1200, "Grey")

    print("Sedan price : " + str(sedan.get_sales_price()))
    print("Ford 1 price : " + str(ford1.get_sales_price()))
    print("Ford 2 price : " + str(ford2.get_sales_price()))
    print("Car price : " + str(car.get_sales_price()))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
