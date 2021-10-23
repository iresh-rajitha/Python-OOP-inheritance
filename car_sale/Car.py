class Car:

    def __init__(self, speed, regular_price, color):
        self.__speed = speed
        self.__regular_price = regular_price
        self.__color = color

    def get_sales_price(self):
        return self.__regular_price
