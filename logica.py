# 10 km in 43 minutes and 30 seconds, what is the average time per mile
# in 1 mile is 1,64km 

# Inputs
distance_km = 10
total_time = 43.5
mile_in_km = 1.64

# Convert kilometers to miles
distance_miles = distance_km / mile_in_km

# Calculate average time per mile
average_pace_per_mile = total_time / distance_miles
print(f"Average mile: {distance_miles:.2f} miles")
print(f"Average time per ma ile: {average_pace_per_mile:.2f} minutes")
print(1, 0, 0)
print(type(average_pace_per_mile))
n = lambda a,b : a + b 
print(n(20,32))
pi = 3.14
r = 5
n = (4/3)*pi*r**3
print(f"é {n:.2f}")

def começar():
    parede = """
        +- - - -+ - - - -+ - - - -+
        /       /       /         /
        /       /       /         /
        /       /       /         /
        /       /       /         /
    """
    print(parede)
def final():
    perede = """
        + - - - -+ - - - -+ - - - -+    
        /        /        /        /
        /        /        /        /
        /        /        /        /
        /        /        /        /
        + - - - -+ - - - -+ - - - -+
    """
    print(perede)
def completar():
    começar();começar();final()
    
completar()
