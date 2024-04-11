# sepal.py (PANDS project)
#
# Python functions to create histograms of the the sepal length and sepal width by species. They are then
# written to a file.
#
# Author: David O'Connell
#
# Reference(s)
#  - Programming and Scripting lecture series - week 07, 08 (files, plotting)
#  - Principles of Data Analytics lecture series - week 08 (iris dataset)
#  - Matplotlib documentation - https://matplotlib.org/stable/users/index.html 
#  - Pandas methods - https://pandas.pydata.org/docs/reference/index.html
#
# ***************************************************************************************************

# Import the required libraries for visualization
import matplotlib.pyplot as plt

# Define file name where the histograms will be saved - can be easily moved to a config file 
HIST_SL = 'hist_sepal_length.png'
HIST_SW = 'hist_sepal_width.png'

# Define the function to draw the sepal length histograms that will be called from the main program
def plot_sepal_length(iris):

    # Extract the sepal length
    setosa_slen = iris.loc[iris['species']=="setosa", 'sepal_length']
    versicolor_slen = iris.loc[iris['species']=="versicolor", 'sepal_length']
    virginica_slen = iris.loc[iris['species']=="virginica", 'sepal_length']

    # Create a figure with 3 axes (subplots), one for each variety 
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
    plt.savefig(HIST_SL)
    print("Sepal length histograms and kde plots written to", HIST_SL)

    return

# Define the function to draw the sepal width histograms that will be called from the main program
def plot_sepal_width(iris):

    # Extract the sepal width
    setosa_swth = iris.loc[iris['species']=="setosa", 'sepal_width']
    versicolor_swth = iris.loc[iris['species']=="versicolor", 'sepal_width']
    virginica_swth = iris.loc[iris['species']=="virginica", 'sepal_width']

    # Create a figure with 3 axes (subplots), one for each variety 
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
    plt.savefig(HIST_SW)
    print("Sepal width histograms and kde plots written to", HIST_SW)

    return