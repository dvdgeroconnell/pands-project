
FILENAME = "iris_summary.txt"

def summary(iris, choice):

    setosa = iris.loc[iris['species']=="setosa", "sepal_length":"petal_width"]
    versicolor = iris.loc[iris['species']=="versicolor", "sepal_length":"petal_width"]
    virginica = iris.loc[iris['species']=="virginica", "sepal_length":"petal_width"]

    # Originally used describe(), however it is a bit of a shortcut and is fixed in the statistical
    # parameters it calculates, so moved to the .agg method instead.
    # result = str(iris.describe())

    result = iris.agg({"petal_length":["min", "max", "median", "mean", "std"],
                       "petal_width":["min", "max", "median", "mean", "std"],
                       "sepal_length":["min", "max", "median", "mean", "std"],
                       "sepal_width":["min", "max", "median", "mean", "std"]})

    set_res = setosa.agg({"petal_length":["min", "max", "median", "mean", "std"],
                          "petal_width":["min", "max", "median", "mean", "std"],
                          "sepal_length":["min", "max", "median", "mean", "std"],
                          "sepal_width":["min", "max", "median", "mean", "std"]})

    ver_res = versicolor.agg({"petal_length":["min", "max", "median", "mean", "std"],
                              "petal_width":["min", "max", "median", "mean", "std"],
                              "sepal_length":["min", "max", "median", "mean", "std"],
                              "sepal_width":["min", "max", "median", "mean", "std"]})

    vir_res = virginica.agg({"petal_length":["min", "max", "median", "mean", "std"],
                             "petal_width":["min", "max", "median", "mean", "std"],
                             "sepal_length":["min", "max", "median", "mean", "std"],
                             "sepal_width":["min", "max", "median", "mean", "std"]})

    # write a summary of the iris dataset to FILENAME
    try:
        with open(FILENAME, "w") as f:

            match(choice):

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

                case "setosa":
                    f.write("\n\nStatistical summary for the setosa species\n")
                    f.write(set_res)

                case "versicolor":
                    f.write("\n\nStatistical summary for the versicolor species\n")
                    f.write(ver_res)

                case "virginica":
                    f.write("\n\nStatistical summary for the virginica species\n")
                    f.write(vir_res)
                    
            f.close()    
            print("Dataset summary written")    
    
    except OSError:
        print("Error - file could not be created")

    return