

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

# The iris dataset is available in a csv file at this link - we will use a local copy
# https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv

# Read the csv file into a Pandas dataframe
iris = pd.read_csv("iris.csv")
print(iris.head())
#print(iris.describe())

# Create a dataframe for each species
setosa = iris.loc[iris['species']=="setosa", "sepal_length":"petal_width"]
versicolor = iris.loc[iris['species']=="versicolor", "sepal_length":"petal_width"]
virginica = iris.loc[iris['species']=="virginica", "sepal_length":"petal_width"]
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
ax1.hist(setosa_plen, label="setosa", color='red')
ax1.legend()
ax1.set_xlabel('Petal Length (cm)')
ax1.set_ylabel('Number')
#ax1.set_title('Petal Lengths')

# Histogram for versicolor
ax2.hist(versicolor_plen, label="versicolor", color='blue')
ax2.legend()
ax2.set_xlabel('Petal Length (cm)')
ax2.set_ylabel('Number')
#ax2.set_title('Petal Lengths')

# Histogram for virginica
ax3.hist(virginica_plen, label="virginica", color='green')
ax3.legend()
ax3.set_xlabel('Petal Length (cm)')
ax3.set_ylabel('Number')
#ax3.set_title('Petal Lengths')

# Set the overall title for the figure
fig.suptitle("Petal Lengths\n", fontsize=14, fontweight='bold')

# Show the plot
plt.show()


#Get the NumPy array... no need for this
#num_plen = plen.to_numpy()
#plt.plot(num_plen)
#plt.title("Lengths", fontweight='bold')
#plt.xlabel('Petal Length (cm)')
#plt.ylabel('Number')
#plt.legend()
