
import matplotlib.pyplot as plt

def plot_sepal_length(setosa, versicolor, virginica):

    # Extract the sepal length
    setosa_slen = setosa['sepal_length']
    versicolor_slen = versicolor['sepal_length']
    virginica_slen = virginica['sepal_length']

    # Create a figure with 3 Axes (subplots), one for each variety 
    fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(12,4))

    # Create histograms for setosa, versicolor and virginica
    ax1.hist(setosa_slen, label="setosa", color='red', edgecolor='black')
    ax2.hist(versicolor_slen, label="versicolor", color='blue', edgecolor='black')
    ax3.hist(virginica_slen, label="virginica", color='green', edgecolor='black')

    # Set the labels and legend (before drawing kde as it was overwriting the histogram)
    for ax in (ax1, ax2, ax3):
        ax.legend()
        ax.set_xlabel('Sepal Length (cm)')
        ax.set_ylabel('Number')

    # Create kde (kernel density estimation) plots, these will be superimposed on the histograms
    ax1 = setosa_slen.plot.kde(ax=ax1, color='b')
    ax2 = versicolor_slen.plot.kde(ax=ax2, color='g')
    ax3 = virginica_slen.plot.kde(ax=ax3,  color='r')

    # Set the overall title for the figure
    fig.suptitle("Sepal Lengths - Histograms and Density Plots\n", fontsize=14, fontweight='bold')

    # Show the plot
    plt.savefig('hist_sepal_length.png')

    return

def plot_sepal_width(setosa, versicolor, virginica):

    # Extract the sepal width
    setosa_swth = setosa['sepal_width']
    versicolor_swth = versicolor['sepal_width']
    virginica_swth = virginica['sepal_width']

    # Create a figure with 3 Axes (subplots), one for each variety 
    fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(12,4))

    # Create histograms for setosa, versicolor and virginica
    ax1.hist(setosa_swth, label="setosa", color='red', edgecolor='black')
    ax2.hist(versicolor_swth, label="versicolor", color='blue', edgecolor='black')
    ax3.hist(virginica_swth, label="virginica", color='green', edgecolor='black')

    # Set the labels and legend (before drawing kde as it was overwriting the histogram)
    for ax in (ax1, ax2, ax3):
        ax.legend()
        ax.set_xlabel('Sepal Width (cm)')
        ax.set_ylabel('Number')

    # Create kde (kernel density estimation) plots, these will be superimposed on the histograms
    ax1 = setosa_swth.plot.kde(ax=ax1, color='b')
    ax2 = versicolor_swth.plot.kde(ax=ax2, color='g')
    ax3 = virginica_swth.plot.kde(ax=ax3,  color='r')

    # Set the overall title for the figure
    fig.suptitle("Sepal Widths - Histograms and Density Plots\n", fontsize=14, fontweight='bold')

    # Show the plot
    plt.savefig('hist_sepal_width.png')

    return