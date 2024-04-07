
import matplotlib.pyplot as plt

def plot_petal_width(setosa, versicolor, virginica):

    # Extract the petal width
    setosa_pwth = setosa['petal_width']
    versicolor_pwth = versicolor['petal_width']
    virginica_pwth = virginica['petal_width']

    #plt.plot(setosa_pwth, label="setosa", color='red')
    #plt.plot(versicolor_pwth, label="versicolor", color='blue')
    #plt.plot(virginica_pwth, label="virginica", color='green')

    # Create a figure with 3 Axes (subplots), one for each variety 
    fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(12,4))

    # Histogram for setosa
    ax1.hist(setosa_pwth, label="setosa", color='red', edgecolor = 'black')
    ax1.legend()
    ax1.set_xlabel('Petal Width (cm)')
    ax1.set_ylabel('Number')
    #ax1.set_title('Petal Widths')

    # Histogram for versicolor
    ax2.hist(versicolor_pwth, label="versicolor", color='blue', edgecolor = 'black')
    ax2.legend()
    ax2.set_xlabel('Petal Width (cm)')
    ax2.set_ylabel('Number')
    #ax2.set_title('Petal Widths')

    # Histogram for virginica
    ax3.hist(virginica_pwth, label="virginica", color='green', edgecolor = 'black')
    ax3.legend()
    ax3.set_xlabel('Petal Width (cm)')
    ax3.set_ylabel('Number')
    #ax3.set_title('Petal Widths')

    # Set the overall title for the figure
    fig.suptitle("Petal Widths\n", fontsize=14, fontweight='bold')

    # Show the plot
    plt.show()

    return