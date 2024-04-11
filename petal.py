
import matplotlib.pyplot as plt

def plot_petal_length(setosa, versicolor, virginica):

    # Extract the petal length
    setosa_plen = setosa['petal_length']
    versicolor_plen = versicolor['petal_length']
    virginica_plen = virginica['petal_length']

    # Create a figure with 3 Axes (subplots), one for each variety 
    fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(12,4))

    # Create histograms for setosa, versicolor and virginica
    ax1.hist(setosa_plen, label="setosa", color='red', edgecolor='black')
    ax2.hist(versicolor_plen, label="versicolor", color='blue', edgecolor='black')
    ax3.hist(virginica_plen, label="virginica", color='green', edgecolor='black')

    # Set the labels and legend (before drawing kde as it was overwriting the histogram)
    for ax in (ax1, ax2, ax3):
        ax.legend()
        ax.set_xlabel('Petal Length (cm)')
        ax.set_ylabel('Number')

    # Create kde (kernel density estimation) plots, these will be superimposed on the histograms
    ax1 = setosa_plen.plot.kde(ax=ax1, color='b')
    ax2 = versicolor_plen.plot.kde(ax=ax2, color='g')
    ax3 = virginica_plen.plot.kde(ax=ax3,  color='r')

    # Set the overall title for the figure
    fig.suptitle("Petal Lengths - Histograms and Density Plots\n", fontsize=14, fontweight='bold')

    # Save the plot
    plt.savefig('hist_petal_length.png')

    return

def plot_petal_width(setosa, versicolor, virginica):

    # Extract the petal width
    setosa_pwth = setosa['petal_width']
    versicolor_pwth = versicolor['petal_width']
    virginica_pwth = virginica['petal_width']

    # Create a figure with 3 Axes (subplots), one for each variety 
    fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(12,4))

    # Create histograms for setosa, versicolor and virginica
    ax1.hist(setosa_pwth, label="setosa", color='red', edgecolor='black')
    ax2.hist(versicolor_pwth, label="versicolor", color='blue', edgecolor='black')
    ax3.hist(virginica_pwth, label="virginica", color='green', edgecolor='black')

    # Set the labels and legend (before drawing kde as it was overwriting the histogram)
    for ax in (ax1, ax2, ax3):
        ax.legend()
        ax.set_xlabel('Petal Width (cm)')
        ax.set_ylabel('Number')

    # Create kde (kernel density estimation) plots, these will be superimposed on the histograms
    ax1 = setosa_pwth.plot.kde(ax=ax1, color='b')
    ax2 = versicolor_pwth.plot.kde(ax=ax2, color='g')
    ax3 = virginica_pwth.plot.kde(ax=ax3,  color='r')

    # Set the overall title for the figure
    fig.suptitle("Petal Widths - Histograms and Density Plots\n", fontsize=14, fontweight='bold')

    # Save the plot
    plt.savefig('hist_petal_width.png')

    return