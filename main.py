### Imports.
import os, matplotlib.cm
import refactoringFunctions as rf
import mainMenuFunctions as mmf
import figurePlottingFunctions as fpf
import optionsFunctions as of

### Intro message.
mmf.introMessage()


### Sets the path and checks the file directories.
path = os.getcwd()
mmf.directoryChecks()
mmf.displayMainMenu()


### Initialises some of the global variables necessary for execution.
time = None
wavelength = None
intensity = None
logTruncTime = None
intensPos = None
refactored = False
surfaceDataFiles = []
rawDataFiles = []
colormap = matplotlib.cm.jet


### Begins the main program execution and allows the user to choose the jobs they want to do.
userChoice = str(input("\n>>> Enter the number of the job you wish to do: "))
while True:


    ### Loads all of the surface datasets and makes the program aware of their existence.
    if userChoice == "1":
        surfaceDataFiles = mmf.loadSurfaceFiles()
        mmf.displayMainMenu()
        userChoice = str(input("\n>>> Enter the number of the job you wish to do: "))


    ### Loads all of the raw data files and makes the program aware of their existence.
    elif userChoice == "2":
        rawDataFiles = mmf.loadRawFiles()
        mmf.displayMainMenu()
        userChoice = str(input("\n>>> Enter the number of the job you wish to do: "))


    ### Extracts components from a specific surface dataset and pulls the information from the necessary areas. Crops
    ### some of the data for the cropped plots.
    elif userChoice == "3":
        time, wavelength, intensity, logTruncTime, intensPos, refactored = rf.extractProperties(rf.fileChoice(surfaceDataFiles), surfaceDataFiles)
        mmf.displayMainMenu()
        userChoice = str(input("\n>>> Enter the number of the job you wish to do: "))


    ### Refactors the raw data files to more-legible CSV files that can be manipulated by other
    ### software. Index is set to wavelength and header is set to time.
    elif userChoice == "4":
        returnCheck4 = rf.refactorDatasets(rawDataFiles)
        if returnCheck4 == 1:
            print("\nAll datasets have now been refactored.")
            returnCheck4 = 0
        mmf.displayMainMenu()
        userChoice = str(input("\n>>> Enter the number of the job you wish to do: "))


    ### Plots a single surface dataset that has been refactored and will then give the user the option
    ### to choose to save the images.
    elif userChoice == "5":
        returnCheck5 = fpf.surfacePlotting(time, wavelength, intensity, logTruncTime, intensPos, refactored)
        if returnCheck5 == 0:
            print("\nYou must extract properties from a dataset before plotting!")
        mmf.displayMainMenu()
        userChoice = str(input("\n>>> Enter the number of the job you wish to do: "))


    ### Takes a single dataset and plots it. This is useful for seeing what a single dataset
    ### looks like. The file can then be saved.
    elif userChoice == "6":
        availableFiles = mmf.loadRefactoredFiles()
        plottingChoice = str(input("\n>>> Enter the number of the file you wish to plot: "))
        print("\n==================== Generating Plots ====================\n")
        returnCheck6 = fpf.plotSingleDataset(plottingChoice, availableFiles, colormap=colormap)
        if returnCheck6 == 1:
            print("\nGraph was successfully plotted.")
            returnCheck6 = 0
        mmf.displayMainMenu()
        userChoice = str(input("\n>>> Enter the number of the job you wish to do: "))
    

    ### Takes a single dataset and then plots it. The wavelengths in this path are specified
    ### exactly by the user and will be plotted accordingly. The user must know what these wavelengths
    ### are in advance from their file.
    elif userChoice == "7":
        availableFiles = mmf.loadRefactoredFiles()
        plottingChoice = str(input("\n>>> Enter the number of the file you wish to plot: "))
        wavelengthsToSample = fpf.getWavelengths()
        if wavelengthsToSample == 0:
            mmf.displayMainMenu()
            userChoice = str(input("\n>>> Enter the number of the job you wish to do: "))
        else:
            print("\n==================== Generating Plots ====================\n")
            returnCheck7 = fpf.plotSingleDataset(plottingChoice, availableFiles, definedWavelengths=wavelengthsToSample, colormap=colormap)
            if returnCheck7 == 1:
                print("\nGraph was successfully plotted.")
                returnCheck7 = 0
            mmf.displayMainMenu()
            userChoice = str(input("\n>>> Enter the number of the job you wish to do: "))


    ### Takes all of the available refactors and plots them. This is a bulk plotting scheme
    ### and will not ask the user to save each each graph (automatically does). The plots are
    ### not shown in this route.
    elif userChoice == "8":
        availableFiles = mmf.loadRefactoredFiles()
        print("\n==================== Generating Plots ====================\n")
        returnCheck8 = fpf.generatePlots(availableFiles, colormap=colormap)
        if returnCheck8 == 1:
            print("Plots were successfully saved.")
            returnCheck8 = 0
        mmf.displayMainMenu()
        userChoice = str(input("\n>>> Enter the number of the job you wish to do: "))


    ### Allows the user to access the options menu. If the program grows, this will be abstracted to a second folder.
    ### Currently, the user may only set the heatmap colour.
    elif userChoice == "9":
        mmf.displayOptionsMenu()
        optionsChoice = str(input("\n>>> Enter the number of the option you wish to change: "))
        while True:
            if optionsChoice == "1":
                colormap = of.setColorMap()
                mmf.displayOptionsMenu()
                optionsChoice = str(input("\n>>> Enter the number of the option you wish to change: "))
            elif optionsChoice == "2":
                print("\nReturning to Main Menu.")
                mmf.displayMainMenu()
                userChoice = str(input("\n>>> Enter the number of the job you wish to do: "))
                break
            else:
                optionsChoice = str(input("\n>>> I'm sorry, I didn't catch that. Please enter the number corresponding to the option you wish to change: "))


    ### Breaks the while loop and exits the program.
    elif userChoice == "10":
        break
    

    ### Handles all other inputs.
    else:
        userChoice = str(input("\n>>> I'm sorry, I didn't catch that. Please enter the number corresponding to the job you wish to do: "))


### Exits the program.
print("\nThanks for using TAplotS!")
input("Press ENTER to exit...")
exit()
