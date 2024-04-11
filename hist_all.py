# hist_all.py (PANDS project)
#
# A Python function to draw the histograms for the iris dataset variables by species. The histograms
# are drawn as a single figure, which is then saved to a file.
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
HIST_FILE = 'hist_all.png'

# Define the function that will be called from the main program
def plot_all(iris):

    # First, extract the petal length by species from the iris dataset
    setosa_plen = iris.loc[iris['species']=="setosa", 'petal_length']
    versicolor_plen = iris.loc[iris['species']=="versicolor", 'petal_length']
    virginica_plen = iris.loc[iris['species']=="virginica", 'petal_length']

    # Next, extract the petal width by species from the iris dataset
    setosa_pwth = iris.loc[iris['species']=="setosa", 'petal_width']
    versicolor_pwth = iris.loc[iris['species']=="versicolor", 'petal_width']
    virginica_pwth = iris.loc[iris['species']=="virginica", 'petal_width']

    # Then, extract the sepal length by species from the iris dataset
    setosa_slen = iris.loc[iris['species']=="setosa", 'sepal_length']
    versicolor_slen = iris.loc[iris['species']=="versicolor", 'sepal_length']
    virginica_slen = iris.loc[iris['species']=="virginica", 'sepal_length']

    # Finally, extract the sepal width by species from the iris dataset
    setosa_swth = iris.loc[iris['species']=="setosa", 'sepal_width']
    versicolor_swth = iris.loc[iris['species']=="versicolor", 'sepal_width']
    virginica_swth = iris.loc[iris['species']=="virginica", 'sepal_width']

    # Create a figure with 12 axes (subplots), one for each variable across each species
    # Use a common x-scale across columns and y-scale across rows for easier comparison
    fig, axes = plt.subplots(nrows=3, ncols=4, figsize=(12,9), sharex='col', sharey='row')

    # Histogram for setosa petal lengths
    ax1 = axes[0,0]
    ax1.hist(setosa_plen, label="setosa", color='red', edgecolor = 'black')

    # Histogram for versicolor petal lengths
    ax2 = axes[1,0]
    ax2.hist(versicolor_plen, label="versicolor", color='blue', edgecolor = 'black')

    # Histogram for virginica petal lengths
    ax3 = axes[2,0]
    ax3.hist(virginica_plen, label="virginica", color='green', edgecolor = 'black')

    # Set legend and labels for the first column
    ax1.set_title('Petal Lengths')

    for ax in axes[0:3,0]:
        ax.legend()
        ax.set_xlabel('Petal Length (cm)', fontsize=9)
        ax.set_ylabel('Number', fontsize=9)

    # Histogram for setosa petal widths
    ax1 = axes[0,1]
    ax1.hist(setosa_pwth, label="setosa", color='red', edgecolor = 'black')

    # Histogram for versicolor petal widths
    ax2 = axes[1,1]
    ax2.hist(versicolor_pwth, label="versicolor", color='blue', edgecolor = 'black')

    # Histogram for virginica petal widths
    ax3 = axes[2,1]
    ax3.hist(virginica_pwth, label="virginica", color='green', edgecolor = 'black')

    # Set legend and labels for the second column
    ax1.set_title('Petal Widths')

    for ax in axes[0:3,1]:
        ax.legend()
        ax.set_xlabel('Petal Width (cm)', fontsize=9)
        ax.set_ylabel('Number', fontsize=9)

    # Histogram for setosa sepal lengths
    ax1 = axes[0,2]
    ax1.hist(setosa_slen, label="setosa", color='red', edgecolor = 'black')

    # Histogram for versicolor sepal lengths
    ax2 = axes[1,2]
    ax2.hist(versicolor_slen, label="versicolor", color='blue', edgecolor = 'black')

    # Histogram for virginica sepal lengths
    ax3 = axes[2,2]
    ax3.hist(virginica_slen, label="virginica", color='green', edgecolor = 'black')

    # Set legend and labels for the third column
    ax1.set_title('Sepal Lengths')

    for ax in axes[0:3,2]:
        ax.legend()
        ax.set_xlabel('Sepal Length (cm)', fontsize=9)
        ax.set_ylabel('Number', fontsize=9)

    # Histogram for setosa sepal widths
    ax1 = axes[0,3]
    ax1.hist(setosa_swth, label="setosa", color='red', edgecolor = 'black')

    # Histogram for versicolor sepal widths
    ax2 = axes[1,3]
    ax2.hist(versicolor_swth, label="versicolor", color='blue', edgecolor = 'black')

    # Histogram for virginica sepal widths
    ax3 = axes[2,3]
    ax3.hist(virginica_swth, label="virginica", color='green', edgecolor = 'black')

    # Set legend and labels for the fourth column
    ax1.set_title('Sepal Widths')

    for ax in axes[0:3,3]:
        ax.legend()
        ax.set_xlabel('Sepal Width (cm)', fontsize=9)
        ax.set_ylabel('Number', fontsize=9)

    # Only add the labels around the outer axes in the figure for readability 
    for ax in fig.get_axes():
        ax.label_outer()

    # Set the overall title for the figure
    fig.suptitle("Iris dataset histograms\n", fontsize=12, fontweight='bold')

    try:
        # Save the plot
        plt.savefig(HIST_FILE)
        print("Histograms written to", HIST_FILE)
        x = input("Press 'Return' to continue")

    # Handle the error if the file could not be created / opened
    except OSError:
        print("Error - file could not be created")

    return