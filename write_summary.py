
FILENAME = "iris_summary.txt"

def petal_length_summary(iris, setosa, versicolor, virginica):
    
    with open(FILENAME, "w") as f:

        # write a summary of the iris dataset to FILENAME
        f.write("\nOverall Summary\n")
        x = str(iris.describe())
        f.write(x)
        f.write("\n\nSummary for the setosa species\n")
        x = str(setosa.describe())
        f.write(x)
        f.write("\n\nSummary for the versicolor species\n")
        x = str(versicolor.describe())
        f.write(x)
        f.write("\n\nSummary for the virginica species\n")
        x = str(virginica.describe())
        f.write(x)

    return