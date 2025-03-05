#-*- coding: UTF-8 -*-
#"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output 
csv_path = os.path.join("PyBank", "Resources", "budget_data.csv")  # Input file path 
output_path = os.path.join("PyBank", "Analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
changes = []
greatest_inc= ["", 0]
greatest_dec= ["", 0]
# Open and read the csv
with open(csv_path) as financial_data:
    reader = csv.reader(financial_data, delimiter= '\t')

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row= next(reader)
    # Track the total and net change
    total_months += 1
    total_net += int(first_row[1])
    previous_net = int(first_row[1])

    # Process each row of data
    for row in reader:
        if len(row)<2:
            continue 

        # Track the total
        total_months += 1
        total_net += int(row[1])

        # Track the net change
        net_change= int(row[1])- previous_net
        changes.append(net_change)
        previous_net = int(row[1])

        # Calculate the greatest increase in profits (month and amount)
        if net_change >greatest_inc[1]:
            greatest_inc=[row[0], net_change]

        # Calculate the greatest decrease in losses (month and amount)
        if net_change < greatest_dec[1]:
            greatest_dec=[row[0], net_change]


# Calculate the average net change across the months
avg_net_change= sum(changes)/ len(changes) if changes else 0

# Generate the output summary
output = (
    f"Financial Analysis\n"
    f"-------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: {avg_net_change}\n"
    f"Greatest Increase in Profits: {greatest_inc}\n"
    f"Greatest Decrease in Profits: {greatest_dec}\n"
)

# Print the output
print(output)

# Write the results to a text file
with open(output_path, "w") as txt_file:
    txt_file.write(output)