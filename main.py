### Imports.
import os
import functionDefinitions as fd

### Intro message.
fd.introMessage()


### Sets the path and checks the file directories.
path = os.getcwd()
fd.directoryChecks()
fd.displayMainMenu()


### Initialises some of the global variables necessary for execution.
time = None
wavelength = None
intensity = None
logTruncTime = None
intensPos = None
refactored = False
dataFiles = []


### Begins the main program execution and allows the user to choose the jobs they want to do.
userChoice = str(input("\n>>> Enter the number of the job you wish to do: "))
while True:


    ### Loads all of the datasets and makes the program aware of their existence.
    if userChoice == "1":
        dataFiles = fd.loadFiles()
        fd.displayMainMenu()
        userChoice = str(input("\n>>> Enter the number of the job you wish to do: "))


    ### Refactors a specific dataset and pulls the information from the necessary areas. Crops
    ### some of the data for the cropped plots.
    elif userChoice == "2":
        time, wavelength, intensity, logTruncTime, intensPos, refactored = fd.refactorDataset(fd.fileChoice(dataFiles), dataFiles)
        fd.displayMainMenu()
        userChoice = str(input("\n>>> Enter the number of the job you wish to do: "))


    ### Plots a single dataset that has been refactored and will then give the user the option
    ### to choose to save the images.
    elif userChoice == "3":
        confirm = fd.figurePlotting(time, wavelength, intensity, logTruncTime, intensPos, refactored)
        if confirm == 0:
            print("\nYou must refactor a dataset before plotting!")
        fd.displayMainMenu()
        userChoice = str(input("\n>>> Enter the number of the job you wish to do: "))


    ### Breaks the while loop and exits the program.
    elif userChoice == "4":
        break
    

    ### Handles all other inputs.
    else:
        userChoice = str(input("\n>>> I'm sorry, I didn't catch that. Please enter the number corresponding to the job you wish to do: "))

### Exits the program.
print("\nThanks for using TAplotS!")
input("Press ENTER to exit...")
exit()
