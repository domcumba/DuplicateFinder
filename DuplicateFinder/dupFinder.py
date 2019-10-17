from os import walk
import collections
import os

#Get the path that the user wants to search through
userPath = input("Please copy and paste the directory you want to search : ")

dumpFolder = input("Please enter a directory where you would like to save the duplicates: ")

#Create the dump directory to be used later
os.mkdir(dumpFolder)

#Create an initial list of all the filenames that the search finds
directoryList = []
for (root, dirs, files) in walk(userPath):
    directoryList.extend(files)

#remove duplicate filenames and place them inside a new list containing only duplicated
seen = {}
dupes = []

for x in directoryList:
    if x not in seen:
        seen[x] = 1
    else:
        if seen[x] == 1:
            dupes.append(x)
        seen[x] += 1

#find all the paths that have occurneces of duplicates and store them in a list
dupPaths = []
for i in range(len(dupes)):
    for root, dirs, files in walk(userPath):
        if dupes[i] in files:
            dupPaths.append(root + "\\" + dupes[i])
print(dupPaths)

#create report file to inform user of names and location of all duplicates
reportFile = open(dumpFolder + "\\report.txt", "w+")
maxWidth = max(len(dupPaths) for filename in dupPaths)
    
#move files into custom directory
counter = 0;
for i in range(len(dupes)):
    for j in range(directoryList.count(dupes[i])):
        print("TEST")
        ext = os.path.splitext(dupPaths[counter])
        num = str(counter)
        newName = dupes[i] + "(" + num +")" + ext[1]
        size = os.path.getsize(dupPaths[counter])
        reportFile.write(dupes[i].ljust(10) + dupPaths[counter].rjust(30) + str(size).rjust(30) + newName.rjust(30) + "\n")
        os.rename(dupPaths[counter], dumpFolder + "\\" + dupes[i] + "(" + num +")" + ext[1])
        counter += 1
reportFile.close()

input('Press ENTER to exit')
print("Goodbye")
