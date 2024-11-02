import csv

# Variables to count the users with and without emails for hireable and non-hireable users
hireable_with_email = 0
hireable_total = 0
non_hireable_with_email = 0
non_hireable_total = 0

# Open the users.csv file and read data
with open('users.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        try:
            # Check if the user is hireable
            hireable_status = row['hireable'].strip().lower()
            
            # Check if the user has provided an email
            has_email = bool(row['email'].strip())
            
            if hireable_status == 'true':
                hireable_total += 1
                if has_email:
                    hireable_with_email += 1
            elif hireable_status == 'false':
                non_hireable_total += 1
                if has_email:
                    non_hireable_with_email += 1
        except KeyError:
            # Skip rows with missing hireable or email fields
            continue

# Ensure there is data for both hireable and non-hireable users
if hireable_total > 0 and non_hireable_total > 0:
    # Calculate the fraction of users with emails for both groups
    hireable_fraction = hireable_with_email / hireable_total
    non_hireable_fraction = non_hireable_with_email / non_hireable_total
    
    # Calculate the difference
    difference = hireable_fraction - non_hireable_fraction
    
    # Output the difference rounded to 3 decimal places
    print(f"Difference in email sharing: {difference:.3f}")
else:
    print("Insufficient data for hireable or non-hireable users.")
