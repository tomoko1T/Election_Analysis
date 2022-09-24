# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won 
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources","election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis","election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0 
# Candidate options and candidate votes
candidate_options = []
candidate_votes = {}
# Track winning candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0 
winning_percentage = 0 
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader) 
    # Print each row in CSV file.
    for row in file_reader:
        # Add to the total votes count.
        total_votes += 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate add it the
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
              candidate_options.append(candidate_name)
            # And begin tracking that candidate's vote count.
              candidate_votes[candidate_name] = 0 
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
        
# Save the results to our text file.
with open(file_to_save,"w") as txt_file:
    # After opening the file printing the final vote count to the terminal.
    election_results = (
        f"\nElection Result\n"
        f"---------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"---------------------------\n")
    print(election_results,end="")
    # After printing the final vote count to the terminal save the final vote count to the text file.
    txt_file.write(election_results)
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")           
                
        # Print each candidate's voter count and percentage to the terminal. 
        print(candidate_results)
        # Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count and candidate
        # Determine if the votes i greater than the winning count. 
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # if true then set wining_count = votes and wining_percent = 
            # vote_percentage.
            winning_count = votes
            winning_candidate =  candidate_name
            winning_percentage = vote_percentage                   
        
    # Print the winning candidates' results to the terminal.
    winning_candidate_summary = (
        f"---------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winner Percentage: {winning_percentage:.1f}%\n"
        f"---------------------------\n")     
        
    print(winning_candidate_summary)
    # Save the wining candidate's results to the text file.
    text_file.write(winning_candidate_summary)





            



    
    
    






