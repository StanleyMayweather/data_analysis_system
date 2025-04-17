# This enhanced program finds the lowest and highest life expectancy in the dataset.
# It also allows the user to query a specific country for detailed statistics (min, max, avg),
# and detects the country-year pair with the largest drop in life expectancy between two consecutive years.

# Coding starts here...

import csv
from collections import defaultdict

# File path to the CSV dataset
file_path = "life-expectancy.csv"

lowest = float('inf')
highest = float('-inf')

country_data = defaultdict(list)
largest_drop_info = {
    "country": None,
    "year_from": None,
    "year_to": None,
    "drop": 0.0
}

# Load and process the file
with open(file_path, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header

    for row in reader:
        if len(row) != 4:
            continue
        country, code, year, life_exp = row
        try:
            year = int(year)
            life_exp = float(life_exp)
        except ValueError:
            continue

        # Track lowest and highest globally
        if life_exp < lowest:
            lowest = life_exp
        if life_exp > highest:
            highest = life_exp

        # Store for country-based analysis
        country_data[country].append((year, life_exp))

# Show global min and max
print(f"\n🌍 Global Lowest Life Expectancy: {lowest}")
print(f"🌍 Global Highest Life Expectancy: {highest}")

# Ask user for a country to analyze
user_country = input("\nEnter a country name to explore its life expectancy stats: ").strip()

if user_country in country_data:
    records = country_data[user_country]
    records.sort()  # Sort by year

    life_expectancies = [exp for _, exp in records]
    min_exp = min(life_expectancies)
    max_exp = max(life_expectancies)
    avg_exp = sum(life_expectancies) / len(life_expectancies)

    print(f"\n📊 Stats for {user_country}:")
    print(f"Minimum Life Expectancy: {min_exp}")
    print(f"Maximum Life Expectancy: {max_exp}")
    print(f"Average Life Expectancy: {avg_exp:.2f}")

    # Detect largest drop
    for i in range(1, len(records)):
        prev_year, prev_exp = records[i - 1]
        curr_year, curr_exp = records[i]
        drop = prev_exp - curr_exp
        if drop > largest_drop_info['drop']:
            largest_drop_info = {
                "country": user_country,
                "year_from": prev_year,
                "year_to": curr_year,
                "drop": drop
            }
else:
    print(f"\n❌ Country '{user_country}' not found in dataset.")

# Display largest year-over-year drop in life expectancy
if largest_drop_info["country"]:
    print("\n📉 Largest Drop in Life Expectancy Detected:")
    print(f"{largest_drop_info['country']} had a drop of {largest_drop_info['drop']:.2f} years from {largest_drop_info['year_from']} to {largest_drop_info['year_to']}")
