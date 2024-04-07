
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
    fig, axes = plt.subplots(nrows=3, ncols=4, figsize=(12,9))

    # Histogram for setosa
    ax1 = axes[0,0]
    ax1.hist(setosa_plen, label="setosa", color='red', edgecolor = 'black')
    ax1.legend()
    ax1.set_xlabel('Petal Length (cm)', fontsize=9)
    ax1.set_ylabel('Number', fontsize=9)
    #ax1.set_title('Petal Lengths')

    # Histogram for versicolor
    ax2 = axes[1,0]
    ax2.hist(versicolor_plen, label="versicolor", color='blue', edgecolor = 'black')
    ax2.legend()
    ax2.set_xlabel('Petal Length (cm)', fontsize=9)
    ax2.set_ylabel('Number', fontsize=9)
    #ax2.set_title('Petal Lengths')

    # Histogram for virginica
    ax3 = axes[2,0]
    ax3.hist(virginica_plen, label="virginica", color='green', edgecolor = 'black')
    ax3.legend()
    ax3.set_xlabel('Petal Length (cm)', fontsize=9)
    ax3.set_ylabel('Number', fontsize=9)
    #ax3.set_title('Petal Lengths')

    for axes in fig.get_axes():
        axes.label_outer()
        axes.set_ylabel('Number', fontsize=9)

    # Set the overall title for the figure
    fig.suptitle("Petal Lengths\n", fontsize=12, fontweight='bold')

    # Show the plot
    plt.show()

    return