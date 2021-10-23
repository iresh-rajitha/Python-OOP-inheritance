from Car import Car


class Truck(Car):

    def __init__(self, speed, regular_price, color, weight):
        super(Truck, self).__init__(speed, regular_price, color)
        self.__weight = weight

    def get_sales_price(self):
        if self.__weight > 2000:
            return super(Truck, self).get_sales_price() - super(Truck, self).get_sales_price() * 0.1
        else:
            return super(Truck, self).get_sales_price() - super(Truck, self).get_sales_price() * 0.2
