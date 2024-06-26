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

# Import the files that contain the required functions - stored separately for readibility
import write_summary as ws
import hist_all as ha
import scatter_all as sa
import bestfit_all as bf
import write_correlation as wc
import menu, petal, sepal

# Create an alias for the file name rather than hardcoding below, makes it easier to move to a config file.
IRIS_FILE = "iris.csv"

# Read the locally stored csv file into a Pandas dataframe - confirm the file is available and readable
try:
    iris = pd.read_csv(IRIS_FILE)

    # Display the menu - use a while loop to keep the program running until exit or invalid entry
    run = True
    while (run):
        choice = menu.do_menu()
        match choice:

            case 0:
                # Exit the program
                print("Exiting...")
                run = False

            case 1:
                # Write the overall summary for the dataset, and the summary for each species to a text file
                ws.summary(iris, "all")

            case 2:
                # Draw the plots for all variables in one figure
                ha.plot_all(iris)

            case 3:
                # Draw the petal lengths histogram
                petal.plot_petal_length(iris)
                # Draw the petal widths histogram
                petal.plot_petal_width(iris)
                # Draw the sepal lengths histogram
                sepal.plot_sepal_length(iris)
                # Draw the sepal widths histogram
                sepal.plot_sepal_width(iris)
                x = input("Press 'Return' to continue")

            case 4:
                # Draw the scatter plots - function is contained in scatter_all.py
                # Generate plots with both Matplotlib and Seaborn for comparison
                sa.scatter_all(iris)

            case 5:
                # Pandas correlation function here:
                wc.iris_corr(iris)

            case 6:
                # Experimental code for best fit here
                bf.bestfit_all(iris)

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