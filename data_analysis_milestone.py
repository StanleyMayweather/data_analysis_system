# Basic program to find the lowest and highest life expectancy values

# File path to the CSV dataset

# Coding starts here...

file_path = 'life-expectancy.csv'

# Initialize min and max values
lowest_life_expectancy = float('inf')
highest_life_expectancy = float('-inf')

# Open and read the file line by line
with open(file_path, 'r') as file:
    next(file)  # Skip the header line
    for line in file:
        parts = line.strip().split(',')

        # Ensure the line has 4 columns
        if len(parts) == 4:
            try:
                life_expectancy = float(parts[3])  
                if life_expectancy < lowest_life_expectancy:
                    lowest_life_expectancy = life_expectancy
                if life_expectancy > highest_life_expectancy:
                    highest_life_expectancy = life_expectancy
            except ValueError:
                # Skip lines with invalid float values
                continue

# Display the results
print(f"Lowest life expectancy: {lowest_life_expectancy}")
print(f"Highest life expectancy: {highest_life_expectancy}")
