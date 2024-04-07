
import matplotlib.pyplot as plt

def plot_petal_length(setosa, versicolor, virginica):

    # Extract the petal length
    setosa_plen = setosa['petal_length']
    versicolor_plen = versicolor['petal_length']
    virginica_plen = virginica['petal_length']

    #plt.plot(setosa_plen, label="setosa", color='red')
    #plt.plot(versicolor_plen, label="versicolor", color='blue')
    #plt.plot(virginica_plen, label="virginica", color='green')

    # Create a figure with 3 Axes (subplots), one for each variety 
    fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(12,4))

    # Histogram for setosa
    ax1.hist(setosa_plen, label="setosa", color='red', edgecolor = 'black')
    ax1.legend()
    ax1.set_xlabel('Petal Length (cm)')
    ax1.set_ylabel('Number')
    #ax1.set_title('Petal Lengths')

    # Histogram for versicolor
    ax2.hist(versicolor_plen, label="versicolor", color='blue', edgecolor = 'black')
    ax2.legend()
    ax2.set_xlabel('Petal Length (cm)')
    ax2.set_ylabel('Number')
    #ax2.set_title('Petal Lengths')

    # Histogram for virginica
    ax3.hist(virginica_plen, label="virginica", color='green', edgecolor = 'black')
    ax3.legend()
    ax3.set_xlabel('Petal Length (cm)')
    ax3.set_ylabel('Number')
    #ax3.set_title('Petal Lengths')

    # Set the overall title for the figure
    fig.suptitle("Petal Lengths\n", fontsize=14, fontweight='bold')

    # Show the plot
    plt.show()

    return