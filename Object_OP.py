class Car():

    def __init__(self,car_name,car_model, car_colour):
        self.name=car_name
        self.model=car_model
        self.colour=car_colour
        print('car class in running')
    def get_my_car(self):
        print(f"My car name is {self.name} and the model is {self.model}")
    
    def get_my_car_colour(self):
        return self.colour

my_car= Car('ford','2000','yellow')
my_car.get_my_car()
print(my_car.get_my_car_colour())
del my_car.colour
# print(my_car.get_my_car_colour())
del my_car
# print(my_car)
