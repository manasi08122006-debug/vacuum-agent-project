initial_environment = ['clean', 'dirty', 'clean', 'dirty', 'dirty']
initial_location = 0

def sense():
    return environment[location]

def clean():
    global environment
    print(f"Cell {location} is dirty. Cleaning it.")
    environment[location] = 'clean'

def move():
    global location
    print(f"Cell {location} is clean. Moving to the next cell.")
    location = (location + 1) % len(environment)

def is_goal_achieved():
    return environment == goal

def act():
    if is_goal_achieved():
        print("Goal achieved! All cells are clean.")
        return False

    if sense() == 'dirty':
        clean()
    else:
        move()

    return True

environment = list(initial_environment)
location = initial_location
goal = ['clean'] * len(environment)

print("Initial environment:", environment)
for _ in range(10):
    if not act():
        break

print("Final environment:", environment)
