
import matplotlib.pyplot as plt

def plot_sepal_length(setosa, versicolor, virginica):

    # Extract the sepal length
    setosa_slen = setosa['sepal_length']
    versicolor_slen = versicolor['sepal_length']
    virginica_slen = virginica['sepal_length']

    # Create a figure with 3 Axes (subplots), one for each variety 
    fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(12,4))

    # Histograms for setosa, versicolor and virginica
    ax1.hist(setosa_slen, label="setosa", color='red', edgecolor = 'black')
    ax2.hist(versicolor_slen, label="versicolor", color='blue', edgecolor = 'black')
    ax3.hist(virginica_slen, label="virginica", color='green', edgecolor = 'black')

    # Set the labels and legend
    for ax in (ax1, ax2, ax3):
        ax.legend()
        ax.set_xlabel('Sepal Length (cm)')
        ax.set_ylabel('Number')

    # Set the overall title for the figure
    fig.suptitle("Sepal Lengths\n", fontsize=14, fontweight='bold')

    # Show the plot
    plt.savefig('hist_sepal_length.png')

    return