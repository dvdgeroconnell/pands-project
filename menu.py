# menu.py (PANDS project)
#
# A Python function to draw the menu of options, check the entered choice is a valid integer and returns
# the value to the main program. Range checking is done by the main program.
#
# Author: David O'Connell
#
# Reference(s)
#  - Programming and Scripting lecture series - week 09 (error handling) and general
#
# ***************************************************************************************************

# Define the function that will be called from the main program
def do_menu():

    # The do_menu() function just draws the menu and returns the choice
    print("\nEnter one of the following:")
    print("1 for a statistical summary of the iris dataset to be written to a file")
    print("2 for a set of histograms representing the iris dataset variables written to a file")
    print("3 for histograms and density plots representing the individual iris variables written to 4 files")
    print("4 for a set of scatter plots representing the iris dataset variables")
    print("5 for the correlation and heatmaps of the iris dataset variables across the species")
    print("6 for the best fit line")
    print("0 to quit")

    # Check that the entered value is an integer - range check will be handled by the main program
    try:
        choice = int(input("Enter choice: "))

    # Handle non-integer entries gracefully
    except ValueError:
        print("Invalid entry - ", end='')
        choice = 0
    return choice