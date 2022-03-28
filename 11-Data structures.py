###############################################################################
# list #

# names_list = []                                           # Creates new list
# names_list.append("Kaminsky")                             # Adds first value to the list
# names_list.append("Marco")                                # Adds second value to the list

names_list = ["Kaminsky", "Marco", "Hektor", "Kaminsky"]    # Creates list and defining values for it

print(names_list)                                           # Prints all values in the list
print()

print(names_list[0])                                        # Prints first value in the list
print()

names_list.reverse()                                        # Reverses index in the list
print(names_list)
print()

names_list.sort()                                           # Sorts index alphabetically
print(names_list)
print()

names_list.sort(reverse=True)                               # Reverses alphabetical sort
print(names_list)
print()

print(names_list.count("Kaminsky"))                         # Prints how many "Ada" values are in the list 
print()

print(len(names_list[0]))                                   # Prints length of the string in the list
print()

print(len(names_list))                                      # Prints length of an index in the list
print()

names_list.pop(0)                                           # Deletes first index in the list
print(names_list)
print()

names_list2 = ["Prom"]
names_list3 = names_list + names_list2                      # Connects with first and second list
print(names_list3)
print()

names_list.remove("Kaminsky")                               # Deletes index with "Kaminsky" value
print(names_list)
print()

names_list.clear()
print(names_list)                                           # Deletes all values in the list
print()

names_list = ["Kaminsky", "Marco", "Hektor", "Kaminsky"]
for name in names_list:                                     # Prints all values from the list
    print(name)
print()

print("###############################################################################")
print()
###############################################################################
# tuple #

names_tuple = ("Kaminsky", "Marco", "Hektor", "Kaminsky")  # Can't delete or modify any of the value from it 
print(names_tuple)
print()

print("###############################################################################")
print()

###############################################################################
# set #

# names_set = set()                                         # Clears set
# names_set.add("Kaminsky")                                 # Adds first value
# names_set.add("Marco")                                    # Adds second value
# names_set.add(names_list)                                 # Can't do that
# names_set.add(names_touple)                               # Can do that

names_set = {"Kaminsky", "Marco", "Hektor", "Kaminsky"}     # Can't add any duplicated data into it
print(names_set)
print()

names_set.remove("Kaminsky")                                # Removes value from the set                 
print(names_set)
print()

names_set.discard("Kaminsky")                               # Can't show any error if value to remove doesn't exist

# print(names_set[0])                                       # You can't do that

for name in names_set:                                      # Prints all values from the set
    print(name)

names_set2 = {"fsdfdsdf", "Kaminsky"}                       
                     
names_set3 = names_set.union(names_set2)                    # Connects first set with the second
for name in names_set3:                                    
    print(names_set3)

print()

names_set3 = names_set.difference(names_set2)               # Return only values that are in the first set but not in the second
for name in names_set3:
    print(name)

print()

names_set3 = names_set.intersection(names_set2)             # Returns all elements that are in both sets
for name in names_set3:
    print(name)

print()

names_set3 = names_set.symmetric_difference(names_set2)     # Returns all elements that are exacly in one of the set
for name in names_set3:
    print(name)

print()

names_set.clear()                                           # Deletes all values in the set
for name in names_set:
    print(name)

print()

names_list.extend(names_set2)                               # Adds value from set to the list
print(names_list)                               
print()

print("###############################################################################")
print()

###############################################################################
# dictionary # 

countries_and_capitals = {"USA" : "Washington", "Persia": "Mesopotamia"}            # Declares dictionary with values
countries_and_capitals['Czechia'] = "Prague"

print(countries_and_capitals)                                                       # Prints all dictionary keys and values
print()

for country in countries_and_capitals.keys():                                       # Prints only keys ("USA") etc.
    print(country)
print()

for capital in countries_and_capitals.values():                                     # Prints only values of the keys ("Washington") etc.
    print(capital)
print()

for country, capital in countries_and_capitals.items():                             # Prints all values
    print(country + "-" + capital)
print()

print(countries_and_capitals["USA"])                                                # Displays error
print()

print(countries_and_capitals.get("USA"))                                            # Doesn't display any error
print()

print(countries_and_capitals.setdefault("Great Britain", "London"))                 # Inserts key with value
print(countries_and_capitals)
print()

countries_and_capitals["Poland"] = "Cracow"                                         # Adds new key with value
print(countries_and_capitals)
print()

print(countries_and_capitals.pop("Poland"))                                         # Removes key
print(countries_and_capitals)
print()

print(countries_and_capitals.popitem())                                             # Removes last added item
print(countries_and_capitals)
print()

if "Poland" in countries_and_capitals.keys():                                       # Checks value in the dictionary keys
    print("Founded!")
else:
    print("Did not find!")
print()

countries_and_capitals.clear()                                                      # Clears dictionary
print(countries_and_capitals)