# bestfit_all.py (PANDS project)
#
# A Python function to draw the pairwise scatter plots for the Iris dataset variables colour-coded by
# species. Best fit lines are then calculated using NumPy's ployfit method and superimposed on the 
# scatter plots. The plots are drawn as a single figure, which is then saved to a file.
# Seaborn is then used to create similar scatter plots with best fit lines by species for comparison.
#
# Author: David O'Connell
#
# Reference(s)
#  - Programming and Scripting lecture series - week 07, 08 (files, plotting)
#  - Principles of Data Analytics lecture series - week 08 (iris dataset, best fit)
#  - Matplotlib documentation - https://matplotlib.org/stable/users/index.html
#  - Pandas methods - https://pandas.pydata.org/docs/reference/index.html
#  - Seaborn documentation / tutorials - https://seaborn.pydata.org/tutorial/function_overview.html
#  - NumPy polyfit - https://numpy.org/doc/1.26/reference/generated/numpy.polyfit.html#numpy.polyfit
#  - https://stackoverflow.com/questions/31568874/how-to-change-the-line-color-in-seaborn-linear-regression-jointplot
#  - https://stackoverflow.com/questions/74971910/how-to-remove-confidance-interval-in-pairplot
#
# ***************************************************************************************************

# Import the required libraries for visualization
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Files where the scatter plots with best fit lines will be saved - can be easily moved to a config file 
BESTFIT_PLT = 'bestfit_plt.png'
BESTFIT_SNS = 'bestfit_sns.png'

# Define the function that will be called from the main program
def bestfit_all(iris):

    # Extract the petal lengths as NumPy arrays (for polyfit)
    setosa_plen = iris.loc[iris['species']=="setosa", 'petal_length'].to_numpy()
    versicolor_plen = iris.loc[iris['species']=="versicolor", 'petal_length'].to_numpy()
    virginica_plen = iris.loc[iris['species']=="virginica", 'petal_length'].to_numpy()
    iris_plen = iris['petal_length'].to_numpy()

    # Extract the petal widths as NumPy arrays (for polyfit)
    setosa_pwth = iris.loc[iris['species']=="setosa", 'petal_width'].to_numpy()
    versicolor_pwth = iris.loc[iris['species']=="versicolor", 'petal_width'].to_numpy()
    virginica_pwth = iris.loc[iris['species']=="virginica", 'petal_width'].to_numpy()
    iris_pwth = iris['petal_width'].to_numpy()

    # Extract the sepal lengths as NumPy arrays (for polyfit)
    setosa_slen = iris.loc[iris['species']=="setosa", 'sepal_length'].to_numpy()
    versicolor_slen = iris.loc[iris['species']=="versicolor", 'sepal_length'].to_numpy()
    virginica_slen = iris.loc[iris['species']=="virginica", 'sepal_length'].to_numpy()
    iris_slen = iris['sepal_length'].to_numpy()

    # Extract the sepal widths as NumPy arrays (for polyfit)
    setosa_swth = iris.loc[iris['species']=="setosa", 'sepal_width'].to_numpy()
    versicolor_swth = iris.loc[iris['species']=="versicolor", 'sepal_width'].to_numpy()
    virginica_swth = iris.loc[iris['species']=="virginica", 'sepal_width'].to_numpy()
    iris_swth = iris['sepal_width'].to_numpy()

    # Create a figure with 6 Axes (subplots), as the number of pairwise scatterplots for 4 variables
    # will be (4 x 3)/2 = 6 in total
    fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(12,9), sharex='col')

    # Create the scatter plots for petal length vs petal width by species
    ax1 = axes[0,0]
    ax1.scatter(setosa_plen, setosa_pwth, label="setosa", color='red', edgecolor='black')
    ax1.scatter(versicolor_plen, versicolor_pwth, label="versicolor", color='blue', edgecolor='black')
    ax1.scatter(virginica_plen, virginica_pwth, label="virginica", color='green', edgecolor='black')
    ax1.set_title('Petal Length vs Petal Width\nwith best fit lines per dataset and per species', fontsize=9)
    ax1.set_xlabel('Petal Length (cm)', fontsize=9)
    ax1.set_ylabel('Petal Width (cm)', fontsize=9)
    # Calculate the best fit coefficients for a first order ploynomial (straight line) for the iris dataset
    m1, c1 = np.polyfit(iris_plen, iris_pwth, 1)
    # Plot the best fit line, 'm-' instructs matplot to draw a line in purple
    ax1.plot(iris_plen, iris_plen*m1 + c1, 'm-')

    # Now calculate the best fit coefficients for a first order ploynomial (straight line) by species
    m1a, c1a = np.polyfit(setosa_plen, setosa_pwth, 1)
    m1b, c1b = np.polyfit(versicolor_plen, versicolor_pwth, 1)
    m1c, c1c = np.polyfit(virginica_plen, virginica_pwth, 1)

    # Plot the best fit lines, 'k-' instructs matplot to draw a line in black
    ax1.plot(setosa_plen, setosa_plen*m1a + c1a, 'k-')
    ax1.plot(versicolor_plen, versicolor_plen*m1b + c1b, 'k-')
    ax1.plot(virginica_plen, virginica_plen*m1c + c1c, 'k-')

    # Create the scatter plot for petal length vs sepal length by species
    ax2 = axes[1,0]
    ax2.scatter(setosa_plen, setosa_slen, label="setosa", color='red', edgecolor='black')
    ax2.scatter(versicolor_plen, versicolor_slen, label="versicolor", color='blue', edgecolor='black')
    ax2.scatter(virginica_plen, virginica_slen, label="virginica", color='green', edgecolor='black')
    ax2.set_title('Petal Length vs Sepal Length\nwith best fit line per species', fontsize=9)
    ax2.set_xlabel('Petal Length (cm)', fontsize=9)
    ax2.set_ylabel('Sepal Length (cm)', fontsize=9)

    # Calculate the best fit coefficients for a first order ploynomial (straight line) by species
    m2a, c2a = np.polyfit(setosa_plen, setosa_slen, 1)
    m2b, c2b = np.polyfit(versicolor_plen, versicolor_slen, 1)
    m2c, c2c = np.polyfit(virginica_plen, virginica_slen, 1)

    # Plot the best fit lines, 'k-' instructs matplot to draw a line in black
    ax2.plot(setosa_plen, setosa_plen*m2a + c2a, 'k-')
    ax2.plot(versicolor_plen, versicolor_plen*m2b + c2b, 'k-')
    ax2.plot(virginica_plen, virginica_plen*m2c + c2c, 'k-')

    # Scatter plot for petal length vs sepal width
    ax3 = axes[0,2]
    ax3.scatter(setosa_plen, setosa_swth, label="setosa", color='red', edgecolor='black')
    ax3.scatter(versicolor_plen, versicolor_swth, label="versicolor", color='blue', edgecolor='black')
    ax3.scatter(virginica_plen, virginica_swth, label="virginica", color='green', edgecolor='black')
    ax3.set_title('Petal Length vs Sepal Width\nwith best fit line per species', fontsize=9)
    ax3.set_xlabel('Petal Length (cm)', fontsize=9)
    ax3.set_ylabel('Sepal Width (cm)', fontsize=9)

    # Calculate the best fit coefficients for a first order ploynomial (straight line) by species
    m3a, c3a = np.polyfit(setosa_plen, setosa_swth, 1)
    m3b, c3b = np.polyfit(versicolor_plen, versicolor_swth, 1)
    m3c, c3c = np.polyfit(virginica_plen, virginica_swth, 1)

    # Plot the best fit lines, 'k-' instructs matplot to draw a line in black
    ax3.plot(setosa_plen, setosa_plen*m3a + c3a, 'k-')
    ax3.plot(versicolor_plen, versicolor_plen*m3b + c3b, 'k-')
    ax3.plot(virginica_plen, virginica_plen*m3c + c3c, 'k-')

    # Scatter plot for petal width vs sepal length
    ax4 = axes[0,1]
    ax4.scatter(setosa_pwth, setosa_slen, label="setosa", color='red', edgecolor='black')
    ax4.scatter(versicolor_pwth, versicolor_slen, label="versicolor", color='blue', edgecolor='black')
    ax4.scatter(virginica_pwth, virginica_slen, label="virginica", color='green', edgecolor='black')
    ax4.set_title('Petal Width vs Sepal Length\nwith best fit line per species', fontsize=9)
    ax4.set_xlabel('Petal Width (cm)', fontsize=9)
    ax4.set_ylabel('Sepal Length (cm)', fontsize=9)

    # Calculate the best fit coefficients for a first order ploynomial (straight line) by species
    m4a, c4a = np.polyfit(setosa_pwth, setosa_slen, 1)
    m4b, c4b = np.polyfit(versicolor_pwth, versicolor_slen, 1)
    m4c, c4c = np.polyfit(virginica_pwth, virginica_slen, 1)

    # Plot the best fit lines, 'k-' instructs matplot to draw a line in black
    ax4.plot(setosa_pwth, setosa_pwth*m4a + c4a, 'k-')
    ax4.plot(versicolor_pwth, versicolor_pwth*m4b + c4b, 'k-')
    ax4.plot(virginica_pwth, virginica_pwth*m4c + c4c, 'k-')

    # Scatter plot for petal width vs sepal width
    ax5 = axes[1,1]
    ax5.scatter(setosa_pwth, setosa_swth, label="setosa", color='red', edgecolor='black')
    ax5.scatter(versicolor_pwth, versicolor_swth, label="versicolor", color='blue', edgecolor='black')
    ax5.scatter(virginica_pwth, virginica_swth, label="virginica", color='green', edgecolor='black')
    ax5.set_title('Petal Width vs Sepal Width\nwith best fit lines per dataset and per species', fontsize=9)
    ax5.set_xlabel('Petal Width (cm)', fontsize=9)
    ax5.set_ylabel('Sepal Width (cm)', fontsize=9)

    # Calculate the best fit coefficients for a first order ploynomial (straight line) for the iris dataset
    m5, c5 = np.polyfit(iris_pwth, iris_swth, 1)
    # Plot the best fit line, 'm-' instructs matplot to draw a line in purple
    ax5.plot(iris_pwth, iris_pwth*m5 + c5, 'm-')

    # Calculate the best fit coefficients for a first order ploynomial (straight line) by species
    m5a, c5a = np.polyfit(setosa_pwth, setosa_swth, 1)
    m5b, c5b = np.polyfit(versicolor_pwth, versicolor_swth, 1)
    m5c, c5c = np.polyfit(virginica_pwth, virginica_swth, 1)

    # Plot the best fit lines, 'k-' instructs matplot to draw a line in black
    ax5.plot(setosa_pwth, setosa_pwth*m5a + c5a, 'k-')
    ax5.plot(versicolor_pwth, versicolor_pwth*m5b + c5b, 'k-')
    ax5.plot(virginica_pwth, virginica_pwth*m5c + c5c, 'k-')

    # Scatter plot for sepal length vs sepal width
    ax6 = axes[1,2]
    ax6.scatter(setosa_slen, setosa_swth, label="setosa", color='red', edgecolor='black')
    ax6.scatter(versicolor_slen, versicolor_swth, label="versicolor", color='blue', edgecolor='black')
    ax6.scatter(virginica_slen, virginica_swth, label="virginica", color='green', edgecolor='black')
    ax6.set_title('Sepal Length vs Sepal Width\nwith best fit line per species', fontsize=9)
    ax6.set_xlabel('Sepal Length (cm)', fontsize=9)
    ax6.set_ylabel('Sepal Width (cm)', fontsize=9)

    # Calculate the best fit coefficients for a first order ploynomial (straight line) by species
    m6a, c6a = np.polyfit(setosa_slen, setosa_swth, 1)
    m6b, c6b = np.polyfit(versicolor_slen, versicolor_swth, 1)
    m6c, c6c = np.polyfit(virginica_slen, virginica_swth, 1)

    # Plot the best fit lines, 'k-' instructs matplot to draw a line in black
    ax6.plot(setosa_slen, setosa_slen*m6a + c6a, 'k-')
    ax6.plot(versicolor_slen, versicolor_slen*m6b + c6b, 'k-')
    ax6.plot(virginica_slen, virginica_slen*m6c + c6c, 'k-')

    # Set the overall title for the figure
    fig.suptitle("Iris dataset scatter plots and best fit lines (setosa=red, versicolor=blue, "
                 "virginica=green)\n", fontsize=12, fontweight='bold')

    # Show the plot - fig.show() will draw and continue, plt.show() blocks
    plt.savefig(BESTFIT_PLT)

    # Now draw a scatter plot for the dataset with Seaborn - it is one line versus all of the code above
    # Setting kind='reg' adds the liner regression plots 
    # Density plots on the diagonal show the spread of values
    # Draw all 12 individual plots (corner=False), so we can compare them to the Matplotlib plots
    sns.pairplot(iris, hue="species", kind='reg', corner=False, plot_kws={'line_kws':{'color':'black'},'ci':None})
    plt.savefig(BESTFIT_SNS)

    print("Scatter plots with best fit lines written to", BESTFIT_PLT, "(Pyplot) and", BESTFIT_SNS, "(Seaborn)")
    x = input("Press 'Return' to continue")

    return