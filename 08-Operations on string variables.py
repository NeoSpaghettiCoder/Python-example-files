name = "eDeNn"
name2 = "     fsdsdfsdfsdfsd      "
print(len(name))                                            # Displays amounts of letters in variable
print(name.capitalize())                                    # Changes first letter to capital letter
print(name.upper())                                         # Changes all letters to capital letters
print(name.lower())                                         # Changes all letters to lower letters
print(name[0])                                              # Displays letter from first index
print(name[0:2])                                            # Displays first and second letter
print(name[1:3])                                            # Displays second and third letter from index
print(name[-1])                                             # Displays letters from the end
print(name[-3:])                                            # Displays from the end to third letter (reverse)

channel = "How to make cookies"
print(channel.split(" "))                                   # Displays split words

join_string = " . "
print(join_string.join(['How', 'To', 'Make', 'Cookies']))   # Connects words

print(name.startswith('e'))                                 # Returns true because first letter is 'e'
print(name.startswith('E'))                                 # Returns false because first letter is not 'E'

print(name.endswith('n'))                                   # Returns true because last letter is 'n'
print(name.endswith('N'))                                   # Returns false because last letter is not 'N'

print(name.rstrip("n"))                                     # Removes first letter 'e'
print(name.lstrip("e"))                                     # Removes last letter 'n'

print(name2.strip())                                        # Deletes tab and space 

first_name = "asds"
last_name = "das"

join_string = " "
print(first_name+last_name)                                 # Connects two strings
print(join_string.join([first_name,last_name]))             # Same as before but with function

james_bond = 7
print(str(james_bond).zfill(3))                             # Adds zeros at the beginning of string
