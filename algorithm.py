
from datetime import datetime, time, timedelta
def calcFunc():
	return 1

class customTime():
	def __init__(self, time):
		self.time=time
	def intValue(self):
		return self.time.hour*60*60+self.time.minute*60+self.time.second
	def addSeconds(self,second):
		self.time+=timedelta(seconds=second)
	def setTimeFromInt(seconds):
		self.time=time(seconds/(60*60),(seconds%(60*60))/60,(seconds%60))
class light():
	def __init__(self, times):
		self.times = times
		self.queue=[[],[]]
	def addToLeft(car):
		self.queue[0].append(car)
	def addToStraigt(car):
		self.queue[0].append(car)
	def addToRight(car):
		self.queue[1].append(car)
	def runOneCycle(startTime):
		sum=runOneLane(startTime, 0)
		sum+=runOneLane(startTime, 1)
		return sum
	def runOneLane(self,startTime, lane):
		sum=0
		currentTime=startTime
		carsWaitingBefore=0
		for car in queue[lane]:
			while(currentTime.intValue()<startTime.intValue()+self.times[startTime.time.hour].intValue()):
				if(car.time.intValue()<startTime.intValue() and carsWaitingBefore*waitingTime.intValue()<self.time.intValue()):
					sum+=carsWaitingBefore*waitingTime.intValue()+accelerateTime.intValue()+startTime.intValue()-car.time.intValue()
					++carsWaitingBefore
					queue[lane].pop(0)
				elif (car.time.intValue()>startTime.intValue() and car.time.intValue()-startTime.intValue()+carsWaitingBefore*waitingTime.intValue()<self.time.intValue()):
					if(car.time.intValue()>startTime.intValue()+carsWaitingBefore*waitingTime.intValue()):
						sum+=0
						++carsWaitingBefore
					else:
						++carsWaitingBefore
						sum+=startTime.intValue()+carsWaitingBefore*waitingTime.intValue()+accelerateTime.intValue()-car.time.intValue()
					sum+=carsWaitingBefore*waitingTime.intValue()+accelerateTime.intValue()
					++carsWaitingBefore
					queue[lane].pop(0)
				else:
					return sum
				currentTime.setTimeFromInt(startTime+carsWaitingBefore*waitingTime.intValue())
		return sum
class car():
    def __init__(self, time, direction_from, direction_to, lane):
		self.time = time
		self.direction_from = direction_from
		self.direction_to = direction_to
		self.lane = lane
    def to_string(self):
        return str(self.time.time.strftime("%H:%M:%S") + ' ' + 
                   str(self.direction_from) + ' ' + str(self.direction_to) + ' ' + str(self.lane)+ ' '+str(self.time.time.hour)+ ' '+str(self.time.time.minute)+ ' '+str(self.time.time.second)+' ')

	
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
		time=customTime(datetime.strptime(args[0], '%H:%M:%S').time())
		direction_from=args[1]
		direction_to=args[2]
		lane=args[3]
		cars.append(car(time, direction_from, direction_to, lane))
	return cars
def main():
	readData()
	for car in cars:
		print(car.to_string()+str(car.time.intValue()))
	
config_file = 'data.txt'
cars=[]
lights=[time(0,0,20),time(0,0,20),time(0,0,20),time(0,0,20),time(0,0,20),time(0,0,20),time(0,0,20),time(0,0,20)]
accelerateTime=customTime(time(0,0,5))
waitingTime=customTime(time(0,0,5))
main()










