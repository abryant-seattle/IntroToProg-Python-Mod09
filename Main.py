# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# ABryant,6.13.2020,Modified and imported DataClasses, IOClasses, and Processing Classes modules
# ABryant,6.14.2020,Removed try-except block after modifying the employee class
# ABryant,6.15.2020,Captured demo images in PyCharm and Command Line, tidied for Git push
# ------------------------------------------------------------------------ #

if __name__ == "__main__":
    from DataClasses import Employee as Emp
    from ProcessingClasses import FileProcessor as Fp
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")

# Main Body of Script  ---------------------------------------------------- #

# Load data from file into a list of employee objects when script starts
text_file = "EmployeeData.txt"
lstFileData = Fp.read_data_from_file(text_file)
lstTable = []
for line in lstFileData:
    lstTable.append(Emp(line[0], line[1], line[2].strip()))

while True:
    try:
        # Show user a menu of options
        Eio.print_menu_items()

        # Get user's menu option choice
        menu_choice = int(Eio.input_menu_options())

        # Show user current data in the list of employee objects
        if menu_choice == 1:
            Eio.print_current_list_items(lstTable)

        # Let user add data to the list of employee objects
        elif menu_choice == 2:
            new_emp = Eio.input_employee_data()
            lstTable.append(new_emp)

        # let user save current data to file
        elif menu_choice == 3:
            Fp.save_data_to_file(text_file, lstTable)

        # Let user exit program
        elif menu_choice == 4:
            break

        # In case of invalid selection
        else:
            print('Invalid selection, please choose a valid menu option')
    # In case of an invalid selection
    except ValueError as e:
        print('Invalid selection, please choose a valid menu option')

    # Main Body of Script  ---------------------------------------------------- #
