# petal.py (PANDS project)
#
# Python functions to create histograms of the the petal length and petal width by species. They are then
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
HIST_PL = 'hist_petal_length.png'
HIST_PW = 'hist_petal_width.png'

# Define the function to draw the petal length histograms that will be called from the main program
def plot_petal_length(iris):

    # Extract the petal length
    setosa_plen = iris.loc[iris['species']=="setosa", 'petal_length']
    versicolor_plen = iris.loc[iris['species']=="versicolor", 'petal_length']
    virginica_plen = iris.loc[iris['species']=="virginica", 'petal_length']

    # Create a figure with 3 axes (subplots), one for each variety 
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
    plt.savefig(HIST_PL)
    print("Petal length histograms and kde plots written to", HIST_PL)
    return

# Define the function to draw the petal width histograms that will be called from the main program
def plot_petal_width(iris):

    # Extract the petal width
    setosa_pwth = iris.loc[iris['species']=="setosa", 'petal_width']
    versicolor_pwth = iris.loc[iris['species']=="versicolor", 'petal_width']
    virginica_pwth = iris.loc[iris['species']=="virginica", 'petal_width']

    # Create a figure with 3 axes (subplots), one for each variety 
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
    plt.savefig(HIST_PW)
    print("Petal width histograms and kde plots written to", HIST_PW)

    return