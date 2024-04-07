# Function to output a scatter plot of each pair of variables

import matplotlib.pyplot as plt

def plot_all(setosa, versicolor, virginica):

    # Extract the 4 sets of data - first, petal length
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

    # Create a figure with 3 Axes (subplots), one for each variety 
    fig, axes = plt.subplots(nrows=3, ncols=4, figsize=(12,9), sharex=True, sharey=True)

    #Plot petal lengths as the first column

    # Histogram for setosa
    ax1 = axes[0,0]
    ax1.hist(setosa_plen, label="setosa", color='red', edgecolor = 'black')
    ax1.set_title('Petal Lengths')

    # Histogram for versicolor
    ax2 = axes[1,0]
    ax2.hist(versicolor_plen, label="versicolor", color='blue', edgecolor = 'black')

    # Histogram for virginica
    ax3 = axes[2,0]
    ax3.hist(virginica_plen, label="virginica", color='green', edgecolor = 'black')

    # Set legend and labels for the first column
    for ax in axes[0:3,0]:
        ax.legend()
        ax.set_xlabel('Petal Length (cm)', fontsize=9)
        ax.set_ylabel('Number', fontsize=9)

    #Plot petal widths as the second column

    # Histogram for setosa
    ax1 = axes[0,1]
    ax1.hist(setosa_pwth, label="setosa", color='red', edgecolor = 'black')
    ax1.set_title('Petal Widths')

    # Histogram for versicolor
    ax2 = axes[1,1]
    ax2.hist(versicolor_pwth, label="versicolor", color='blue', edgecolor = 'black')

    # Histogram for virginica
    ax3 = axes[2,1]
    ax3.hist(virginica_pwth, label="virginica", color='green', edgecolor = 'black')

    # Set legend and labels for the second column
    for ax in axes[0:3,1]:
        ax.legend()
        ax.set_xlabel('Petal Width (cm)', fontsize=9)
        ax.set_ylabel('Number', fontsize=9)

    #Plot sepal lengths as the third column

    # Histogram for setosa
    ax1 = axes[0,2]
    ax1.hist(setosa_slen, label="setosa", color='red', edgecolor = 'black')
    ax1.set_title('Sepal Lengths')

    # Histogram for versicolor
    ax2 = axes[1,2]
    ax2.hist(versicolor_slen, label="versicolor", color='blue', edgecolor = 'black')

    # Histogram for virginica
    ax3 = axes[2,2]
    ax3.hist(virginica_slen, label="virginica", color='green', edgecolor = 'black')

    # Set legend and labels for the third column
    for ax in axes[0:3,2]:
        ax.legend()
        ax.set_xlabel('Sepal Length (cm)', fontsize=9)
        ax.set_ylabel('Number', fontsize=9)

    #Plot sepal widths as the fourth column

    # Histogram for setosa
    ax1 = axes[0,3]
    ax1.hist(setosa_swth, label="setosa", color='red', edgecolor = 'black')
    ax1.set_title('Sepal Widths')

    # Histogram for versicolor
    ax2 = axes[1,3]
    ax2.hist(versicolor_swth, label="versicolor", color='blue', edgecolor = 'black')

    # Histogram for virginica
    ax3 = axes[2,3]
    ax3.hist(virginica_swth, label="virginica", color='green', edgecolor = 'black')

    # Set legend and labels for the fourth column
    for ax in axes[0:3,3]:
        ax.legend()
        ax.set_xlabel('Sepal Width (cm)', fontsize=9)
        ax.set_ylabel('Number', fontsize=9)

    # Only add the labels around the outer axes in the figure for readibility 
    for ax in fig.get_axes():
        ax.label_outer()

    # Set the overall title for the figure
    fig.suptitle("Iris dataset\n", fontsize=12, fontweight='bold')

    # Show the plot
    plt.show()

    return