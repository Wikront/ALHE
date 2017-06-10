'''
0 - gora 
1 - prawo (centrum)
2 - dol
3 - lewo (od centrum)

pasy:
0 - lewo
1 - srodek
2 - prawo prosto
'''
import random
from datetime import time

FILE = open('data.txt', 'w')
HOURS = [7, 8, 8, 9, 15, 16, 16, 17, 18]
DIRECTIONS_MORNING = [1, 1]
DIRECTIONS_AFTERNOON = [3, 3]

class car():
    def __init__(self, hour, minute, second, direction_from, direction_to, lane):
        self.time = time(hour, minute, second)
        self.direction_from = direction_from
        self.direction_to = direction_to
        self.lane = lane
    def to_string(self):
        return str(self.time.strftime("%H:%M:%S ") + str(self.direction_from) + ' ' + str(self.direction_to) + ' ' + str(self.lane))

def generate_one_car_data():
    hour = random.randrange(0, 24, 1)
    direction_from = random.randrange(0, 4, 1)
    direction_to = random.randrange(0, 4, 1)
    lane = random.randrange(0, 3, 1)
    minute = random.randrange(0, 60, 1)
    second = random.randrange(0, 60, 1)
    return car(hour, minute, second, direction_from, direction_to, lane)

class random_hour_generator():
    def __init__(self, list):
        self.hours = [i for i in range(24)] + list
    def get_random_hour(self):
        random.choice(self.hours)
    def print_hours(self):
        print(self.hours)

class random_direction_generator():
    def __init__(self, list):
        self.directions = [0, 1, 2, 3] + list
    def get_random_hour(self):
        random.choice(self.directions)

def main():
    for i in range(300):
        FILE.write(generate_one_car_data().to_string() + '\n')
    random_hour_generator([2,3,4,5]).print_hours()
	
main()

