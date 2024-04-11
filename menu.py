

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
    except ValueError:
        print("Invalid entry - ", end='')
        choice = 0
    return choice
