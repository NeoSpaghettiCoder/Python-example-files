# number = 1

# while number < 6:                     # Repeats until number will be greater than 6
#     print(number)
#     number += 1

# for number in range(0,19):            # Repeats until number will be 20
#     print(number)

# for number in range(0, 10, 2):        # Repeats until number will be 10 and jump every two numbers 
#     print(number)

# for number in range(0, 10):     
#     if number == 5:                   # Stops repeating tasks when number is 5
#         break
#     print(number)

for number in range(0, 10):         
    if(number == 5):                    # Ignores print when number is 5
        continue                   
    print(number)