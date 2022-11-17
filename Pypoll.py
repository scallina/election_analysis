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


# Open the election results and read the file.
with open(file_to_load) as election_data:

    #Read the file object with the reader function
    file_reader = csv.reader(election_data)

    #read and print the header row
    headers = next(file_reader)
    print(headers)

    


    #To-do: run the analysis

    # the data we need to retrieve. 

    # 1.Total number of votes cast

    # 2.complete list of candisates who received votes

    # 3.total number of votes each candidate received

    # 4.Percentage of votes each candidate won

    # 5. the winner of the election based on popular vote
