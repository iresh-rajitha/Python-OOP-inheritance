from Car import Car


class Sedan(Car):
    def __init__(self, speed, regular_price, color, length):
        super(Sedan, self).__init__(speed, regular_price, color)
        self.__length = length

    def get_sales_price(self):
        if self.__length > 20:
            return super(Sedan, self).get_sales_price() - super(Sedan, self).get_sales_price() * 0.05
        else:
            return super(Sedan, self).get_sales_price() - super(Sedan, self).get_sales_price() * 0.1
