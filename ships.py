from math import ceil


class Ship:
    def __init__(self, string):
        tmp = string.split(':')
        self.id = tmp[0]
        tmp = tmp[1]
        tmp = tmp.split()
        self.name = tmp[0]
        self.type = tmp[1]
    def printShip(self):
        print ("ID: ", self.id, " name: ", self.name, " type: ", self.type)

class Container:
    def __init__(self, string):
        tmp = string.split('/')
        field1 = tmp[0].split('-')
#        print field1
        self.origin = field1[0]
        self.dest = field1[1]
        self.id = field1[2]
        self.weight = tmp[1]
        field3 = tmp[2].split('@')
        self.type = field3[0]
        self.company = field3[1]
        self.price = tmp[3]
#        print self.origin
#        print self.dest
#        print self.id
#        print self.weight
#        print self.type
#        print self.company 
#        print self.price

    def setClass(self, ship):
        self.carrier = ship
    def printContainer(self):
        print(self.origin, self.dest, self.id, self.weight, self.type, self.company, self.price, "Ship: ")
        self.carrier.printShip()

f = open("dane.csv", "r")

shipline = f.readline()
shipline = shipline.split(",")

shipArr = []

for shqip in shipline:
    shipArr.append(Ship(shqip))

r = f.readline()

contArr = []

while r != "":
    line = r.split(',')
    x = 0;
    for cont in line:
        if cont != "" and cont != '\n':
            contArr.append(Container(cont))
            contArr[-1].setClass(shipArr[x])
        x = x + 1
    r = f.readline() 

##DATA BASE CREATED
##contArr contains all containers in the csv file

task1 = sum(1 for cont in contArr if cont.dest == "JP")
print ("Task 1:", task1)

print ("Task 2:")

def uniqueType(ships):
    types = []
    for ship in ships:
        if ship.type not in types:
            types.append(ship.type)
    return types

shipTypes = uniqueType(shipArr)

typeSums = []



for typ in shipTypes:
    suma = 0
    for ship in shipArr:
        if ship.type == typ:
            for cont in contArr:
                if cont.carrier == ship:
                    suma += 1
    typeSums.append((typ, suma))


typeAvgs = []

for suma in typeSums:
    countShips = 0
    for ship in shipArr:
        if ship.type == suma[0]:
            countShips += 1
    typeAvgs.append((suma[0], (suma[1]/countShips)))


typeAvgs.sort(key = lambda tup: tup[1])

print typeAvgs[-1]



print "Task 3:"

weightSum = 0.0;
contSum = 0.0;

for cont in contArr:
    if cont.type == "X1":
        contSum += 1.0
        weightSum += float(cont.weight)


print ceil(weightSum/contSum)

print "Task 4"

polishCompanies = []


for cont in contArr:
    if cont.company[-2:] == "pl" and cont.company not in polishCompanies:
        polishCompanies.append(cont.company)

polishCompaniesWithValues = []

for company in polishCompanies:
    suma = 0
    for cont in contArr:
        if cont.company == company:
            suma += 1
    polishCompaniesWithValues.append((company, suma))

polishCompaniesWithValues.sort(key = lambda tup: tup[1])

print polishCompaniesWithValues[-1]

print "Task 5"

loads = []

for cont in contArr:
    if cont.company[-2:] == "de" and  cont.origin == "DE":
        loads.append((cont.type, (float(cont.weight)/float(cont.price))))


loads.sort(key = lambda tup: tup[1])

print loads[-1]
