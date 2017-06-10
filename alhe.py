'''
0 - dol
1 - prawo (centrum)
2 - gora
3 - lewo (od centrum)

pasy:
0 - lewo
1 - srodek
2 - prawo
'''
import random
from datetime import time
import math

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
    hour = random_hour_generator(HOURS).get_random_hour()
    direction_from = random.randrange(0, 4, 1)
    if(hour > 7 and hour < 10):
        direction_to = random_direction_generator(DIRECTIONS_MORNING, direction_from).get_random_direction()
    elif(hour > 14 and hour < 19):
        direction_to = random_direction_generator(DIRECTIONS_AFTERNOON, direction_from).get_random_direction()
    else:
        direction_to = random_direction_generator([], direction_from).get_random_direction()
    lane = 2
    if ((direction_to-direction_from)%4) == 1:
        lane = 0
    elif ((direction_to-direction_from)%4) == 2:
        lane = random.randrange(1, 3, 1)
    elif ((direction_to-direction_from)%4) == 3:
        lane = 2
    minute = random.randrange(0, 60, 1)
    second = random.randrange(0, 60, 1)
    return car(hour, minute, second, direction_from, direction_to, lane)

class random_hour_generator():
    def __init__(self, list):
        self.hours = [i for i in range(24)] + list
    def get_random_hour(self):
        return random.choice(self.hours)
    def print_hours(self):
        print(self.hours)

class random_direction_generator():
    def __init__(self, list, from_direction):
        self.directions = [0, 1, 2, 3] + list
        self.directions.remove(from_direction)
    def get_random_direction(self):
        return random.choice(self.directions)

class cars_set():
    def __init__(self):
        self.list = []
    def generate_data(self, count):
        for i in range(count):
            self.list.append(generate_one_car_data())
        self.list.sort(key = lambda x: x.time)
        return self.list

def main():
    cars = cars_set().generate_data(300)
    for i in range(300):
        FILE.write(cars[i].to_string() + '\n')
	
main()

