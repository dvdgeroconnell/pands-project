# Function to output a scatter plot of each pair of variables

import matplotlib.pyplot as plt

def scatter_all(setosa, versicolor, virginica):

    # Extract the 4 sets of data, starting with petal length
    setosa_plen = setosa['petal_length']
    versicolor_plen = versicolor['petal_length']
    virginica_plen = virginica['petal_length']

    # Next, petal width
    setosa_pwth = setosa['petal_width']
    versicolor_pwth = versicolor['petal_width']
    virginica_pwth = virginica['petal_width']

    # Then, sepal length
    setosa_slen = setosa['sepal_length']
    versicolor_slen = versicolor['sepal_length']
    virginica_slen = virginica['sepal_length']

    # Finally, sepal width
    setosa_swth = setosa['sepal_width']
    versicolor_swth = versicolor['sepal_width']
    virginica_swth = virginica['sepal_width']

    # Create a figure with 6 Axes (subplots), as the number of pairwise scatterplots for 4 variables
    # will be (4 x 3)/2 = 6 in total
    # fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(12,9), sharex=True, sharey=True)
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

    # Show the plot
    plt.show()

    return