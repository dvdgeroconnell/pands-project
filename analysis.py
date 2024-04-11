# analysis.py (PANDS project)
#
# A Python program to examine Fisher's iris dataset, a well known dataset with datapoints across 3 species
# of iris, widely used in Data Analytics and Machine Learning.
#
# Author: David O'Connell
#
# Reference(s)
#  - Iris dataset
#      - https://en.wikipedia.org/wiki/Iris_flower_data_set
#      - https://archive.ics.uci.edu/dataset/53/iris
#      - https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv (a local copy of this file
#        is used)
#
#  - Programming and Scripting lecture series
#  - Principles of Data Analytics lecture series, primarily week 08 (best fit & correlation)
#  - Matplotlib documentation - https://matplotlib.org/stable/users/index.html 
#  - Seaborn documentation / tutorials - https://seaborn.pydata.org/tutorial/function_overview.html
#  - Pandas - https://pandas.pydata.org/docs/user_guide/index.html
#
# The functionality is contained in functions which are imported below as separate files.
# This file contains the main program.
#
# ***************************************************************************************************

# Pandas implements dataframes for working with tabular data
import pandas as pd

# Import pyplot from matplotlib and seaborn for visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Import the files that contain the required functions - stored separately for readibility
import write_summary as ws
import hist_all as ha
import scatter_all as sa
import bestfit_all as bf
import write_correlation as wc
import menu
import petal
import sepal

# Create an alias for the file name rather than hardcoding below, makes it easier to move to a config file.
IRIS_FILE = "iris.csv"

# Read the locally stored csv file into a Pandas dataframe - confirm the file is available and readable
try:
    iris = pd.read_csv(IRIS_FILE)

    # Create a dataframe with the 4 petal and sepal columns for each species
    setosa = iris.loc[iris['species']=="setosa", "sepal_length":"petal_width"]
    versicolor = iris.loc[iris['species']=="versicolor", "sepal_length":"petal_width"]
    virginica = iris.loc[iris['species']=="virginica", "sepal_length":"petal_width"]

    run = True
    while (run):
        choice = menu.do_menu()
        match choice:

            case 1:
                # Write the overall summary for the dataset, and the summary for each species to a text file
                ws.summary(iris, "all")

            case 2:
                # Draw the plots for all variables in one figure
                ha.plot_all(setosa, versicolor, virginica)

            case 3:
                # Draw the petal lengths histogram
                petal.plot_petal_length(setosa, versicolor, virginica)
                # Draw the petal widths histogram
                petal.plot_petal_width(setosa, versicolor, virginica)
                # Draw the sepal lengths histogram
                sepal.plot_sepal_length(setosa, versicolor, virginica)
                # Draw the sepal widths histogram
                sepal.plot_sepal_width(setosa, versicolor, virginica)

            case 4:
                # Draw the scatter plots - function is contained in scatter_all.py
                sa.scatter_all(setosa, versicolor, virginica)
                # Now using Seaborn - very simple by comparison! Density plots show the spread of values.
                sns.pairplot(iris,hue="species")
                plt.show()

            case 5:
                # Pandas correlation function here:
                wc.iris_corr(iris, setosa, versicolor, virginica)

            case 6:
                # Experimental code for best fit here
                bf.bestfit_all(iris, setosa, versicolor, virginica)
                sns.pairplot(iris,hue="species", kind='reg')
                plt.show()

            case 0:
                # Exit the program
                print("Exiting...")
                run = False

            case _:
                # Catch-all for entries other than the ones listed above
                print("Invalid entry, exiting...")
                run = False

# Print an error message and exit gracefully if the iris.csv file is not in the same directory
except FileNotFoundError:
    print("Error finding iris dataset file")

# Print an error message and exit gracefully if the iris.csv file contains no data
except pd.errors.EmptyDataError:
    print("Iris dataset file is empty")