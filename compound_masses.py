import re

# Define a function to calculate the molecular mass of a compound
def calculate_molecular_mass(compound):
    atomic_masses = {"H": 1.008, "He": 4.003, "Li": 6.941, "Be": 9.012, "B": 10.81, "C": 12.01, "N": 14.01, "O": 16.00,
                     "F": 19.00, "Ne": 20.18, "Na": 22.99, "Mg": 24.31, "Al": 26.98, "Si": 28.09, "P": 30.97,
                     "S": 32.07, "Cl": 35.45, "K": 39.10, "Ca": 40.08, "Sc": 44.96, "Ti": 47.87, "V": 50.94,
                     "Cr": 52.00, "Mn": 54.94, "Fe": 55.85, "Co": 58.93, "Ni": 58.69, "Cu": 63.55, "Zn": 65.38,
                     "Ga": 69.72, "Ge": 72.63, "As": 74.92, "Se": 78.96, "Br": 79.90, "Kr": 83.80}

    # Split the compound formula into individual elements and store them in a list
    elements = re.findall('([A-Z][a-z]*)(\d*)', compound)

    # Calculate the molecular mass of the compound using the atomic masses dictionary
    molecular_mass = sum([atomic_masses[element[0]] * float(element[1] or 1) for element in elements])

    return molecular_mass


# Define a function to ask user whether he/she wants to calculate mass for another compound.
def repeat():
    while True:
        try:
            answer = input("Do you want to calculate mass for another compound (yes/no)? ")
            if answer.lower().startswith("y"):
                main()
                break
            elif answer.lower().startswith("n"):
                print("Goodbye!")
                break
            else:
                raise ValueError("Invalid input. Please enter 'yes' or 'no'.")
        except ValueError as e:
            print(e)


# Define a main function to run the program
def main():
    while True:
        try:
            # Ask user to input the compound formula and print out that input is case sensitive
            compound_formula = input("Please enter the compound formula(case-sensitive): ")
            if not compound_formula.islower():
                # Call the calculate_molecular_mass function and print the result
                print("The molecular mass of the compound is:", calculate_molecular_mass(compound_formula))
                # Call the repeat function
                repeat()
                break
            else:
                raise ValueError("Input is case sensitive. Please enter the compound formula again.")
        except ValueError as e:
            print(e)


# Call the main function to start the program
main()
