light = input("What is the light (red or green): ")

# if light=="red":                                        # If light is red, print "Wait!""
#     print("Wait!")
# elif light=="green":                                    # If light is green, print "Go!"
#     print("Go!")
# else:                                                   # If you type anything else you get the message below
#     print("I don't know what color is it!")

print("Go!") if light == "green" else print("Wait!")      # Simple way for two conditions