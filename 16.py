import csv
from collections import Counter

# Dictionary to count the occurrences of each surname
surname_count = Counter()

# Open the users.csv file and read data
with open('users.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        try:
            # Get the user's name and split it by whitespace
            name = row['name'].strip()
            
            # Skip missing or empty names
            if name:
                # Split by whitespace and take the last word as the surname
                surname = name.split()[-1]
                
                # Increment the count for this surname
                surname_count[surname] += 1
        except KeyError:
            # Skip rows without the 'name' field
            continue

# Find the highest occurrence(s)
if surname_count:
    max_count = max(surname_count.values())
    
    # Get all surnames that have the maximum count
    most_common_surnames = [surname for surname, count in surname_count.items() if count == max_count]
    
    # Sort the surnames alphabetically and join them with commas
    most_common_surnames.sort()
    print(','.join(most_common_surnames))
else:
    print("No valid names found.")
