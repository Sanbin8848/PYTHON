from car import Car


# class Battery():
#      """一次模拟电动汽车电瓶的简单尝试"""
#      def __init__(self, battery_size=70):
#           """初始化电瓶的属性"""
#           self.battery_size = battery_size
#      def describe_battery(self):
#           """打印一条描述电瓶容量的消息"""
#           print("This car has a " + str(self.battery_size) + "-kWh battery.")


# battery1=Battery()
# battery1.describe_battery()

class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    # def __int__(self, battery_size=70):
    #     self.battery_size = battery_size

    def describe_battery(self):
        print(str(self.battery_size))


#
#
# #        print('This car has a ' + str(self.battery_size) + '-kwh battery.')


# battery1 = Battery()
# battery1.describe_battery()


class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
# my_tesla.battery.describe_battery()
