# scatter_all.py (PANDS project)
#
# A Python function to draw the pairwise scatter plots for the Iris dataset variables colour-coded by
# species. The scatter plots are drawn as a single figure, which is then saved to a file.
# Scatter plots are drawn using both Matplotlib and Seaborn for comparison.
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
import seaborn as sns

# Define file names where the scatter plots will be saved - can be easily moved to a config file 
SCATTER_PLT = 'scatter_plt.png'
SCATTER_SNS = 'scatter_sns.png'

# Define the function that will be called from the main program
def scatter_all(iris):

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

    # Create a figure with 6 axes (subplots), as the number of pairwise scatterplots for 4 variables
    # will be (4 x 3)/2 = 6 in total
    fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(12,9), sharex='col')

    # Scatter plot for petal length vs petal width
    ax1 = axes[0,0]
    ax1.scatter(setosa_plen, setosa_pwth, label="setosa", color='red', edgecolor='black')
    ax1.scatter(versicolor_plen, versicolor_pwth, label="versicolor", color='blue', edgecolor='black')
    ax1.scatter(virginica_plen, virginica_pwth, label="virginica", color='green', edgecolor='black')
    ax1.set_title('Petal Length vs Petal Width', fontsize=9)
    ax1.set_xlabel('Petal Length (cm)', fontsize=9)
    ax1.set_ylabel('Petal Width (cm)', fontsize=9)

    # Scatter plot for petal length vs sepal length
    ax2 = axes[1,0]
    ax2.scatter(setosa_plen, setosa_slen, label="setosa", color='red', edgecolor='black')
    ax2.scatter(versicolor_plen, versicolor_slen, label="versicolor", color='blue', edgecolor='black')
    ax2.scatter(virginica_plen, virginica_slen, label="virginica", color='green', edgecolor='black')
    ax2.set_title('Petal Length vs Sepal Length', fontsize=9)
    ax2.set_xlabel('Petal Length (cm)', fontsize=9)
    ax2.set_ylabel('Sepal Length (cm)', fontsize=9)

    # Scatter plot for petal length vs sepal width
    ax1 = axes[0,2]
    ax1.scatter(setosa_plen, setosa_swth, label="setosa", color='red', edgecolor='black')
    ax1.scatter(versicolor_plen, versicolor_swth, label="versicolor", color='blue', edgecolor='black')
    ax1.scatter(virginica_plen, virginica_swth, label="virginica", color='green', edgecolor='black')
    ax1.set_title('Petal Length vs Sepal Width', fontsize=9)
    ax1.set_xlabel('Petal Length (cm)', fontsize=9)
    ax1.set_ylabel('Sepal Width (cm)', fontsize=9)

    # Scatter plot for petal width vs sepal length
    ax1 = axes[0,1]
    ax1.scatter(setosa_pwth, setosa_slen, label="setosa", color='red', edgecolor='black')
    ax1.scatter(versicolor_pwth, versicolor_slen, label="versicolor", color='blue', edgecolor='black')
    ax1.scatter(virginica_pwth, virginica_slen, label="virginica", color='green', edgecolor='black')
    ax1.set_title('Petal Width vs Sepal Length', fontsize=9)
    ax1.set_xlabel('Petal Width (cm)', fontsize=9)
    ax1.set_ylabel('Sepal Length (cm)', fontsize=9)

    # Scatter plot for petal width vs sepal width
    ax1 = axes[1,1]
    ax1.scatter(setosa_pwth, setosa_swth, label="setosa", color='red', edgecolor='black')
    ax1.scatter(versicolor_pwth, versicolor_swth, label="versicolor", color='blue', edgecolor='black')
    ax1.scatter(virginica_pwth, virginica_swth, label="virginica", color='green', edgecolor='black')
    ax1.set_title('Petal Width vs Sepal Width', fontsize=9)
    ax1.set_xlabel('Petal Width (cm)', fontsize=9)
    ax1.set_ylabel('Sepal Width (cm)', fontsize=9)

    # Scatter plot for sepal length vs sepal width
    ax1 = axes[1,2]
    ax1.scatter(setosa_slen, setosa_swth, label="setosa", color='red', edgecolor='black')
    ax1.scatter(versicolor_slen, versicolor_swth, label="versicolor", color='blue', edgecolor='black')
    ax1.scatter(virginica_slen, virginica_swth, label="virginica", color='green', edgecolor='black')
    ax1.set_title('Sepal Length vs Sepal Width', fontsize=9)
    ax1.set_xlabel('Sepal Length (cm)', fontsize=9)
    ax1.set_ylabel('Sepal Width (cm)', fontsize=9)

    # Set the overall title for the figure
    fig.suptitle("Iris dataset (setosa=red, versicolor=blue, virginica=green)\n",
                 fontsize=12, fontweight='bold')

    # Show the plot - fig.show() will draw and continue, plt.show() blocks
    # plt.show()

    # Updated to save to file
    plt.savefig(SCATTER_PLT)

    # Now using Seaborn - one line versus the code above
    # Density plots on the diagonal show the spread of values
    # Just draw the 6 individual plots (corner=True), do not repeat them above the diagonal
    sns.pairplot(iris,hue="species", corner=True)
    plt.savefig(SCATTER_SNS)

    print("Scatter plots written to", SCATTER_PLT, "(Pyplot) and", SCATTER_SNS, "(Seaborn)")
    x = input("Press 'Return' to continue")

    return