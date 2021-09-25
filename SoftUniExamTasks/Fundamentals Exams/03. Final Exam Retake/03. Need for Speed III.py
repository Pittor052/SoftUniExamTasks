num_cars = int(input())
garage = {}
output = []

while num_cars > 0:

    # {car}|{mileage}|{fuel}
    car, mileage, fuel = input().split('|')
    garage[car] = {"mileage": int(mileage), "fuel": int(fuel)}
    num_cars -= 1

command = input()

while 'Stop' not in command:

    command = command.split(' :')
    action = command[0]
    car = command[1].lstrip()

    if 'Drive' in action:
        # Drive : {car} : {distance} : {fuel}
        # oYou need to drive the given distance and you will need the given fuel to do that.
        # If the car doesn`t have enough fuel print:
        # "Not enough fuel to make that ride"
        # oIf the car has the required fuel available in the tank, increase its mileage with the given distance,
        # decrease its fuel with the given fuel and print:
        # "{car} driven for {distance} kilometers. {fuel} liters of fuel consumed."
        # oYou like driving new cars only, so if the mileage of a car reaches 100 000 km,
        # remove it from the collection(s). Print:
        # "Time to sell the {car}!"
        distance = int(command[2].lstrip())
        fuel_consumption = int(command[3].lstrip())

        if garage[car]['fuel'] >= fuel_consumption:

            garage[car]['fuel'] -= fuel_consumption
            garage[car]['mileage'] += distance
            output.append(f"{car} driven for {distance} kilometers. {fuel_consumption} liters of fuel consumed.")

            if garage[car]['mileage'] >= 100000:

                output.append(f"Time to sell the {car}!")
                garage.pop(car)

        else:
            output.append("Not enough fuel to make that ride")

    elif 'Refuel' in action:
        # Refuel : {car} : {fuel}
        # oRefill the tank of your car.
        # oEach tank can hold a maximum of 75 liters of fuel,
        # so if the given amount of fuel is more than you can fit in the tank, take only what is required to fill it up.
        # oPrint a message in the following format:
        # "{car} refueled with {fuel} liters"
        refill = int(command[2].lstrip())

        if garage[car]['fuel'] + refill > 75:
            refill = 75 - garage[car]['fuel']

        garage[car]['fuel'] += refill
        output.append(f"{car} refueled with {refill} liters")

    elif 'Revert' in action:
        # Revert : {car} : {kilometers}
        # oDecrease the mileage of the given car with the given kilometers and print the kilometers you have decreased
        # it with in the following format:
        # "{car} mileage decreased by {amount reverted} kilometers"
        # oIf the mileage becomes less than 10 000km after it is decreased, just set it to 10 000km and
        # DO NOT print anything.
        revert = int(command[2].lstrip())

        if garage[car]['mileage'] - revert < 10000:
            garage[car]['mileage'] = 10000

        else:
            garage[car]['mileage'] -= revert
            output.append(f"{car} mileage decreased by {revert} kilometers")

    command = input()

print(*output, sep='\n')

for car, stats in sorted(garage.items(), key=lambda x: (-x[1]['mileage'], x[0])):

    print(f"{car} -> Mileage: {stats['mileage']} kms, Fuel in the tank: {stats['fuel']} lt.")

# # INPUT 0
# 3
# Audi A6|38000|62
# Mercedes CLS|11000|35
# Volkswagen Passat CC|45678|5
# Drive : Audi A6 : 543 : 47
# Drive : Mercedes CLS : 94 : 11
# Drive : Volkswagen Passat CC : 69 : 8
# Refuel : Audi A6 : 50
# Revert : Mercedes CLS : 500
# Revert : Audi A6 : 30000
# Stop
# # OUTPUT 0
# Audi A6 driven for 543 kilometers. 47 liters of fuel consumed.
# Mercedes CLS driven for 94 kilometers. 11 liters of fuel consumed.
# Not enough fuel to make that ride
# Audi A6 refueled with 50 liters
# Mercedes CLS mileage decreased by 500 kilometers
# Volkswagen Passat CC -> Mileage: 45678 kms, Fuel in the tank: 5 lt.
# Mercedes CLS -> Mileage: 10594 kms, Fuel in the tank: 24 lt.
# Audi A6 -> Mileage: 10000 kms, Fuel in the tank: 65 lt.
# # INPUT 1
# 4
# Lamborghini Veneno|11111|74
# Bugatti Veyron|12345|67
# Koenigsegg CCXR|67890|12
# Aston Martin Valkryie|99900|50
# Drive : Koenigsegg CCXR : 382 : 82
# Drive : Aston Martin Valkryie : 99 : 23
# Drive : Aston Martin Valkryie : 2 : 1
# Refuel : Lamborghini Veneno : 40
# Revert : Bugatti Veyron : 2000
# Stop
