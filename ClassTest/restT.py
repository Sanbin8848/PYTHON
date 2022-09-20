class Restaurant():
    '''定义一个restaurant类'''

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type

    def describe_restaurant(self):
        print("The restaurant name is: "+self.restaurant_name)
        print("The restaurant cuisine_type is:"+self.cuisine_type)

    def open_restaurant(self):
        print("The restaurant is on the service.")

my1_Restaurant=Restaurant('Siji','bookstore')
my1_Restaurant.describe_restaurant()
my1_Restaurant.open_restaurant()
print("____________________________________")
my2_Restaurant=Restaurant('yaduo','qucikin')
my2_Restaurant.describe_restaurant()
my2_Restaurant.open_restaurant()