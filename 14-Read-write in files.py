# file = open("countries_and_capitals.txt", "w+")                                                   # Opens file with read and write mode

file = open("countries_and_capitals.txt", "w")                                                      # Opens file with write mode

countries_and_capitals = {"Poland": "Warsaw", "Czechia": "Prague", "Germany": "Berlin"}            

for country, capital in countries_and_capitals.items():                                             # Loop that will write country-capital to the file
    file.write(country + "-" + capital + '\n')

file.close()                                                                                        # Closes file

###

# file = open("countries_and_capitals.txt", "r")                                                    # Opens file with read mode
file = open("countries_and_capitals.txt")                                                           # The default mode is read in open function

for line in file.readlines():                                                                       # Loop that will read lines from the file
    # print(line)                                                                                   # Print with new lines
    print(line.strip())                                                                             # Deletes space between lines

file.close()