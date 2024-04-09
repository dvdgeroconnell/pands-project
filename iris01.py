

# References (additional to README)
# - https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html#min-tut-03-subset

# ******************************************************************************************************

# Import Pandas for working with the raw dataset. It implements dataframes for working with data and
# is built on top of NumPy. It addresses the restriction in NumPy whereby the array must be of only
# one data type. NumPy is not specifically required to be imported.
import pandas as pd

# Import pyplot from matplotlib and seaborn for visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Import the files that contain the required functions - stored separately for readibility
import write_summary as ws
import hist_all as ha
import scatter_all as sa
import petal_length as pl
import petal_width as pw
import sepal_length as sl
import sepal_width as sw

def do_menu():
    print("\nEnter one of the following:")
    print("1 for a statistical summary of the iris dataset to be written to a file")
    print("2 for statistical summaries of the individual iris variables to be written to 4 files")
    print("2 for a set of histograms representing the iris dataset variables written to a file")
    print("3 for histograms representing the individual iris variables written to 4 files")
    print("4 for a set of scatter plots representing the iris dataset variables")
    print("5 for the correlation of the iris dataset variables across the species")
    print("0 to quit")

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

    # Create a dataframe with the 4 petal and sepal columns for each species
    setosa = iris.loc[iris['species']=="setosa", "sepal_length":"petal_width"]
    versicolor = iris.loc[iris['species']=="versicolor", "sepal_length":"petal_width"]
    virginica = iris.loc[iris['species']=="virginica", "sepal_length":"petal_width"]

    run = True
    while (run):
        choice = do_menu()
        match choice:

            case 1:
                # Write the overall summary for the dataset, and the summary for each species to a text file
                ws.summary(iris, "all")

            case 2:
                # Draw the plots for all variables in one figure
                ha.plot_all(setosa, versicolor, virginica)

            case 3:
                # Draw the petal lengths histogram
                pl.plot_petal_length(setosa, versicolor, virginica)
                # Draw the petal widths histogram
                pw.plot_petal_width(setosa, versicolor, virginica)
                # Draw the sepal lengths histogram
                sl.plot_sepal_length(setosa, versicolor, virginica)
                # Draw the sepal widths histogram
                sw.plot_sepal_width(setosa, versicolor, virginica)

            case 4:
                # Draw the scatter plots - function is contained in scatter_all.py
                sa.scatter_all(setosa, versicolor, virginica)
                # Now using Seaborn - very simple by comparison! Density plots show the spread of values.
                sns.pairplot(iris,hue="species")
                plt.show()

            case 5:
                # Pandas correlation function here:
                # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html#pandas.DataFrame.corr
                print("\nAll")
                corr = iris[["petal_length", "petal_width", "sepal_length", "sepal_width"]].corr()
                print(corr)
                sns.heatmap(corr, annot=True, fmt=".2f")
                plt.show()
                print("\nSetosa")
                corr = setosa[["petal_length", "petal_width", "sepal_length", "sepal_width"]].corr()
                print(corr)

            case 0:
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