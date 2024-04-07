

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

# Main program
# The iris dataset is available in a csv file at this link - we will use a local copy
# https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv

# Read the csv file into a Pandas dataframe. Ensure the iris.csv file is available
try:
    iris = pd.read_csv("iris.csv")
    #print(iris.head())
    print(iris.describe())

    # Create a dataframe with the 4 petal and sepal columns for each species
    setosa = iris.loc[iris['species']=="setosa", "sepal_length":"petal_width"]
    versicolor = iris.loc[iris['species']=="versicolor", "sepal_length":"petal_width"]
    virginica = iris.loc[iris['species']=="virginica", "sepal_length":"petal_width"]

    # Write the overall summary for the dataset, and the summary for each species to a text file
    ws.petal_length_summary(iris, setosa, versicolor, virginica)

    # Draw the plots for all variables in one figure
    ha.plot_all(setosa, versicolor, virginica)

    # Draw the petal lengths histogram - function is contained in petal_length.py
    pl.plot_petal_length(setosa, versicolor, virginica)

    # Draw the petal widths histogram - function is contained in petal_width.py
    pw.plot_petal_width(setosa, versicolor, virginica)

    # Draw the sepal lengths histogram - function is contained in sepal_length.py
    sl.plot_sepal_length(setosa, versicolor, virginica)

    # Draw the sepal widths histogram - function is contained in sepal_width.py
    sw.plot_sepal_width(setosa, versicolor, virginica)

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
