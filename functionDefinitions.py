if __name__ == "__main__":
    print("You must call this program from main.py!")
    choice = input("Press ENTER to exit...")
    from sys import exit
    exit()


### Prints the intro screen.
def introMessage():
    print("""
        #################################################################################
        #################################################################################
        #################################################################################
        ############                                                         ############
        ############                         TAplotS                         ############
        ############                      Kate Robertson,                    ############
        ############                       Nicholas Lau                      ############
        ############                                                         ############
        ############                        21/01/2021                       ############
        ############                                                         ############
        #################################################################################
        #################################################################################
        #################################################################################
        \n""")
    return 1


### Tries to create the necessary directories for manipulating files and saving. Allows for portability.
### If folders exist then they are not created.
def directoryChecks():
    from os.path import isdir
    from os import getcwd, mkdir
    
    print("\n==================== Performing Directory Checks ====================\n")
    # Sets the path to the current working directory.
    path = str(getcwd())
    
    # This block determines if the necessary folders already exist. If they do not, then
    # the function creates them.
    if not isdir(str(path + "\\surfaceFiles\\")):
        mkdir(str(path + "\\surfaceFiles\\"))
        print("Creating 'surfaceFiles' folder...")
        print("\nPlease place the surface data files into the 'surfaceFiles' directory and choose\nto detect datasets before refactoring or plotting.\n")
    else:
        print("The folder 'surfaceFiles' exists! Moving to next folder.\n")
    
    if not isdir(str(path + "\\refactoredDatasets\\")):
        mkdir(str(path + "\\refactoredDatasets\\"))
        print("Creating 'refactoredDatasets' folder...\n")
    else:
        print("The folder 'refactoredDatasets' exists! Moving to next folder.\n")
    
    if not isdir(str(path + "\\savedPlots\\")):
        mkdir(str(path + "\\savedPlots\\"))
        print("Creating 'savedPlots' folder...\n")
    else:
        print("The folder 'savedPlots' exists!\n")

    input(">>> Directory checks complete. Press ENTER to continue...")
    return 1


### Simple function to display the main menu options. This is used multiple times and serves only
### to be a large print statement.
def displayMainMenu():
    # Declares the main menu options. This can be added to later. This is useful for modular code.
    print("\n==================== Main Menu ====================\n")
    userOperations = ["Detect Datasets",
                    "Refactor Datasets and Export",
                    "Plot and Display a Dataset",
                    "Exit"]

    # Prints the list of main menu options alongside a counter variable for easier job selection.
    for count, operation in enumerate(userOperations):
        print(count+1, operation)

    return 1


### Displays the raw data files found within the 'surfaceFiles' folder. This then prints the files to the
### user to alter directory and call the method again. A list of the directory files is then returned.
def loadFiles():
    from os import listdir
    print("\n==================== Loading Files ====================\n")
    print("The following files were found in the folder 'surfaceFiles':\n")
    directoryFiles = listdir("surfaceFiles")
    for index, name in enumerate(directoryFiles):
        print(index + 1, name)
    return directoryFiles


### Enumerates the list of files and then allows the user to choose one. The enumerated file choice is then
### decremented and returned to the main execution environment.
def fileChoice(dataFiles):
    print("\n==================== Choose A File ====================\n")
    for index, name in enumerate(dataFiles):
        print(index + 1, name)
    choice = str(input("\n>>> Please choose the number associated with the file you want to refactor:"))
    choice = str(int(choice) - 1)
    return choice


### Opens the specified dataset and extracts the necessary data from the main array. Positive-time manipulations
### are then performed and the function returns the extracted time and wavelength 1D arrays, the log of the positive-
### time 1D array and the 2D truncated intensity and main intensity arrays.
def refactorDataset(surfaceFile, dataFiles):
    
    print("\n==================== Refactoring {name} ====================\n".format(name=dataFiles[int(surfaceFile)]))

    # Checks if data files have been loaded.
    if len(dataFiles) == 0:
        print("No dataset has been specified, please load dataset first.")
        return 0
    
    # Imports only necessary functions; for slow computers.
    import numpy as np
    from os import getcwd

    # Sets the file path.
    path = str(getcwd())

    # Loads the data as a 2D NumPy array.
    array = np.genfromtxt(path + "\\surfaceFiles\\" + str(dataFiles[int(surfaceFile)]))

    # Generates the x- and y-coordinates as well as the intensity matrix.
    time = array[0,:][1:]
    wavelength = array[:,0][1:]
    intensity = np.delete(np.delete(array, 0, 0), 0, 1)

    # Gets positive time log values.
    logTruncTime = np.log(time[time > 0])

    # Gets positive-time intensity values.
    intensPos = np.transpose(np.delete(intensity, range(len(time[time <= 0])), 1))
   
    # Displays the name of the file refactored.
    print(str(dataFiles[int(surfaceFile)]) + " has now been refactored.")

    # Sets the refactored variable to True
    refactored=True

    return time, wavelength, intensity, logTruncTime, intensPos, refactored


### Generates the figures used. Creates the overall figure and then individual figures all of which have the option of
### being saved.
def figurePlotting(time, wavelength, intensity, logTruncTime, intensPos, refactored):

    # Handles plotting before refactoring.
    if refactored == False:
        return 0

    from matplotlib import pyplot as plt
    from matplotlib import cm
    import os

    # Creates the figure object.
    plt.rc("font", size=11)
    fig = plt.figure(figsize=(10, 8), dpi=100, facecolor="white")

    # Creates the general axis objects and adds them to the main figure object.
    ax0 = fig.add_subplot(2, 2, 1)
    ax1 = fig.add_subplot(2, 2, 2)
    ax2 = fig.add_subplot(2, 2, 3)
    ax3 = fig.add_subplot(2, 2, 4)

    # Creates the heatmap axis objects.
    ax0Plot = ax0.pcolormesh(wavelength, logTruncTime, intensPos, cmap=cm.jet, vmin=0, vmax=0.035, shading="gouraud", antialiased=True)
    ax1Plot = ax1.pcolormesh(time, wavelength, intensity, cmap=cm.jet, vmin=0, vmax=0.035, shading="gouraud", antialiased=True)
    ax2Plot = ax2.pcolormesh(time, wavelength, intensity, cmap=cm.jet, vmin=0, vmax=0.035, shading="gouraud", antialiased=True)
    ax3Plot = ax3.pcolormesh(time, wavelength, intensity, cmap=cm.jet, vmin=0, vmax=0.035, shading="gouraud", antialiased=True)

    # Crops the x-limits for other graphs.
    ax2.set_xlim(0, 5)
    ax3.set_xlim(0, 100)

    # Formatting.
    ax0.set_ylabel("log(Time Delay) / log(ps)", fontsize="medium", fontweight="bold")
    ax0.set_xlabel("Wavelength / nm", fontsize="medium", fontweight="bold")
    ax1.set_xlabel("Time Delay / ps", fontsize="medium", fontweight="bold")
    ax1.set_ylabel("Wavelength / nm", fontsize="medium", fontweight="bold")
    ax2.set_xlabel("Time Delay / ps", fontsize="medium", fontweight="bold")
    ax2.set_ylabel("Wavelength / nm", fontsize="medium", fontweight="bold")
    ax3.set_xlabel("Time Delay / ps", fontsize="medium", fontweight="bold")
    ax3.set_ylabel("Wavelength / nm", fontsize="medium", fontweight="bold")
    fig.colorbar(ax0Plot, ax=ax0)
    fig.colorbar(ax1Plot, ax=ax1)
    fig.colorbar(ax2Plot, ax=ax2)
    fig.colorbar(ax3Plot, ax=ax3)
    fig.tight_layout(h_pad=2.0, w_pad=3.0)

    # Allows program execution whilst figure displays.
    print("Drawing plot...")
    plt.show(block=False)

    # Halts program execution.
    input("\n>>> Press ENTER to resume program...")
    
    # Gives user the option to save the figure.
    saveFig = str(input("\n>>> Do you want to save this figure? (y/n): "))
    if saveFig.lower() == "y":

        # Saves the main figure.
        fileName = str(input("\n>>> Enter a filename: "))
        fileNamePath = str(os.getcwd() + "\\savedPlots\\" + fileName + ".png")
        plt.savefig(fileNamePath, format="png")

        # Generates the first individual figure and saves it.
        plt.rc("font", size=14)
        tempFig1 = plt.figure(figsize=(8, 8), tight_layout=True)
        tempAx1 = tempFig1.add_subplot(1, 1, 1)
        tempAx1Plot = tempAx1.pcolormesh(wavelength, logTruncTime, intensPos, cmap=cm.jet, vmin=0, vmax=0.035, shading="gouraud", antialiased=True)
        
        # More formatting.
        tempAx1.set_ylabel("log(Time Delay) / log(ps)", fontsize="medium", fontweight="bold")
        tempAx1.set_xlabel("Wavelength / nm", fontsize="medium", fontweight="bold")
        tempFig1.colorbar(tempAx1Plot, ax=tempAx1)
        plt.savefig(str(os.getcwd() + "\\savedPlots\\" + fileName + str("_individual_" + str(1)) + ".png"), format="png")
        plt.close(tempFig1)

        for i in range(3):
            
            # Generates the remaining individual cropped figures.
            tempFig2 = plt.figure(figsize=(8, 8), tight_layout=True)
            tempAx2 = tempFig2.add_subplot(1, 1, 1)
            tempAx2Plot = tempAx2.pcolormesh(time, wavelength, intensity, cmap=cm.jet, vmin=0, vmax=0.035, shading="gouraud", antialiased=True)
            
            # Defines the limits for the cropped figures.
            if i == 1:
                tempAx2.set_xlim(0, 5)
                
            elif i == 2:
                tempAx2.set_xlim(0, 100)
            
            # Even More formatting.
            tempAx2.set_xlabel("Time Delay / ps", fontsize="medium", fontweight="bold")
            tempAx2.set_ylabel("Wavelength / nm", fontsize="medium", fontweight="bold")
            tempFig2.colorbar(tempAx2Plot, ax=tempAx2)

            # Saves the remaining cropped figures.
            plt.savefig(str(os.getcwd() + "\\savedPlots\\" + fileName + str("_individual_" + str(i + 2)) + ".png"), format="png")
            plt.close(tempFig2)
        
        # Closes the final figure object
        plt.close(fig)
    
    elif saveFig.lower() =="n":
        plt.close(fig)

    # Halts program execution.
    input("\n>>> Press ENTER to resume program...")

    return 1