# Function to output a scatter plot of each pair of variables
# Experimental file for best fit

import numpy as np
import matplotlib.pyplot as plt

def bestfit_all(iris, setosa, versicolor, virginica):

    # Extract the 4 sets of data, starting with petal length
    setosa_plen = setosa['petal_length'].to_numpy()
    versicolor_plen = versicolor['petal_length'].to_numpy()
    virginica_plen = virginica['petal_length'].to_numpy()
    iris_plen = iris['petal_length'].to_numpy()

    # Next, petal width
    setosa_pwth = setosa['petal_width'].to_numpy()
    versicolor_pwth = versicolor['petal_width'].to_numpy()
    virginica_pwth = virginica['petal_width'].to_numpy()
    iris_pwth = iris['petal_width'].to_numpy()

    # Then, sepal length
    setosa_slen = setosa['sepal_length'].to_numpy()
    versicolor_slen = versicolor['sepal_length'].to_numpy()
    virginica_slen = virginica['sepal_length'].to_numpy()
    iris_slen = iris['sepal_length'].to_numpy()

    # Finally, sepal width
    setosa_swth = setosa['sepal_width'].to_numpy()
    versicolor_swth = versicolor['sepal_width'].to_numpy()
    virginica_swth = virginica['sepal_width'].to_numpy()
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
    # Calculate the best fit coefficients for a first order ploynomial (straight line)
    m1, c1 = np.polyfit(iris_plen, iris_pwth, 1)
    # Plot the best fit line, 'm-' instructs matplot to draw a line in purple
    ax1.plot(iris_plen, iris_plen*m1 + c1, 'm-')

    m1a, c1a = np.polyfit(setosa_plen, setosa_pwth, 1)
    m1b, c1b = np.polyfit(versicolor_plen, versicolor_pwth, 1)
    m1c, c1c = np.polyfit(virginica_plen, virginica_pwth, 1)

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

    m2a, c2a = np.polyfit(setosa_plen, setosa_slen, 1)
    m2b, c2b = np.polyfit(versicolor_plen, versicolor_slen, 1)
    m2c, c2c = np.polyfit(virginica_plen, virginica_slen, 1)

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

    m3a, c3a = np.polyfit(setosa_plen, setosa_swth, 1)
    m3b, c3b = np.polyfit(versicolor_plen, versicolor_swth, 1)
    m3c, c3c = np.polyfit(virginica_plen, virginica_swth, 1)

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

    m4a, c4a = np.polyfit(setosa_pwth, setosa_slen, 1)
    m4b, c4b = np.polyfit(versicolor_pwth, versicolor_slen, 1)
    m4c, c4c = np.polyfit(virginica_pwth, virginica_slen, 1)

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

    # Calculate the best fit coefficients for a first order ploynomial (straight line)
    m5, c5 = np.polyfit(iris_pwth, iris_swth, 1)
    # Plot the best fit line, 'm-' instructs matplot to draw a line in purple
    ax5.plot(iris_pwth, iris_pwth*m5 + c5, 'm-')

    m5a, c5a = np.polyfit(setosa_pwth, setosa_swth, 1)
    m5b, c5b = np.polyfit(versicolor_pwth, versicolor_swth, 1)
    m5c, c5c = np.polyfit(virginica_pwth, virginica_swth, 1)

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

    m6a, c6a = np.polyfit(setosa_slen, setosa_swth, 1)
    m6b, c6b = np.polyfit(versicolor_slen, versicolor_swth, 1)
    m6c, c6c = np.polyfit(virginica_slen, virginica_swth, 1)

    ax6.plot(setosa_slen, setosa_slen*m6a + c6a, 'k-')
    ax6.plot(versicolor_slen, versicolor_slen*m6b + c6b, 'k-')
    ax6.plot(virginica_slen, virginica_slen*m6c + c6c, 'k-')

    # Set the overall title for the figure
    fig.suptitle("Iris dataset scatter plots and best fit lines (setosa=red, versicolor=blue, "
                 "virginica=green)\n", fontsize=12, fontweight='bold')

    # Show the plot - fig.show() will draw and continue, plt.show() blocks
    plt.show()

    return