if __name__ == "__main__":
    print("You must call this program from main.py!")
    choice = input("Press ENTER to exit...")
    from sys import exit
    exit()

### Coverts a value from science form two two decimal places.
def floatFormatting(valueToSquash):
    return "{:.2f}".format(valueToSquash)


### Iterates over an array to flatten the scientific values to two decimal places.
def applyFloatFormat(arrayToIterate):
    listToReturn = []
    for i in range(len(arrayToIterate)):
        listToReturn.append(floatFormatting(arrayToIterate[i]))
    return listToReturn


### Generates the figures used. Creates the overall figure and then individual figures all of which have the option of
### being saved.
def surfacePlotting(time, wavelength, intensity, logTruncTime, intensPos, refactored):

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
    while True:
        if saveFig.lower() == "y":

            # Saves the main figure.
            fileName = str(input("\n>>> Enter a filename: "))
            fileNamePath = str(os.getcwd() + "\\savedSurfacePlots\\" + fileName + ".png")
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
            plt.savefig(str(os.getcwd() + "\\savedSurfacePlots\\" + fileName + str("_individual_" + str(1)) + ".png"), format="png")
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
                plt.savefig(str(os.getcwd() + "\\savedSurfacePlots\\" + fileName + str("_individual_" + str(i + 2)) + ".png"), format="png")
                plt.close(tempFig2)

            # Closes the final figure object
            plt.close(fig)
            break

        elif saveFig.lower() =="n":
            plt.close(fig)
            break
        
        else:
            saveFig = str(input("\n>>> I'm sorry, I didn't catch that. Do you want to save this figure? (y/n): "))

    # Halts program execution.
    input("\n>>> Press ENTER to resume program...")

    return 1


### Plots all of the data from the desired file. This plot will be generated and displayed to
### the user but is not saved.
def plotSingleDataset(datasetChoice, directoryFiles, saveDialog=True, definedWavelengths=None, colormap="Spectral_r"):

    ### Tries to convert the dataset chosen to an integer type. If this fails then we return 0.
    try:
        datasetChoice = int(datasetChoice)
    
    except TypeError:
        return 0
    
    else:
        from os import getcwd
        from pandas import read_csv
        from matplotlib import pyplot as plt
        from seaborn import heatmap, color_palette
        from numpy import genfromtxt, delete
        
        ### Sets the file paths
        path = str(getcwd() + "\\refactoredDataFiles\\" + directoryFiles[datasetChoice-1])
        rawPath = str(getcwd() + "\\rawDataFiles\\" + directoryFiles[datasetChoice-1][:-4] + ".txt")

        ### Loads the data as a 2D NumPy array.
        array = genfromtxt(rawPath)

        ### Generating the array used as the actual Pandas df index.
        wavelength = delete(array[:,0], 0)
        time = delete(array[0,:], 0)

        ### Convert the axis lists into readable float types
        wavelengthFloat = applyFloatFormat(wavelength)
        timeFloat = applyFloatFormat(time)

        ### Tries to loadt the requested DataFrame. If this fails, then the function returns 0.
        try: 
            df = read_csv(path, header=0, index_col=0) 
        except FileNotFoundError:
            print("The requested file was not accessible, please try another file.")
            return 0

        ### Constructs the figure space and creates the two axes object for plotting.
        fig = plt.figure(figsize=(15,6), frameon=True, facecolor="white")
        ax0 = fig.add_subplot(1, 2, 1)
        ax1 = fig.add_subplot(1, 2, 2)
        
        ### Generates the heatmap for the data using Seaborn heatmap
        heatmap(df, cmap=color_palette("Spectral_r", as_cmap=True), ax=ax0)

        ### Sets the ticks and tick labels to the more readable float formats for the heatmap.
        ax0.set_xlabel("Time / s", fontsize="medium", fontweight="bold")
        ax0.set_ylabel("Wavelength / nm", fontsize="medium", fontweight="bold")
        ax0.set_xticks([x for x in range(0, len(timeFloat), 7)])
        ax0.set_yticks([x for x in range(0, len(wavelengthFloat), 19)])
        ax0.set_xticklabels([timeFloat[x] for x in range(0, len(timeFloat), 7)])
        ax0.set_yticklabels([wavelengthFloat[x] for x in range(0, len(wavelengthFloat), 19)])

        ### Extracts each intensity value at a certain wavelength for the duration of the experiemnt
        ### to a list. Each list is then stored in a bigger list of values.
        intensityValues = df.values.tolist()

        if definedWavelengths == None:
            ### Selects a sample of the intensityValues using the plottingValues list. This will select
            ### 6 wavelengths to display (regularly spaced intervals).
            plottingValues = [x for x in range(0, len(wavelength), (len(wavelength)//6))]

            ### Defines the plotting variables for the sample graph.
            ax1.plot(time, intensityValues[plottingValues[0]], '-r',
                     time, intensityValues[plottingValues[1]], '-y',
                     time, intensityValues[plottingValues[2]], '-g',
                     time, intensityValues[plottingValues[3]], '-c',
                     time, intensityValues[plottingValues[4]], '-b',
                     time, intensityValues[plottingValues[5]], '-m')
        
        elif definedWavelengths != None:
            ### Uses the defined wavelengths for plotting. Searches the raw wavelength array for the wavelengths
            ### specified and returns the indices for these positions.
            plottingValues = []
            wavelength = wavelength.tolist()
            for i in range(len(definedWavelengths)):
                plottingValues.append(wavelength.index(definedWavelengths[i]))

            ### Defines the plotting variables for the sample graph. This uses the returned position indices above.
            ax1.plot(time, intensityValues[plottingValues[0]], '-r',
                     time, intensityValues[plottingValues[1]], '-y',
                     time, intensityValues[plottingValues[2]], '-g',
                     time, intensityValues[plottingValues[3]], '-c',
                     time, intensityValues[plottingValues[4]], '-b',
                     time, intensityValues[plottingValues[5]], '-m')

        ### Sets the ticks and tick labels to the more readable float formats for the decay graph.
        ax1.set_xlabel("Time / s", fontsize="medium", fontweight="bold")
        ax1.set_ylabel("Intensity / arb.", fontsize="medium", fontweight="bold")
        ax1.set_xlim(-1,100)
        
        ### Formatting
        ax1.legend([wavelengthFloat[plottingValues[0]],
                    wavelengthFloat[plottingValues[1]],
                    wavelengthFloat[plottingValues[2]],
                    wavelengthFloat[plottingValues[3]],
                    wavelengthFloat[plottingValues[4]],
                    wavelengthFloat[plottingValues[5]]],
                    title="Wavelength / nm",
                    title_fontsize="medium",
                    fontsize="small",
                    labelspacing=0.7,
                    columnspacing=3.0
                    )

        ### Shows the figure containing the plots with some minor spacing adjustment. This code will always
        ### be called when under userChoice = 3, but will be ignored under userChoice = 4. This is because
        ### the latter needs to just save the files continuously.
        plt.subplots_adjust(wspace=0.250, bottom=0.165)
        if saveDialog == True:
            print("Drawing plot...")
            plt.show(block=False)

            ### Halts program execution until the user closes the plot window. This then closes all
            ### open figures as a safeguard measure.
            input("\n>>> Press ENTER to resume program...")

            ### Gives user the option to save the figure.
            saveFig = str(input("\n>>> Do you want to save this figure? (y/n): "))
            if saveFig.lower() == "y":
                fileName = str(input("\n>>> Enter a filename: "))
                fileName = str(getcwd() + "\\savedGeneralPlots\\" + fileName + ".png")
                plt.savefig(fileName, format="png")
        
        ### Saves the figus without creating the diaglog options for the user to go through. This path is used
        ### bulk plot saving and is only called under userChoice = 4.
        elif saveDialog == False:
            fileName = directoryFiles[datasetChoice-1][:-4]
            fileName = str(getcwd() + "\\savedGeneralPlots\\" + fileName + ".png")
            plt.savefig(fileName, format="png")

        plt.close("all")
        return 1


### Loop call to plotSingleDataset function which will generate graphs iteratively with the
### different available datasets.
def generatePlots(directoryFiles, colormap="Spectral_r"):
    for i in range(len(directoryFiles)):
        print("Plotting: " + str(directoryFiles[i][:-4]))
        plotSingleDataset(i, directoryFiles, saveDialog=False, colormap=colormap)
        print("Finished Plotting: " + str(directoryFiles[i][:-4] + "\n"))
    return 1


### Assigns the wavelengths to use as a list and returns them for use as the general 1D plot.
### This is not a necessary assignment but allows the user to choose whether they want specific
## wavelengths or whether they want the general equally-spaced wavelengths.
def getWavelengths():
    wavelengthList = []
    round = ["first", "second", "third", "fourth", "fifth", "sixth"]
    for i in range(6):
        try:
            wavelengthValue = float(input("\n>>> Enter the {round} wavelength in full: ".format(round=round[i])))
            wavelengthList.append(wavelengthValue)
        except ValueError:
            print("\nThe values entered do not belong to the float type.")
            print("Please repeat the process and enter float values.")
            print("Returning to main menu.")
            return 0
    return wavelengthList

