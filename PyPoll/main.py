# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
csv_path = os.path.join('PyPoll', 'Resources', 'election_data.csv')  # Input file path
output_path = os.path.join("PyPoll", "Analysis", "election_analysis.txt")  # Output file path

print(csv_path)
# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidates= {}

# Winning Candidate and Winning Count Tracker
winner_winner= ""
winner_count=0
# Open the CSV file and process it
with open(csv_path) as election_data:
        reader = csv.reader(election_data, delimiter='\t')

    # Skip the header row
        header = next(reader)

        # Loop through each row of the dataset and process it
        for row in reader:
        # Print a loading indicator (for large datasets)
            print(". ", end="")
        
        # Increment the total vote count for each row
            total_votes +=1

        # Get the candidate's name from the row
            candidate_names=row[2].strip()

        # If the candidate is not already in the candidate list, add them
            if candidate_names not in candidates: 
                candidates[candidate_names]=1
            else:
        # Add a vote to the candidate's count
                candidates[candidate_names] += 1


# Open a text file to save the output
with open(output_path, "w") as txt_file:

    # Print the total vote count (to terminal)
    election_results= ("\n"
            f"Election Results\n"
            f"------------------\n"
            f"Total Votes:{total_votes}\n"
            f"------------------\n")
    print(election_results)

    # Write the total vote count to the text file
    txt_file.write(election_results)

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate_names, vote_totals in candidates.items():
        
        # Get the vote count and calculate the percentage
        percentage=(float(vote_totals)/total_votes)*100

        # Update the winning candidate if this one has more votes
        if vote_totals>winner_count:
             winner_count=vote_totals
             winner_winner=candidate_names

        # Print and save each candidate's vote count and percentage
        results= f"{candidate_names}: {percentage:.3f}% ({vote_totals})\n"
        print(results)
        txt_file.write(results)

    # Generate and print the winning candidate summary
    winning_summary= (
             f"--------------\n"
             f"Winner: {winner_winner}\n"
             f"--------------\n")
    print (winning_summary)

    # Save the winning candidate summary to the text file
    txt_file.write(winning_summary)