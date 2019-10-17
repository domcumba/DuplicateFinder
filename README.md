# DuplicateFinder
Python program I developed during my internship that allowed me to easily traverse directories and find duplicated files

## How To Run
There is file in the "_pycache_" folder called "_dupFinder.cpython-37.pyc_". Running this will bring up a command window that asks the user for the parent directory that they want to search. Every directory inside this parent directory will be searched for duplicated files.

Once all sub-directories have been searched the user will be asked to give a target directory to store the duplicated files and a report stating what they were, where they were found, the size of the files, and the new names of those files. Since the program makes a new directory, the user must enter a directory that __does not exist already.__ 
