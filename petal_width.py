
import matplotlib.pyplot as plt

def plot_petal_width(setosa, versicolor, virginica):

    # Extract the petal width
    setosa_pwth = setosa['petal_width']
    versicolor_pwth = versicolor['petal_width']
    virginica_pwth = virginica['petal_width']

    # Create a figure with 3 Axes (subplots), one for each variety 
    fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(12,4))

    # Histograms for setosa, versicolor and virginica
    ax1.hist(setosa_pwth, label="setosa", color='red', edgecolor = 'black')
    ax2.hist(versicolor_pwth, label="versicolor", color='blue', edgecolor = 'black')
    ax3.hist(virginica_pwth, label="virginica", color='green', edgecolor = 'black')

    # Set the labels and legend
    for ax in (ax1, ax2, ax3):
        ax.legend()
        ax.set_xlabel('Petal Width (cm)')
        ax.set_ylabel('Number')

    # Set the overall title for the figure
    fig.suptitle("Petal Widths\n", fontsize=14, fontweight='bold')

    # Save the plot
    plt.savefig('hist_petal_width.png')

    return