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
        ############                          V 1.1                          ############
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
    
    # Creates 'rawSurfacePlots' folder.
    if not isdir(str(path + "\\rawSurfaceFiles\\")):
        mkdir(str(path + "\\rawSurfaceFiles\\"))
        print("Creating 'rawSurfaceFiles' folder...")
        print("\nPlease place the surface data files into the 'rawSurfaceFiles' directory and choose\nto detect files before extracting or plotting.\n")
    else:
        print("The folder 'rawSurfaceFiles' exists! Moving to next folder.\n")
    
    # Creates 'refactoredDataFiles' folder.
    if not isdir(str(path + "\\refactoredDataFiles\\")):
        mkdir(str(path + "\\refactoredDataFiles\\"))
        print("Creating 'refactoredDataFiles' folder...\n")
    else:
        print("The folder 'refactoredDataFiles' exists! Moving to next folder.\n")
    
    # Creates 'savedSurfacePlots' folder.
    if not isdir(str(path + "\\savedSurfacePlots\\")):
        mkdir(str(path + "\\savedSurfacePlots\\"))
        print("Creating 'savedSurfacePlots' folder...\n")
    else:
        print("The folder 'savedPlots' exists!\n")

    # Creates 'savedGeneralPlots' folder.
    if not isdir(str(path + "\\savedGeneralPlots\\")):
        mkdir(str(path + "\\savedGeneralPlots\\"))
        print("Creating 'savedGeneralPlots' folder...\n")
    else:
        print("The folder 'savedGeneralPlots' exists!\n")

    # Creates 'rawDataFiles' folder.
    if not isdir(str(path + "\\rawDataFiles\\")):
        mkdir(str(path + "\\rawDataFiles\\"))
        print("Creating 'rawDataFiles' folder...")
        print("\nPlease place the raw data files into the 'rawDataFiles' directory and choose\nto detect datasets before refactoring or plotting.\n")
    else:
        print("The folder 'rawDataFiles' exists! Moving to next folder.\n")

    # Halts program execution.
    input(">>> Directory checks complete. Press ENTER to continue...")
    return 1


### Simple function to display the main menu options. This is used multiple times and serves only
### to be a large print statement.
def displayMainMenu():
    # Declares the main menu options. This can be added to later. This is useful for modular code.
    print("\n==================== Main Menu ====================\n")
    userOperations = ["Detect Surface Datasets",
                    "Detect Raw Datasets",
                    "Extract Properties from a Surface Dataset",
                    "Refactor Raw Datasets and Export",
                    "Plot and Display a Surface Dataset",
                    "Plot and Display a Dataset (General Wavelengths)",
                    "Plot and Display a Dataset (Defined Wavelengths)",
                    "Plot and Save all Datasets",
                    "Options",
                    "Exit"]

    # Prints the list of main menu options alongside a counter variable for easier job selection.
    for count, operation in enumerate(userOperations):
        print(count+1, operation)

    return 1


### Simple function to display the main menu options. This is used multiple times and serves only
### to be a large print statement.
def displayOptionsMenu():
    ### Declares the main menu options. This can be added to later. This is useful for modular code.
    print("\n==================== Options Menu ====================\n")
    userOperations = ["Set Heatmap Colour Palette",
                    "Exit"]

    ### Prints the list of main menu options alongside a counter variable for easier job selection.
    for count, operation in enumerate(userOperations):
        print(count+1, operation)

    return 1


### Displays the raw data files found within the 'surfaceFiles' folder. This then prints the files to the
### user to alter directory and call the method again. A list of the directory files is then returned.
def loadSurfaceFiles():
    from os import listdir
    print("\n==================== Loading Surface Files ====================\n")
    print("The following files were found in the folder 'surfaceFiles':\n")
    directoryFiles = listdir("rawSurfaceFiles")
    for index, name in enumerate(directoryFiles):
        print(index + 1, name)
    return directoryFiles


### Displays the refactored data files found within the 'refactoredDataFiles' folder. This then prints the
### files to the user to alter directory and call the method again. A list of the directory files is then returned.
def loadRefactoredFiles():
    from os import listdir
    print("\n==================== Loading Refactored Files ====================\n")
    print("The following files were found in the folder 'refactoredDataFiles':\n")
    directoryFiles = listdir("refactoredDataFiles")
    for index, name in enumerate(directoryFiles):
        print(index + 1, name)
    return directoryFiles


### Displays the raw data files found within the 'rawDataFiles' folder. This then prints the files to the
### user to alter directory and call the method again. A list of the directory files is then returned.
def loadRawFiles():
    from os import listdir
    print("\n==================== Loading Cropped Raw Files ====================\n")
    print("The following files were found in the folder 'rawDataFiles':\n")
    directoryFiles = listdir("rawDataFiles")
    for index, name in enumerate(directoryFiles):
        print(index + 1, name)
    return directoryFiles