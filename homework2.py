# write a python program for age by using functions
def calculateAge():
    birthYear:int = 1988
    currentYear:int = 2024
    currentAge:int = currentYear - birthYear
    print(currentAge)
calculateAge()

# calculate area of rectangle by using fucntions
def calculateAreaRectangle():
    length:int = 10
    width:int = 5
    area:int = length * width
    print(area)
calculateAreaRectangle()

# calculate the area of a cube
def calculateAreaCube():
    lenghtSide:int = 10
    formula:int = 6 * (lenghtSide)**2
    print(formula)
calculateAreaCube()

#calculate the area of the circle by using functions
def calculateAreaCircle():
    radiusCircle:int = 5
    pie:int = 3.1416
    area:int = pie * (radiusCircle)**2
    print(area)
calculateAreaCircle()

#calculate the percentage of the student using functions
def calculatePercentage():
    totalMarks:int = 570
    obtainedMarks:int = 517
    percentage:int = (obtainedMarks / totalMarks) * 100
    print(percentage)
calculatePercentage()

#convert the temprature from cel to far and vice versa
def tempInCelsius():
    tempFarenhiet:int = 45
    tempCelsius:int = (tempFarenhiet * 5/9 ) - 32
    print(tempCelsius)
def tempInFarenhiet():
    tempCelsius:int = 45
    tempFarenhiet:int = (tempCelsius * 9/5 ) + 32
    print(tempFarenhiet)
tempInCelsius()
tempInFarenhiet()

#convert sec in min and vice versa
def inMinutes():
    a:int = 120
    inMin:int = a / 60
    print(inMin)
def inSeconds():
    a:int = 120
    inSeconds:int = a * 60
    print(inSeconds)
inMinutes()
inSeconds()

#calculate the volume of the cylinder with functions
def calculateVolume():
    heightCylinder:int = 5.5
    radiusCylinder:int = 3.5
    pie :int = 3.1416
    volume:int = pie * (radiusCylinder)**2 *heightCylinder
    print(volume)
calculateVolume()

#calculate the BMI of a person using functions
def calculateBMI():
    weight:int = 80
    height:int = 1.5 
    secondheight:int = height * height
    BMIperson:int = weight / secondheight
    print(BMIperson)
calculateBMI()