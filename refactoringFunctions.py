if __name__ == "__main__":
    print("You must call this program from main.py!")
    choice = input("Press ENTER to exit...")
    from sys import exit
    exit()


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
def extractProperties(surfaceFile, dataFiles):
    
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
    array = np.genfromtxt(path + "\\rawSurfaceFiles\\" + str(dataFiles[int(surfaceFile)]))

    # Generates the x- and y-coordinates as well as the intensity matrix.
    time = array[0,:][1:]
    wavelength = array[:,0][1:]
    intensity = np.delete(np.delete(array, 0, 0), 0, 1)

    # Gets positive time log values.
    logTruncTime = np.log(time[time > 0])

    # Gets positive-time intensity values.
    intensPos = np.transpose(np.delete(intensity, range(len(time[time <= 0])), 1))
   
    # Displays the name of the file refactored.
    print(str(dataFiles[int(surfaceFile)]) + " has now had data extracted.")

    # Sets the refactored variable to True
    refactored=True

    return time, wavelength, intensity, logTruncTime, intensPos, refactored


### Refactors the data files to CSV files with index of wavelength and header of time.
def refactorDatasets(dataFiles):
    
    print("\n==================== Refactoring Datasets ====================\n")

    ### Checks if data files have been loaded.
    if len(dataFiles) == 0:
        print("No datasets have been specified, please detect datasets first.")
        return 0
    
    ### Imports only necessary functions; for slow computers.
    from numpy import genfromtxt, savetxt, delete
    from pandas import read_csv
    from os import getcwd, remove
    
    ### Iterates over each file for refactoring.
    for i in range(len(dataFiles)):

        ### Sets the file path.
        path = str(getcwd())

        ### Loads the data as a 2D NumPy array.
        array = genfromtxt(path + "\\rawDataFiles\\" + str(dataFiles[i]))

        ### Pandas has easier importing with CSV files.
        savetxt("csvData.csv", array, delimiter=",")

        ### Generating the array used as the actual Pandas df index.
        wavelength = delete(array[:,0], 0)

        ### Loads the CSV from storage and sets the index to the wavelength.
        df = read_csv("csvData.csv", header=0, index_col=0)
        df = df.set_index(wavelength)

        ### Sets the export location as the original filename with CSV extension.
        name = dataFiles[i][:-4]
        exportLocation = str(path + "\\refactoredDataFiles\\" + name + ".csv")

        ### Exports the refactored dataset  and removes the temporary CSV file.
        df.to_csv(exportLocation, sep=',')
        remove(path + "\\csvData.csv")
        print(str(name) + " has now been refactored.")

    return 1


