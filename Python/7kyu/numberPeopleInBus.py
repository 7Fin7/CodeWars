
def number(bus_stops):
    
    # Initialise amount of people on bus
    bus_count = 0
    
    # Loop through each bus stop (pair of numbers)
    for bus_stop in bus_stops:
        on_bus = bus_stop[0]    # Amount of people getting on bus
        off_bus = bus_stop[1]   # # Amount of people getting off bus
        
        # Add people getting on at current bus stop and subtract people getting off
        bus_count += on_bus - off_bus
        
    return bus_count

print(number([[10,0],[3,5],[5,8]]))
print(number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]))
print(number([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]]))

# There is a bus moving in the city which takes and drops some people at each bus stop.

# You are provided with a list (or array) of integer pairs. Elements of each pair represent the number of people that get on the bus (the first item) and the 
# number of people that get off the bus (the second item) at a bus stop.

# Your task is to return the number of people who are still on the bus after the last bus stop (after the last array). Even though it is the last bus stop, 
# the bus might not be empty and some people might still be inside the bus, they are probably sleeping there :D

# Take a look on the test cases.

# Please keep in mind that the test cases ensure that the number of people in the bus is always >= 0. So the returned integer can't be negative.

# The second value in the first pair in the array is 0, since the bus is empty in the first bus stop.