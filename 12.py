import csv

# Variables to store the total following and count for hireable and non-hireable users
hireable_following = []
non_hireable_following = []

# Open the users.csv file and read data
with open('users.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        try:
            # Get following count
            following_count = int(row['following'])
            
            # Check if user is hireable
            hireable_status = row['hireable'].strip().lower()
            
            if hireable_status == 'true':
                hireable_following.append(following_count)
            elif hireable_status == 'false':
                non_hireable_following.append(following_count)
        except (ValueError, KeyError):
            # Skip rows with invalid numerical values or missing fields
            continue

# Ensure there is data for both hireable and non-hireable users
if hireable_following and non_hireable_following:
    # Calculate the averages for both groups
    avg_hireable = sum(hireable_following) / len(hireable_following)
    avg_non_hireable = sum(non_hireable_following) / len(non_hireable_following)
    
    # Calculate the difference
    difference = avg_hireable - avg_non_hireable
    
    # Output the difference rounded to 3 decimal places
    print(f"Difference in average following: {difference:.3f}")
else:
    print("Insufficient data for hireable or non-hireable users.")
