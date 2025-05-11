from time import sleep

#Greet user and initiate calculation
def game_start():
    print("Hello! I am Emi, an Emission Savings Calculation Bot! Let us calculate your emission savings for today!")
    sleep(2)
    print("I will guide you through the calculation process. You just need to answer a few questions.")
    sleep(2)
    game_start_command = input("Press 'START' to start the calculation. Press 'EXIT' to end this program. ")
    return game_start_command

#Calculate emissions related to transportation
def transportation_calculation():
    emissions_data = {"car": 171, "train": 35, "bike": 0, "walk": 0}
    print("Let's calculate your transportation related emissions for today!")
    trans_mode = input("Enter your mode of transportation ('car', 'train', 'bike'): ")
    trans_distance = int(input("Enter the approximate distance you traveled today in kilometers: "))
    trans_emissions = emissions_data[trans_mode] * trans_distance
    trans_check_value = emissions_data["car"] * trans_distance
    trans_savings = trans_check_value - trans_emissions
    return trans_savings

#Calculate emissions related to coffee consumption
def coffee_calculation():
    emissions_data = {"single-use": 0.029, "reusable": 0.0084}
    print("Let's calculate your coffee related emissions for today!")
    coffee_cup = input("Enter what coffee cup you used ('single-use', 'reusable'): ")
    coffee_amount = int(input("Enter how many cups of coffee you had today: "))
    coffee_emissions = emissions_data[coffee_cup] * coffee_amount
    coffee_check_value = emissions_data["single-use"] * coffee_amount
    coffee_savings = coffee_check_value - coffee_emissions
    return coffee_savings

#Main calculation of total emission savings
def calculation():
    if game_start() == "EXIT":
        print("Exiting Program.")
    else:
        total_savings = transportation_calculation() + coffee_calculation()
        print("Your total emissions savings for today are {savings} kg CO2.".format(savings=str(total_savings)))
        sleep(2)
        print("Thank you! Visit again tomorrow to calculate your emission savings!")


calculation()
