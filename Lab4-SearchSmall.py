# Lab4-SearchSmall.py

# opens list from file
myFile = open (# file path, "r")

lineCount = 0
# Lists
females = []  #female names
fCount = []   #count the number of females with this name
males = []    #male names
mCount = []   #count the number of males with this name

print("US Baby name data from 1995")

#search for a name
who = input("What name would you like to look for? ")

# for loop reads each line in the file

for line in myFile:
    line = line.strip()   #strip new line
    lineCount += 1
    #split the line into a lineList
    #splits the commas
    lineList = line.split (",")
    name = lineList [0]
    sex = lineList[1]
    count = int (lineList[2])
    if sex == "F":
        females.append(name)
        fCount.append(count)
    else:
        males.append(name)
        mCount.append(count)
# searches the female list
for name in females:
    if who == name:
        print ("Found in females, " +who)
        

#searches the male list
for name in males:
    if who == name:
        print ("Found in males, "+who)


#close file
myFile.close()



