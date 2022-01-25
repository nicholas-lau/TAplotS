if __name__ == "__main__":
    print("You must call this program from main.py!")
    choice = input("Press ENTER to exit...")
    from sys import exit
    exit()


### Allows the user to specify the colour map they wish to use.
def setColorMap():
    from numpy.random import rand
    from numpy import sort as sortNP
    from seaborn import heatmap, color_palette
    from matplotlib import pyplot as plt
    from matplotlib import cm
    
    ### Generates a random array (100,100) and then sorts the array from low to high L-R and T-B. Inverts the finalarray to achieve
    ### low to high L-R, B-T.
    array = rand(100, 100)
    array = sortNP(array, axis=0)
    array = sortNP(array, axis=1, )
    array = array[::-1]
    
    ### Creates the figure object for all of the colour map plots for displaying to the user.
    fig = plt.figure(figsize=(15,6), frameon=True, edgecolor="gainsboro", facecolor="gainsboro")
    
    ### Adds subplots to the figure for the user to select from.
    ax0 = fig.add_subplot(2, 3, 1, title="1")
    ax1 = fig.add_subplot(2, 3, 2, title="2")
    ax2 = fig.add_subplot(2, 3, 3, title="3")
    ax3 = fig.add_subplot(2, 3, 4, title="4")
    ax4 = fig.add_subplot(2, 3, 5, title="5")
    ax5 = fig.add_subplot(2, 3, 6, title="6")

    ### Adds additional vertical spacing.
    fig.subplots_adjust(hspace=0.3)
    
    ### Generates the heatmaps with the sorted array using various colour palettes.
    heatmap(array, cmap=color_palette("Spectral_r", as_cmap=True), ax=ax0, xticklabels=False, yticklabels=False)
    heatmap(array, cmap=color_palette("coolwarm", as_cmap=True), ax=ax1, xticklabels=False, yticklabels=False)
    heatmap(array, cmap=color_palette("icefire", as_cmap=True), ax=ax2, xticklabels=False, yticklabels=False)
    heatmap(array, cmap=color_palette("YlOrBr_r", as_cmap=True), ax=ax3, xticklabels=False, yticklabels=False)
    heatmap(array, cmap=color_palette("Blues_r", as_cmap=True), ax=ax4, xticklabels=False, yticklabels=False)
    heatmap(array, cmap=color_palette("dark:salmon", as_cmap=True), ax=ax5, xticklabels=False, yticklabels=False)

    ### Shows the heatmaps to the user to allow them to select one.
    plt.show(block=False)

    ### Halts program execution until the user closes the plot window. This then closes all
    ### open figures as a safeguard measure.
    input("\n>>> Press ENTER to resume program...")
    
    ### Gives user the option to select the colour map.
    colormapValue = str(input("\n>>> Enter the number of the colour map you wish to use: "))

    ### Creates a list of the available colour maps.
    colormapList = [cm.jet, "Spectral_r", "coolwarm", "icefire", "YlOrBr_r", "Blues_r"]

    ### Creates the while loop to handle user input. Gets the value that the user wants and attempts conversion
    ### the integer type. If this fails, user is asked to re-submit their choice. If this succeeds then the value
    ### is compared to the allowed values and will only allow the function to return when a number between 1 and 6
    ### is chosen.
    while True:
        try:
            colormapValue = int(colormapValue)
            if colormapValue >= 1 and colormapValue <= 6:
                colormap = colormapList[colormapValue - 1]
                print("\nColourmap " + str(colormapValue) + " was chosen. Returning to options menu.")
                break
            else:
                colormapValue = str(input("\n>>> Please enter a number between 1 and 6: "))
            break
        except ValueError:
            print("\nThe value entered does not belong to the integer type.")
            colormapValue = str(input("\n>>> Please enter a number between 1 and 6: "))
    
    plt.close("all")

    return colormap
