# write_correlation.py (PANDS project)
#
# A Python function to calculate the correlation coefficients and draw the heatmaps for the Iris
# dataset, both overall and by species.
#
# Author: David O'Connell
#
# Reference(s)
#  - Programming and Scripting lecture series - week 08 (plotting)
#  - Principles of Data Analytics lecture series - week 08 (best fit & correlation)
#  - Seaborn documentation / tutorials - https://seaborn.pydata.org/tutorial/function_overview.html
#  - Pandas - https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html#pandas.DataFrame.corr
#
# ***************************************************************************************************

# Import the required libraries for visualization
import matplotlib.pyplot as plt 
import seaborn as sns

# Define file names where correlation data and heatmaps will be saved - can easily move to config file 
CORRELATION_IRIS = "iris_correlation.txt"
HEATMAP_IRIS = "corr_iris.png"

# Define the function that will be called from the main program
def iris_corr(iris):

    setosa = iris.loc[iris['species']=="setosa", "sepal_length":"petal_width"]
    versicolor = iris.loc[iris['species']=="versicolor", "sepal_length":"petal_width"]
    virginica = iris.loc[iris['species']=="virginica", "sepal_length":"petal_width"]

    # Create the figure and axes for the heatmap
    fig, axes = plt.subplots(nrows=1, ncols=4, figsize=(12,6), sharey='row')

    try:
        # Make sure the file can be created - handle the exception gracefully if not 
        with open(CORRELATION_IRIS, "w") as f:

                # Calculate and write the correlation across all species
                f.write("\nCorrelation summary for all iris species\n")
                corr = iris[["petal_length", "petal_width", "sepal_length", "sepal_width"]].corr()
                # The file write() function needs a string
                f.write(str(corr))
                f.write("\nNote: these correlations are not so meaningful as they are calculated across\n")
                f.write("3 different species. It is more meaningful to look at the separate correlations\n")
                f.write("for each species separately, and then compare the summaries.")

                # Draw the correlation heatmap for the iris dataset - only need 1 color bar
                sns.heatmap(corr, annot=True, fmt=".2f", linewidth=.5, ax=axes[0], cbar=False)
                axes[0].set_title("all iris species")

                # Calculate and write the correlation for the setosa species
                corr = setosa[["petal_length", "petal_width", "sepal_length", "sepal_width"]].corr()
                f.write("\n\nCorrelation summary for the setosa species\n")
                # The file write() function needs a string
                f.write(str(corr))

                # Draw the correlation heatmap for the setosa species - only need 1 color bar
                sns.heatmap(corr, annot=True, fmt=".2f", linewidth=.5, ax=axes[1], cbar=False)
                axes[1].set_title("setosa")

                # Calculate and write the correlation for the versicolor species
                corr = versicolor[["petal_length", "petal_width", "sepal_length", "sepal_width"]].corr()
                f.write("\n\nCorrelation summary for the versicolor species\n")
                # The file write() function needs a string
                f.write(str(corr))

                # Draw the correlation heatmap for the versicolor species - only need 1 color bar
                sns.heatmap(corr, annot=True, fmt=".2f", linewidth=.5, ax=axes[2], cbar=False)
                axes[2].set_title("versicolor")

                # Calculate and write the correlation for the virginica species
                corr = virginica[["petal_length", "petal_width", "sepal_length", "sepal_width"]].corr()
                f.write("\n\nCorrelation summary for the virginica species\n")
                # The file write() function needs a string
                f.write(str(corr))

                # Draw the correlation heatmap for the virginica species (with color bar) and write all to file
                sns.heatmap(corr, annot=True, fmt=".2f", linewidth=.5, ax=axes[3], cbar=True)
                axes[3].set_title("virginica")

                # Configure the x and y axis labels
                for i in range(4):
                    axes[i].set_xticks([0.5,1.5,2.5,3.5], labels=['p_len', 'p_wth', 's_len', 's_wth'])
                    axes[i].xaxis.set_tick_params(rotation=45, labelsize=9)
                    axes[i].set_yticks([0.5,1.5,2.5,3.5], labels=['p_len', 'p_wth', 's_len', 's_wth'])
                    axes[i].yaxis.set_tick_params(rotation=0, labelsize=9)

                # Set the overall title for the figure
                fig.suptitle("Iris dataset - heatmap of correlation coefficients\n",
                             fontsize=14, fontweight='bold')

                # Save the plot
                plt.savefig(HEATMAP_IRIS)

                # All data written, now close the file
                f.close()
                # Print a confirmation message and keep it on screen to allow the user to see it
                print("Correlation summaries and heatmaps written to", HEATMAP_IRIS)
                x = input("Press 'Return' to continue")    

    except OSError:
        # Handle the exception
        print("Error - file could not be created")

    return