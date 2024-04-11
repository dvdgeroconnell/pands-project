# write_summary.py (PANDS project)
#
# A Python function to calculate some key statistics for the iris dataset overall and by species. They
# are then written to a file.
#
# Author: David O'Connell
#
# Reference(s)
#  - Programming and Scripting lecture series - week 07 (files)
#  - Principles of Data Analytics lecture series - week 08 (iris dataset)
#  - Seaborn documentation / tutorials - https://seaborn.pydata.org/tutorial/function_overview.html
#  - Pandas methods - https://pandas.pydata.org/docs/reference/index.html
#
# ***************************************************************************************************

# Define file name where the statistical data will be saved - can be easily moved to a config file 
FILENAME = "iris_summary.txt"

# Define the function that will be called from the main program
def summary(iris, choice):

# Extract the columns with numerical data by species
    setosa = iris.loc[iris['species']=="setosa", "sepal_length":"petal_width"]
    versicolor = iris.loc[iris['species']=="versicolor", "sepal_length":"petal_width"]
    virginica = iris.loc[iris['species']=="virginica", "sepal_length":"petal_width"]

    # Originally used describe(), however it is a shortcut and is fixed in the statistics that it 
    # calculates, so changed to the .agg method instead.

    # result = str(iris.describe())

    # Create summary statistics for the iris dataset - min, max, median, mean, standard deviation
    result = iris.agg({"petal_length":["min", "max", "median", "mean", "std"],
                       "petal_width":["min", "max", "median", "mean", "std"],
                       "sepal_length":["min", "max", "median", "mean", "std"],
                       "sepal_width":["min", "max", "median", "mean", "std"]})

    # Create summary statistics for the setosa species - min, max, median, mean, standard deviation
    set_res = setosa.agg({"petal_length":["min", "max", "median", "mean", "std"],
                          "petal_width":["min", "max", "median", "mean", "std"],
                          "sepal_length":["min", "max", "median", "mean", "std"],
                          "sepal_width":["min", "max", "median", "mean", "std"]})

    # Create summary statistics for the versicolor species - min, max, median, mean, standard deviation
    ver_res = versicolor.agg({"petal_length":["min", "max", "median", "mean", "std"],
                              "petal_width":["min", "max", "median", "mean", "std"],
                              "sepal_length":["min", "max", "median", "mean", "std"],
                              "sepal_width":["min", "max", "median", "mean", "std"]})

    # Create summary statistics for the virginica species - min, max, median, mean, standard deviation
    vir_res = virginica.agg({"petal_length":["min", "max", "median", "mean", "std"],
                             "petal_width":["min", "max", "median", "mean", "std"],
                             "sepal_length":["min", "max", "median", "mean", "std"],
                             "sepal_width":["min", "max", "median", "mean", "std"]})

    # Write the summary statistics to FILENAME - check the filename can be opened / created
    try:
        with open(FILENAME, "w") as f:

            # Use a match statement to parse the choice 
            match(choice):

                # If "all" is passed, then write statistics for the iris dataset and by species
                case "all":
                    f.write("\nOverall summary for the iris dataset\n")
                    f.write(str(result))
                    f.write("\nNote: these statistics are not so meaningful as they are calculated across 3\n")
                    f.write("different species. It is more meaningful to look at the separate summaries for\n")
                    f.write("each species separately, and then compare the summaries.\n")
                    f.write("\nStatistical summary for the setosa species\n")
                    f.write(str(set_res))
                    f.write("\n\nStatistical summary for the versicolor species\n")
                    f.write(str(ver_res))
                    f.write("\n\nStatistical summary for the virginica species\n")
                    f.write(str(vir_res))

                # Write statistics for the setosa species
                case "setosa":
                    f.write("\n\nStatistical summary for the setosa species\n")
                    f.write(set_res)

                # Write statistics for the versicolor species
                case "versicolor":
                    f.write("\n\nStatistical summary for the versicolor species\n")
                    f.write(ver_res)

                # Write statistics for the virginica species
                case "virginica":
                    f.write("\n\nStatistical summary for the virginica species\n")
                    f.write(vir_res)

            # All data written, now close the file
            f.close()    
            # Print a confirmation message and keep it on screen to allow the user to see it
            print("Dataset summary written to", FILENAME)
            x = input("Press 'return' to continue")   
    
    # Handle the error if the file could not be created / opened
    except OSError:
        print("Error - file could not be created")

    return