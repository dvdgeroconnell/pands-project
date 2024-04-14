# Programming and Scripting Project - the Iris data set 

| Topic | Details |
|---------|-------------|
| **Module:**  | Programming and Scripting  |
| **Lecturer:**  | Andrew Beatty  | 
| **Course:**  | Diploma in Science in Computing (Data Analytics)  |
| **Year/Semester:**  | Year 1/Semester 1  |
| **Student Name:**  | David O'Connell  |
| **Student ID:**  | G00438912  |
| **Student Email:**  | G00438912@atu.ie  |

# Table of Contents
[Purpose of this Repository](#Purpose-of-this-Repository)  
[References](#References)

## Purpose of this Repository  
<a name="Purpose-of-this-Repository"></a>  
This repository contains the files associated with the Programming and Scripting final project, the subject of which is an analysis of Fisher's iris data set.  
Link to repository - [PANDS Project](https://github.com/dvdgeroconnell/pands-project.git).  

## Project Summary
### Problem Statement
This is summarized from the detailed Project Description in [g2].
The project is about researching and analyzing the well-known Fisher’s Iris data set [g1]. The investigation requires documentation and code (in Python [c6]) to be written. The project will need to be broken into several smaller tasks that are easier to solve, and these will need to be plugged together once they have been completed. Steps to follow:

1. Research the data set online and write a summary about it in the README.
2. Download the data set and add it to the repository.
3. Write a program called analysis.py that:
    1. Outputs a summary of each variable to a single text file
    2. Saves a histogram of each variable to png files, and
    3. Outputs a scatter plot of each pair of variables
    4. Performs any other analysis you think is appropriate

The requiremnent for original text and analysis is emphasized in the Project Description.

### Approach
While it was left open as to whether to create a Jupyter notebook as well as the README, it was decided to capture the reasearch and analysis in the README to avoid repetition and / or referencing over and back between documents.

# Background Research  

## Fisher's Iris data set
The Iris flower data set was originally gathered by botanist [Edgar Anderson](https://en.wikipedia.org/wiki/Edgar_Anderson) as part of his work to develop techniques to quantify geographic variation the morphological differences and geographical variations between different species of Iris - Iris setosa, Iris versicolor and Iris virginica.  

**Figure 1 - Iris Species**  
![Iris species](images/iris_species_2.png)   
Source [g8]  

The data set contains 150 sets of measurements, consisting of a set of 50 measurements for each of the 3 species of Iris flowers across 4 attributes, those being petal length, petal width, sepal length and sepal width, measured in centimeters. The measurements cover the sepal and petal length and width for each flower in cm. These are shown in Figure 2 below.  

**Figure 2 - Iris Characteristics**  
![Iris characteristics](images/iris_characteristics.png)  
Source [g4]

The dataset is often called "Fisher's Iris data set" as it was presented as an example of linear discriminant analysis in a 1936 paper, *"The use of multiple measurements in taxonomic problems"* by the British statistician and biologist [Ronald A. Fisher](https://en.wikipedia.org/wiki/Ronald_Fisher). [Linear discriminant analysis](https://en.wikipedia.org/wiki/Linear_discriminant_analysis) is a method used in statistics, and other fields, to find a linear combination of features that characterizes or separates two or more classes of objects or events. Fisher used the Iris data set to demonstrate how his linear discriminant model could be used to distinguish the 3 species from each other based on the 4 known attributes [g1]. The paper is available [here](https://digital.library.adelaide.edu.au/dspace/handle/2440/15227).  

This data set is widely used in field of statistical data analysis and pattern recognition / machine learning.  
It is often used to understand classification and clustering algorithms.   

This dataset is particularly popular due to its simplicity and the clear separation of the different species based on the measured attributes. Using the features of the iris flowers, researchers and data scientists can classify each sample into one of the three species. One class (setosa) is linearly separable from the other 2; the other 2 (versicolor and virginica) are not linearly separable from each other [g1], [g7].  

# Using the Program
## Libraries and Packages Used
| Software | Version | Summary|
|---------|-------------|---------|
|[Python](https://www.python.org/) | 3.11.7 | Python is a programming language that lets you work more quickly and integrate your systems more effectively.  |
|[NumPy](https://numpy.org/) |1.26.4 | NumPy is an open source project that enables numerical computing with Python.  
|[Pandas](https://pandas.pydata.org/) |2.1.4 | Pandas is a software library written for the Python programming language for data manipulation and analysis.  |
|[Matplotlib](https://matplotlib.org/) | 3.8.0 | Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. |  
|[Seaborn](https://seaborn.pydata.org/) | 0.13.2 | Seaborn is a Python data visualization library based on matplotlib. |  
|[VS Code](https://code.visualstudio.com/) | 1.88.0 | Visual Studio Code is a lightweight but powerful source code editor which runs on your desktop. |  

## Files in this Repository  
### iris.csv
The raw dataset in useable csv format was downloaded from [here](https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv). This csv file has already undergone some cleanup, including the addition of a heaading row and presentation of the different species as simply *setosa*, *versicolor* and *virginica*.  
### analysis.py  
This file contains the main Python program to offer the menu options and run the relevant functions based on the menu option chosen.   
### menu.py  
This file contains a Python function to draw the menu of options, check the entered choice is a valid integer and return the value to the calling program, where the range checking is done.     
### write_summary.py  
This file contains a Python function to calculate the following statistics for the Iris dataset overall and by species, specifically:  
- Minimum value  
- Maximum value  
- Median value  
- Mean value  
- Standard Deviation  

The values are written to a text file. The name is displayed to the user.  
### hist_all.py  
This file contains a Python function to draw the histograms for the iris dataset variables by species. There are 12 in total, 4 per species.  
- Petal Length  
- Petal Width  
- Sepal Length  
- Sepal Width  

The histograms are drawn as a single figure, which is then saved to a file. The name is displayed to the user.  
### petal.py  
This file contains 2 Python functions to create histograms of a) the petal length and b) the petal width by species. They are then written to files. The name are displayed to the user.  
### sepal.py  
This file contains 2 Python functions to create histograms of a) the petal length and b) the petal width by species. They are then written to files. The names are displayed to the user.  
### scatter_all.py  
This file contains a Python function to draw the pairwise scatter plots for the Iris dataset variables, colour-coded by species. The scatter plots are drawn as a single figure using both Matplotlib and Seaborn for comparison. They are written to files and the names are displayed to the user.    
### write_correlation.py  
This file contains a Python function to calculate the correlation coefficients and draw the heatmaps for the Iris dataset, both overall and by species. The heatmaps are drawn as a single figure and saved to a file. The name is displayed to the user. 
### bestfit_all.py  
A Python function to draw the pairwise scatter plots for the Iris dataset variables colour-coded by species. Best fit lines are then calculated using NumPy's ployfit method and superimposed on the scatter plots. The plots are drawn as a single figure. Seaborn is then used to create similar scatter plots with best fit lines by species for comparison. Both versions are saved to files and the names are displayed to the user.

## Running the Program

Clone the GitHub repository using the link in the **Purpose of this Repository** section above [Purpose of this Repository](#Purpose-of-this-Repository).
Execute the program by typing *"python analysis.py"*. This results in the menu being presented.
The menu options and their outputs are described in the [Menu Options](#Program-Menu-Options) section.

# Analysis

## Correlation
The Pandas *corr()* method [c4] is used to establish a pairwise correlation between columns. NaN, NULL values are excluded.  
  
The method of correlation may be one of Pearson, Kendall-Tau and Spearman. Pearson is the default, and was used in this analysis [c5].  
The Pearson correlation coefficient is defined as "the ratio between the covariance of two variables and the product of their standard deviations" [g5], where covariance in probability theory and statistics is a measure of the joint variability of two random variables, X and Y, and is defined as "the expected value (or mean) of the product of the deviations of X and Y from their individual expected values"[g6].  

Pearson's correlation coefficient is essentially a normalized measurement of the covariance, such that the result always has a value between −1 and 1" [g5]. Covariance is defined as a measure of the joint variability of two random variables [g6], or in other words, how closely change in one is related to change in another. If both increase together, the covariance will be positive. If one decreases as the other increases, the covariance will be negative, denoting an inverse relationship. This can be seen in Figure 3.  

**Figure 3 - Scatter diagrams with various values of ρ, the correlation coefficient**  
![Correlation Coefficient](images/correlation_coefficient.png)  
Source [g5]  

The lower the correlation value in absolute terms, the weaker the relationship between the x and y variables. For example, 0.8 or -0.8 implies a strong relationship between the x and y variable; whereas a correlation of 0.2 or -0.2 implies a weak relationship.
Note that the Pearson correlation coefficient is symmetric: corr(X,Y) = corr(Y,X) [g5].  

## Best Fit

We will start with the most familiar linear regression, a straight-line fit to data. A straight-line fit is a model of the form y=ax+b where a is commonly known as the slope, and b is commonly known as the intercept.






## Program Menu Options
<a name="Program-Menu-Options"></a> 
The user is presented with the following menu:

    Enter one of the following:
    1 for a statistical summary of the iris dataset to be written to a file
    2 for a set of histograms representing the iris dataset variables written to a file
    3 for histograms and density plots representing the individual iris variables written to 4 files
    4 for a set of scatter plots representing the iris dataset variables
    5 for the correlation and heatmaps of the iris dataset variables across the species
    6 for the best fit line
    0 to quit
    Enter choice:

### Option 1 - Statistical Summary
what does it tell us?  

### Option 2 - Histograms
what does it tell us?

  ### Option 5 - Correlation & Heatmaps

Text file output - *iris_correlation.txt*   
    
    Correlation summary for all iris species
                petal_length  petal_width  sepal_length  sepal_width
    petal_length      1.000000     0.962865      0.871754    -0.428440
    petal_width       0.962865     1.000000      0.817941    -0.366126
    sepal_length      0.871754     0.817941      1.000000    -0.117570
    sepal_width      -0.428440    -0.366126     -0.117570     1.000000
      
    Note: these correlations are not so meaningful as they are calculated across
    3 different species. It is more meaningful to look at the separate correlations
    for each species separately, and then compare the summaries.

    Correlation summary for the setosa species
                petal_length  petal_width  sepal_length  sepal_width
    petal_length      1.000000     0.331630      0.267176     0.177700
    petal_width       0.331630     1.000000      0.278098     0.232752
    sepal_length      0.267176     0.278098      1.000000     0.742547
    sepal_width       0.177700     0.232752      0.742547     1.000000

    Correlation summary for the versicolor species
                petal_length  petal_width  sepal_length  sepal_width
    petal_length      1.000000     0.786668      0.754049     0.560522
    petal_width       0.786668     1.000000      0.546461     0.663999
    sepal_length      0.754049     0.546461      1.000000     0.525911
    sepal_width       0.560522     0.663999      0.525911     1.000000

    Correlation summary for the virginica species
                petal_length  petal_width  sepal_length  sepal_width
    petal_length      1.000000     0.322108      0.864225     0.401045
    petal_width       0.322108     1.000000      0.281108     0.537728
    sepal_length      0.864225     0.281108      1.000000     0.457228
    sepal_width       0.401045     0.537728      0.457228     1.000000

  Test here  
    
![Iris correlation](images/corr_iris.png)  
  
#### Observations
Negative correlations for the iris overall are positive for each of the species. When the best fit lines for those pairs of variables aer viewed in graphical form, the reason can clearly clearly see clear to see.

### Best Fit  
text here  
![Best Fit - NumPy, Pyplot](images/bestfit_plt_1.png)  
  

#### Observations
1. The best fit line for all species has a positive slope in all cases, which implies that as one attribute increases, the other is also likely to increase.


## How to use this Repository





Note to self - review this - https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes


# References  
<a name="References"></a>  
## Methodology  
Since markdown doesn't support superscripts, the paragraph, quotation or figure are followed by the applicable reference or citation in square brackets. The references are listed below, and are prefixed with 'g' or 'c' depending on whether they're in the list of general or code references. So, for example, [g7] refers to item 7 in the General Reference list below.

## General References    
General references are prefixed with 'g'.  
1. [iris dataset wikipedia page](https://en.wikipedia.org/wiki/Iris_flower_data_set)  
2. [Project Description](PANDS_Project_2024.pdf)  
3. [About Fisher's Iris dataset](https://www.angela1c.com/projects/iris_project/the-iris-dataset/)  
4. [Exploring the Iris flower dataset](https://eminebozkus.medium.com/exploring-the-iris-flower-dataset-4e000bcc266c)  
5. [Pearson Correlation Coefficient](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient)  
6. [Covariance](https://en.wikipedia.org/wiki/Covariance)  
7. [UCI Irvine Machine Learning Repository](https://archive.ics.uci.edu/dataset/53/iris)  
8. [The Iris Dataset - A Little Bit of History and Biology](https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5)  
9. [Iris data set in Machine Learning](https://www.geeksforgeeks.org/iris-dataset/)   
  
## Code References  
Code references are prefixed with 'c'.  
1. [matplotlib subplots page](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html)  
2. [match/case statement syntax](https://www.datacamp.com/tutorial/python-switch-case)  
3. [Pandas tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html)  
4. [Pandas correlation method](https://www.geeksforgeeks.org/python-pandas-dataframe-corr/)  
5. [Pandas documentation on corr()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html)  
6. [Python Software Foundation](https://www.python.org/)

## Other References
References that are not explicitly linked to a specific part of the document but of general use.  
1. [Linking within a Markdown document](https://stackoverflow.com/questions/2822089/how-to-link-to-part-of-the-same-document-in-markdown)  
2. [Iris data set Analysis in Kaggle](https://www.kaggle.com/search?q=iris+dataset+analysis)  


****
#### End