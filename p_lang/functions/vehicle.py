def car(**cars):
    """Different car brands popular with users."""
    
    active = True
    while active:
        for car, desc in cars.items():
            if car == 'engine':
                print(f"{car.upper()}: {desc.upper()}")
            
            else:
                print(f"{car.upper()}: {desc.title()}")

        ans = input("You can enter 'x' to exit.")
        
        if ans == 'x':
            active = False
            
            return cars


car_company = input("Enter your favorite car company\n")

car_type = input("Enter the car model\n")

car_engine = input("ICE OR EV\n")

cars = car(manufacturer = car_company, model = car_type, engine = car_engine)
