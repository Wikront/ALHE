import random
from datetime import time

FILE = open('data.txt', 'w')

class car():
    def __init__(self, hour, minute, second, direction_from, direction_to, lane):
        self.time = time(hour, minute, second)
        self.direction_from = direction_from
        self.direction_to = direction_to
        self.lane = lane
    def to_string(self):
        return str(self.time.strftime("%H:%M:%S	") + ' ' + 
                   str(self.direction_from) + ' ' + str(self.direction_to) + ' ' + str(self.lane))

def generate_one_car_data():
    direction_from = random.randrange(0, 4, 1)
    direction_to = random.randrange(0, 4, 1)
    lane = random.randrange(0, 3, 1)
    hour = random.randrange(0, 24, 1)
    minute = random.randrange(0, 60, 1)
    second = random.randrange(0, 60, 1)
    return car(hour, minute, second, direction_from, direction_to, lane)

def main():
    for i in range(300):
        FILE.write(generate_one_car_data().to_string() + '\n')
	
main()

