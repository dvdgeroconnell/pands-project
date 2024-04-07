
import matplotlib.pyplot as plt

def plot_sepal_width(setosa, versicolor, virginica):

    # Extract the sepal width
    setosa_swth = setosa['sepal_width']
    versicolor_swth = versicolor['sepal_width']
    virginica_swth = virginica['sepal_width']

    #plt.plot(setosa_swth, label="setosa", color='red')
    #plt.plot(versicolor_swth, label="versicolor", color='blue')
    #plt.plot(virginica_swth, label="virginica", color='green')

    # Create a figure with 3 Axes (subplots), one for each variety 
    fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(12,4))

    # Histogram for setosa
    ax1.hist(setosa_swth, label="setosa", color='red', edgecolor = 'black')
    ax1.legend()
    ax1.set_xlabel('Sepal Width (cm)')
    ax1.set_ylabel('Number')
    #ax1.set_title('Sepal Widths')

    # Histogram for versicolor
    ax2.hist(versicolor_swth, label="versicolor", color='blue', edgecolor = 'black')
    ax2.legend()
    ax2.set_xlabel('Sepal Width (cm)')
    ax2.set_ylabel('Number')
    #ax2.set_title('Sepal Widths')

    # Histogram for virginica
    ax3.hist(virginica_swth, label="virginica", color='green', edgecolor = 'black')
    ax3.legend()
    ax3.set_xlabel('Sepal Width (cm)')
    ax3.set_ylabel('Number')
    #ax3.set_title('Sepal Widths')

    # Set the overall title for the figure
    fig.suptitle("Sepal Widths\n", fontsize=14, fontweight='bold')

    # Show the plot
    plt.show()

    return