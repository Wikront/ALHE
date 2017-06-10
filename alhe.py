import random
from datetime import time

FILE = open('data.txt', 'w')

class car():
    def __init__(self, hour, minute, second, direction):
        self.time=time(hour, minute, second);
        self.direction = direction
    def to_string(self):
        return str(self.time.strftime("%H:%M:%S	")+ ' ' + str(self.direction))

def generate_one_car_data():
    direction = random.randrange(0, 11, 1)
    hour = random.randrange(0, 24, 1)
    minute = random.randrange(0, 60, 1)
    second = random.randrange(0, 60, 1)
    return car(hour, minute, second, direction)

def main():
    for i in range(300):
        FILE.write(generate_one_car_data().to_string() + '\n')
	
main()

