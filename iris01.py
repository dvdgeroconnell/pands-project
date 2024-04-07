

# References (additional to README)
# - https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html#min-tut-03-subset

# ******************************************************************************************************

# Import Pandas for working with the raw dataset
import pandas as pd

# Import NumPy for working with data arrays 
import numpy as np

# Import pyplot from matplotlib and seaborn for visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Import the files that contain the required functions - stored separately for readibility
import write_summary as ws
import hist_all as ha
import petal_length as pl
import petal_width as pw
import sepal_length as sl
import sepal_width as sw

def do_menu():
    print("1 for a statistical summary of the iris dataset to be written to a file")
    print("2 for a set of histograms representing the full set of iris dataset variables")
    print("3 for a set of histograms representing the iris petal length variable")
    print("4 for a set of histograms representing the iris petal width variable")
    print("5 for a set of histograms representing the iris sepal length variable")
    print("6 for a set of histograms representing the iris sepal width variable")
    print ("7 to quit")

    # Check that the entered value is an integer
    # Range check will be handled by the main program
    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        choice = 0
    return choice

# Main program
# The iris dataset is available in a csv file at this link - we will use a local copy
# https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv

# Read the csv file into a Pandas dataframe. Ensure the iris.csv file is available
try:
    iris = pd.read_csv("iris.csv")
    print(iris.describe())

    # Create a dataframe with the 4 petal and sepal columns for each species
    setosa = iris.loc[iris['species']=="setosa", "sepal_length":"petal_width"]
    versicolor = iris.loc[iris['species']=="versicolor", "sepal_length":"petal_width"]
    virginica = iris.loc[iris['species']=="virginica", "sepal_length":"petal_width"]

    run = True
    while (run):
        choice = do_menu()
        match choice:
            case 1:
                print("Dataset summary written")
                # Write the overall summary for the dataset, and the summary for each species to a text file
                ws.petal_length_summary(iris, setosa, versicolor, virginica)
            case 2:
                # Draw the plots for all variables in one figure
                ha.plot_all(setosa, versicolor, virginica)
            case 3:
                # Draw the petal lengths histogram - function is contained in petal_length.py
                pl.plot_petal_length(setosa, versicolor, virginica)
            case 4:
                # Draw the petal widths histogram - function is contained in petal_width.py
                pw.plot_petal_width(setosa, versicolor, virginica)
            case 5:
                # Draw the sepal lengths histogram - function is contained in sepal_length.py
                sl.plot_sepal_length(setosa, versicolor, virginica)
            case 6:
                # Draw the sepal widths histogram - function is contained in sepal_width.py
                sw.plot_sepal_width(setosa, versicolor, virginica)
            case 7:
                # Exit the program
                print("Exiting...")
                run = False
            case _:
                # Catch-all for entries other than the ones listed above
                print("Invalid entry, exiting...")
                run = False


    #Get the NumPy array... no need for this
    #num_plen = plen.to_numpy()
    #plt.plot(num_plen)
    #plt.title("Lengths", fontweight='bold')
    #plt.xlabel('Petal Length (cm)')
    #plt.ylabel('Number')
    #plt.legend()

except FileNotFoundError:
    print("Error finding iris dataset file")

except pd.errors.EmptyDataError:
    print("Iris dataset file is empty")