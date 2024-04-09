
import matplotlib.pyplot as plt

def plot_petal_length(setosa, versicolor, virginica):

    # Extract the petal length
    setosa_plen = setosa['petal_length']
    versicolor_plen = versicolor['petal_length']
    virginica_plen = virginica['petal_length']

    # Create a figure with 3 Axes (subplots), one for each variety 
    fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(12,4))

    # Histograms for setosa, versicolor and virginica
    ax1.hist(setosa_plen, label="setosa", color='red', edgecolor = 'black')
    ax2.hist(versicolor_plen, label="versicolor", color='blue', edgecolor = 'black')
    ax3.hist(virginica_plen, label="virginica", color='green', edgecolor = 'black')

    # Set the labels and legend
    for ax in (ax1, ax2, ax3):
        ax.legend()
        ax.set_xlabel('Petal Length (cm)')
        ax.set_ylabel('Number')

    # Set the overall title for the figure
    fig.suptitle("Petal Lengths\n", fontsize=14, fontweight='bold')

    # Save the plot
    plt.savefig('hist_petal_length.png')

    return