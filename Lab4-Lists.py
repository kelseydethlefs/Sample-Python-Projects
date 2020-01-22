# Lab4-Lists.py

# opens list from file.
myFile = open (# filepath, "r")

#prints list using for-loop
for line in myFile:
    line = line.strip()  #takes out new line
    lineList = line.split(",")  #splits the information with a comma
    print(line)
