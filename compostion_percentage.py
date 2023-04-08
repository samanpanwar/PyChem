# Define the molar masses of elements in g/mol
molar_masses = {'H': 1.008, 'C': 12.011, 'N': 14.007, 'O': 15.999}

# Define a function to calculate the percentage composition of a compound
def percentage_composition(compound):
    element_count = {}
    total_mass = 0
    i = 0
    while i < len(compound):
        element = compound[i].upper()
        if element in molar_masses:
            count = 1
            if i < len(compound) - 1 and compound[i+1].isdigit():
                count = int(compound[i+1])
                i += 1
            total_mass += molar_masses[element] * count
            if element in element_count:
                element_count[element] += count
            else:
                element_count[element] = count
        else:
            raise ValueError(f"Unknown element '{element}'")
        i += 1
    print(f"Compound: {compound}")
    print(f"Element count: {element_count}")
    composition = {}
    for element, count in element_count.items():
        composition[element] = (molar_masses[element] * count) / total_mass * 100
    return composition

# Ask user if they want to test a compound
while True:
    repeat = input("Do you want to test a compound? (y/n): ")
    if repeat.lower() == "y":
        # Prompt the user to enter a chemical formula
        while True:
            compound = input("\nEnter a chemical formula: ")
            try:
                # check if all uppercase elements in the input string are keys in the `molar_masses` dictionary
                if all(elem.upper() in molar_masses.keys() or elem.isdigit() for elem in compound):
                    break
                else:
                    print("Invalid input. Only the following elements and numerals are acceptable: ", list(molar_masses.keys()))
            except ValueError as e:
                print(e)

        # Calculate and print the percentage composition of the compound
        print(f"\nPercentage composition of {compound}:")
        composition = percentage_composition(compound)
        for element, percentage in composition.items():
            print(f"{element}: {percentage:.2f}%")
        print("\n" + "-"*40)
    elif repeat.lower() == "n":
        quit()
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
