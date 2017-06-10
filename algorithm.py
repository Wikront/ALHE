
from datetime import datetime, time
config_file = 'data.txt'
cars=[]
class car():
    def __init__(self, time, direction_from, direction_to, lane):
        self.time = time
        self.direction_from = direction_from
        self.direction_to = direction_to
        self.lane = lane
    def to_string(self):
        return str(self.time.strftime("%H:%M:%S") + ' ' + 
                   str(self.direction_from) + ' ' + str(self.direction_to) + ' ' + str(self.lane))

	
def readData():
#	with open('data.txt', 'r') as f:
 #   	content = f.readlines()
#	for line in content
#		print(line)
	file=open('data.txt', 'r')
	data=file.readlines()
	#print(readData())
	for line in data:
		args=line.strip().split(" ")	
		time=datetime.strptime(args[0], '%H:%M:%S').time()
		direction_from=args[1]
		direction_to=args[2]
		lane=args[3]
		cars.append(car(time, direction_from, direction_to, lane))
	return cars
def main():
	readData()
	for car in cars:
		print(car.to_string())
	
main()










