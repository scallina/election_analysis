#Add our dependencies
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# using the open() function within the "w" mode we will write data to the file
with open(file_to_save, "w") as txt_file:

    #Write some data into the file
    txt_file.write("Counties in the Election\n--------------------------\nArapahoe\nDenver\nJefferson")

#initialize total_votes to 0
total_votes = 0

#Declare Candidate_options list
candidate_options = []

#Declare Candidate_Votes dictionary
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    #Read the file object with the reader function
    file_reader = csv.reader(election_data)

    #read and print the header row
    headers = next(file_reader)
    print(headers)

    #print each row in the csv file
    for row in file_reader:
          #add to the total row count
        total_votes += 1
        
        #print the candidate names for each row
        candidate_name = row[2]
        
      
        #Check if the candidate name is int he Candidate options list
        if candidate_name not in candidate_options:

            #Add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            #Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

        #Add a vote to that candiate's count
        candidate_votes[candidate_name] += 1

    #print the candidate vote dictionary
    print(candidate_votes)

#iterate throught candidate_options list to get names
for candidate_name in candidate_votes:

    #use variable to retrieve the votes of the candidate from candidate_votes {}
    votes = candidate_votes[candidate_name]
    #calaculate percentage of the vote
    vote_percentage = float(votes) / float(total_votes) * 100

    print(f'{candidate_name}: {vote_percentage:.1f}% ({votes})\n')

    #Determine if the votes are greater than the winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        #if true then set the winning_count = votes and winning_percentage = vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage
        #set the winning_candidate equalt to candidate_name
        winning_candidate = candidate_name

    #to do: print the winning candidate, vote count and percentage to terminal

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

#Print the total votes
print(f'There are {total_votes} total votes')






    #To-do: run the analysis

    # the data we need to retrieve. 

    # 1.Total number of votes cast

    # 2.complete list of candisates who received votes

    # 3.total number of votes each candidate received

    # 4.Percentage of votes each candidate won

    # 5. the winner of the election based on popular vote
