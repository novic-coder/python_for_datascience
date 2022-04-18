# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
print(areas[1])

# Print out last element from areas
print(areas[-1])

# Print out the area of the living room
print(areas[5])



# Performing Additional operations using the items from list

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Sum of kitchen and bedroom area: eat_sleep_area
eat_sleep_area = areas[3]+areas[-3]
# Print the variable eat_sleep_area
print(eat_sleep_area)

# Slicing and Dicing

# My_list[start:end]


"""Use slicing to create a list, downstairs, that contains the first 6 elements of areas.
Do a similar thing to create a new variable, upstairs, that contains the last 4 elements of areas.
Print both downstairs and upstairs using print()"""



# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs

downstairs = areas[0:6]
# Use slicing to create upstairs

upstairs =areas[6:10]
# Print out downstairs and upstairs
print(downstairs)
print(upstairs)


"""Create downstairs again, as the first 6 elements of areas. This time, simplify the slicing by omitting the begin index.
Create upstairs again, as the last 4 elements of areas. This time, simplify the slicing by omitting the end index."""

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Alternative slicing to create downstairs
downstairs = areas[:6]

# Alternative slicing to create upstairs
upstairs = areas[6:]