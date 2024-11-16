print("This program displays a menu with options to choose A - E")

# This function calculates speed
def a():
    distance = float(input("Enter the distance (in meters):"))
    time = float(input("Enter the time (in seconds):"))
    if time != 0:
        speed = distance / time
        print(f"speed is {speed} m/s")
    else:
        print("Time cannot be zero.")

# This function calculate force
def b():
    mass = float(input("Enter the mass (in kg):"))
    acceleration = float(input("Enter the acceleration (in m/s):"))
    force = mass * acceleration
    print(f"Force is {force} Newtons ")

# This function calculate work
def c():
    force = float(input("Enter the force (in newtons):"))
    distance = float(input("Enter the distance (in meters):"))
    work = force * distance
    print(f"work is {work} joules")

# This function calculates power
def d():
    work_done = float(float("Enter the work done (in joules):"))
    time = float(input("Enter the time (in seconds):"))
    if time != 0:
        power = work_done / time
        print(f"power is {power}watts")
    else:
        print("time cannot be zero.")

# This function calculate gravitational force
def e():
    mass = float(input("Enter the mass (in kg)"))
    gravity = 9.8
    height = float(input("Enter the height (in meters):"))
    potential_energy = mass * gravity * height
    print(f"gravitational potential energy is {potential_energy}joules")


# The main function prompt the user
def main():
    print("choose a function to perform physics operation")
    user_choice = input("Enter your choice (a,b,c,d,e) :").lower()

    if user_choice == "a":
        a()
    elif user_choice == "b":
        b()
    elif user_choice == "c":
        c()
    elif user_choice == "d":
        d()
    elif user_choice == "e":
        e()
    else:
        print("invalid choice")

if __name__ == '__main__':
    main()
