
import matplotlib.pyplot as plt

def plot_sepal_width(setosa, versicolor, virginica):

    # Extract the sepal width
    setosa_swth = setosa['sepal_width']
    versicolor_swth = versicolor['sepal_width']
    virginica_swth = virginica['sepal_width']

    # Create a figure with 3 Axes (subplots), one for each variety 
    fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(12,4))

    # Histograms for setosa, versicolor and virginica
    ax1.hist(setosa_swth, label="setosa", color='red', edgecolor = 'black')
    ax2.hist(versicolor_swth, label="versicolor", color='blue', edgecolor = 'black')
    ax3.hist(virginica_swth, label="virginica", color='green', edgecolor = 'black')

    # Set the labels and legend
    for ax in (ax1, ax2, ax3):
        ax.legend()
        ax.set_xlabel('Sepal Width (cm)')
        ax.set_ylabel('Number')

    # Set the overall title for the figure
    fig.suptitle("Sepal Widths\n", fontsize=14, fontweight='bold')

    # Show the plot
    plt.show()

    return