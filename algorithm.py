
from datetime import datetime, time, timedelta

def calcObjectiveFunction():
	size=len(cars)
	currentTime=customTime(time(0,0,0))
	newTime=currentTime.intValue()
	sum=0
	directionIndex=0
	while newTime<customTime(time(23,59,59)).intValue():
		downStraight=lights[directionIndex+1]
		downLeft=lights[directionIndex]
		upStraight=lights[(directionIndex+3)%8]
		upLeft=lights[(directionIndex+2)%8]
		sum+=downStraight.runOneCycle(currentTime.intValue())
		sum+=downLeft.runOneCycle(currentTime.intValue())
		sum+=upStraight.runOneCycle(currentTime.intValue()+downStraight.times[currentTime.time.hour].intValue())
		upLeftStartTime=currentTime.intValue()+max(downLeft.times[currentTime.time.hour].intValue(),downStraight.times[currentTime.time.hour].intValue())
		sum+=upLeft.runOneCycle(upLeftStartTime)
		directionIndex=(directionIndex+1)%2
		newTime=max(upLeftStartTime+upLeft.times[currentTime.time.hour].intValue(),currentTime.intValue()+downStraight.times[currentTime.time.hour].intValue()+upStraight.times[currentTime.time.hour].intValue())
		if(newTime<customTime(time(23,59,59)).intValue()):
			currentTime.setTimeFromInt(newTime)
	print(str(sum)+'/'+str(size))
	return sum/size
def initLightLanes():
	for i in range(8):
		times=[]
		for i in range(24):
			times.append(customTime(time(0,0,20)))
		lightObj=light(times)	
		lights.append(lightObj)
	for car in cars:
		direction=car.direction_from
		if(car.lane==0):
			lights[direction].addToLeft(car)
		elif(car.lane==1):
			lights[direction+1].addToStraigt(car)
		elif(car.lane==2):
			lights[direction+1].addToRight(car)

class customTime():
	def __init__(self, time):
		self.time=time
	def intValue(self):
		return self.time.hour*60*60+self.time.minute*60+self.time.second
	def addSeconds(self,second):
		self.time+=timedelta(seconds=second)
	def setTimeFromInt(self,seconds):
		print(str(seconds/(60*60)))
		self.time=time(seconds/(60*60),(seconds%(60*60))/60,(seconds%60))
class light():
	def __init__(self, times):
		self.times = times
		self.firstIterator=0
		self.secondIterator=0
		self.queue=[[],[]]
	def addToLeft(self,car):
		self.queue[0].append(car)
	def addToStraigt(self,car):
		self.queue[0].append(car)
	def addToRight(self,car):
		self.queue[1].append(car)
	def runOneCycle(self,startTime):
		sum=self.runOneLane(startTime, 0)
		sum+=self.runOneLane(startTime, 1)
		return sum
	def runOneLane(self,startTimeValue, lane):
		sum=0
		startTime=customTime(time(0,0,0))
		startTime.setTimeFromInt(startTimeValue)
		currentTime=startTime.intValue()
		carsWaitingBefore=0
		iterator=0
		if(lane==0):
			iterator=self.firstIterator
		else:
			iterator=self.secondIterator
		while  iterator<len(self.queue[lane]):
			car=self.queue[lane][iterator]
			if(car.time.intValue()<startTime.intValue()+self.times[startTime.time.hour].intValue()):	
				if(currentTime+carsWaitingBefore*waitingTime.intValue()<startTime.intValue()+self.times[startTime.time.hour].intValue()):	
					if(car.time.intValue()<=startTime.intValue()):
						sum+=carsWaitingBefore*waitingTime.intValue()+accelerateTime.intValue()+currentTime-car.time.intValue()
						carsWaitingBefore+=1
					elif (car.time.intValue()>startTime.intValue() and car.time.intValue()<startTime.intValue()+self.times[startTime.time.hour].intValue()):
						if (car.time.intValue()<currentTime+carsWaitingBefore*waitingTime.intValue()):
							carsWaitingBefore+=1
							sum+=carsWaitingBefore*waitingTime.intValue()+accelerateTime.intValue()+currentTime-car.time.intValue()
						elif(car.time.intValue()>currentTime+carsWaitingBefore*waitingTime.intValue()):
							sum+=0
							carsWaitingBefore=1
							currentTime=car.time.intValue()
					else:
						break
				iterator+=1
			else:
				break
		if(lane==0):
			self.firstIterator=iterator
		else:
			self.secondIterator=iterator
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
	file=open('data.txt', 'r')
	data=file.readlines()
	for line in data:
		args=line.strip().split(" ")	
		time=customTime(datetime.strptime(args[0], '%H:%M:%S').time())
		direction_from=int(args[1])
		direction_to=int(args[2])
		lane=int(args[3])
		cars.append(car(time, direction_from, direction_to, lane))
	return cars
def main():
	readData()
	initLightLanes()
	average=calcObjectiveFunction()
	print('Srednia '+str(average))

config_file = 'data.txt'
cars=[]
lights=[]
accelerateTime=customTime(time(0,0,5))
waitingTime=customTime(time(0,0,5))
main()










