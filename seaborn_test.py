# seaborn_test.py
# Programming & Scripting project
#
# A program to experiment with various aspects of the seaborn visualization library

#  - a histogram of a normal distribution of 1000 values with a mean of 5 and a std deviation of 2
#    truncated at 10
#  - a plot of the function h(x) = x^3 in the range 0 - 10
#
# Author: David O'Connell
#
# Reference(s)
#   Programming and Scripting week 08 lecture series - Andrew Beatty
#   https://numpy.org/devdocs/reference/random/generated/numpy.random.normal.html
#   https://www.geeksforgeeks.org/how-to-plot-logarithmic-axes-in-matplotlib/
#   https://matplotlib.org/stable/gallery/color/named_colors.html
#   https://numpy.org/devdocs/reference/generated/numpy.histogram.html


# import the numPy and matplotlib packages - specifically the matplotlib pyplot lib.
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

# Function to cube the argument and return the result
def h(x):
    x = x**3
    return x

# Parameters for the normal distribution histogram and x^3 plot.
# Note - setting the histogram values to 3000, as the y-scale needs to go up to 1000 to accommodate
# the x**3 function and this restricts the 1000-value histogram to the bottom fifth of the plot.
# Tried log scale on the y axis, but it distorts the histogram.

locus = 5
std = 2
size = 1000
range_x = 10
hist_lbl = "normal distribution"
color1 = "cornflowerblue"
color2 = "mediumblue"
# Set a seed, the random numbers that are generated will always be the same.
np.random.seed(1)

# Create the normal distribution values with the specified mean, std deviation and number of values.
normaldata = np.random.normal(locus, std, size)

# new seaborn code - see https://gist.github.com/mwaskom/de44147ed2974457ad6372750bbe5751
#sb.distplot(normaldata, hist=False) - deprecated. Using kde=True draws the kernel density estimate.
sb.kdeplot(normaldata)
#sb.displot(normaldata, kde=True)
#sb.histplot(normaldata, kde=True)
plt.show()
'''
# Create the plot - truncate the histogram at 10
plt.hist(normaldata, range=(0,10), label=hist_lbl, color = color1, edgecolor = color2)

# Not strictly needed, as it is the default. Left it in as had experimented with log
plt.yscale('linear')
#plt.yscale('log')

# Calculate values for h(x) = x^3 across the range 0-10 (inclusive) and draw the plot as a red line
x = np.array(range(0,range_x+1))
y = h(x)
plt.plot(x,y, label="h(x)", color = "r")

# Add plot labels and title
plt.xlabel('normal distribution range, x')
plt.ylabel('normal distribution, y = h(x)')
plt.title('Weekly Assignment 08')

# Add the legend - this uses the label from the hist() and plot() functions
plt.legend()

# Finally, either draw or save the plot to a file
#plt.savefig('plottask_output.png')
plt.show()
'''