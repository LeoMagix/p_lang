from car import Car
from electric_car import ElectricCar as EV 

my_car = Car('audi', 'a4', 2020)
my_car.read_odometer()

ev = EV('hyndai', 'ioniq', 2022)
ev.battery.describe_battery()
ev.gas_tank()
