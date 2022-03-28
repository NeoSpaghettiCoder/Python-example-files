countries_and_capitals = {
"Poland" : "Warsaw", 
"Czechia": "Prague", 
"Germany": "Berlin"
}

try:                                                        # You put your code here
    print(2/0)
    print(countries_and_capitals["USA"])
    print("Here")
except KeyError:                                            # Catch error if key in the dictionary doesn't exists
    print("Key is not in the dictionary!")
except ZeroDivisionError:                                   # Catch error if you'll try to divide any value by 0
    print("You can't divide value by zero!")
except:                                                     # Catch any other error
    print("The error occured in the program!")
finally:                                                    # It'll always realize code
    print("It'll always be realize!")

print("here")