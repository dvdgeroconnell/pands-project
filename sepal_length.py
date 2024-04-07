
import matplotlib.pyplot as plt

def plot_sepal_length(setosa, versicolor, virginica):

    # Extract the sepal length
    setosa_slen = setosa['sepal_length']
    versicolor_slen = versicolor['sepal_length']
    virginica_slen = virginica['sepal_length']

    #plt.plot(setosa_slen, label="setosa", color='red')
    #plt.plot(versicolor_slen, label="versicolor", color='blue')
    #plt.plot(virginica_slen, label="virginica", color='green')

    # Create a figure with 3 Axes (subplots), one for each variety 
    fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(12,4))

    # Histogram for setosa
    ax1.hist(setosa_slen, label="setosa", color='red', edgecolor = 'black')
    ax1.legend()
    ax1.set_xlabel('Sepal Length (cm)')
    ax1.set_ylabel('Number')
    #ax1.set_title('Sepal Lengths')

    # Histogram for versicolor
    ax2.hist(versicolor_slen, label="versicolor", color='blue', edgecolor = 'black')
    ax2.legend()
    ax2.set_xlabel('Sepal Length (cm)')
    ax2.set_ylabel('Number')
    #ax2.set_title('Sepal Lengths')

    # Histogram for virginica
    ax3.hist(virginica_slen, label="virginica", color='green', edgecolor = 'black')
    ax3.legend()
    ax3.set_xlabel('Sepal Length (cm)')
    ax3.set_ylabel('Number')
    #ax3.set_title('Sepal Lengths')

    # Set the overall title for the figure
    fig.suptitle("Sepal Lengths\n", fontsize=14, fontweight='bold')

    # Show the plot
    plt.show()

    return