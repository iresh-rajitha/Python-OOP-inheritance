from Car import Car


class Ford(Car):
    
    def __init__(self, speed, regular_price, color, year , manufacture_discount):
        super(Ford, self).__init__(speed, regular_price , color)
        self.__manufacture_discount = manufacture_discount
        self.__year = year

    def get_sales_price(self):
        return super(Ford, self).get_sales_price() - self.__manufacture_discount
