#!/usr/bin/env python3
# Author: Your Name
# Author ID: YourID
# Date Created: yyyy/mm/dd

import sys

# Conversion functions
def inches_to_cm(inches):
    return inches * 2.54

def cm_to_inches(cm):
    return cm / 2.54

# Main function using sys.argv for arguments
def main():
    print("1. Convert inches -> cm")
    print("2. Convert cm -> inches")
    
    # Ask for selection
    try:
        selection = input("Make your selection (1,2): ")
        if selection == '1':
            inches = input("Enter inches: ")
            # Convert to integer
            inches = int(inches)
            cm = inches_to_cm(inches)
            print("Number of cm: " + str(cm))

        elif selection == '2':
            cm = input("Enter cm: ")
            # Convert to integer
            cm = int(cm)
            inches = cm_to_inches(cm)
            print("Number of inches: " + str(inches))

        else:
            print("Invalid entry")

    except ValueError:
        print("Invalid entry")

if __name__ == "__main__":
    main()
