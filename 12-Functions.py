##############################################################################
# Types of functions #

# def sum(a, b):                                                                # Function that returns sum of two numbers
#     return a + b

# def say_sum():                                                                # Function that prints something
#     print("Sum: ")

# say_sum()                                                                     # Declaring functions
# print(sum(5,3))

##############################################################################
# Country Info #

countries_information = {}                                                      # Declaring dictionary
countries_information["Poland"] = ("Warsaw",37.97)                              # Adding values to the dictionary
countries_information["Germany"] = ("Berlin", 83.02)
countries_information["Slovakia"] = ("Bratislava", 5.45)

def invalid_country(country):                                                   # Function that returns true if the country is not in the dictionary
    for country_name in countries_information.keys():
        if(country==country_name): return False
    return True

def show_country_info(country):                                                 # Function that displays country info from the dictionary
    country_information = countries_information.get(country)

    print()
    print(country)
    print("--------")
    print("Capital: " + country_information[0])
    print("Number of the citizens: " + str(country_information[1]))

for country in countries_information.keys():
    print(country)

country = input("What country do you want to display?")

if(invalid_country(country)):                                                   # Checking if the country value is correct
    print("You type invalid value of the country!")
else: 
    show_country_info(country)