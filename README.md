# election_analysis

## Project Overview

In this project, I assisted a Colorado board of elections employee in an election audit of the tabulated results for a U.S. congressional precinct in Colorado. I was tasked with reporting the total votes cast in the election, a summary of the vote distributions in 3 counties, and a summary of the vote distributions among the 3 candidates. 

## Resources
- Date source: election_results.csv
- Software: Python 3.9.13, Visual Studio Code, 1.73.1

## Results:

### Total Votes:
- There were a total of 369,711 votes cast in the election.

### Votes by county:
- Jefferson county accounted for 38,855 votes (10.5% of the total votes cast).
- Arapahoe county accounted for 24,801 votes (6.7% of the total votes cast).
- Denver county had the largest number of voters, accounting for 306,055 votes (82.8% of the total votes cast).

### Votes by candidate:
- Charles Casper Stockham received 85,123 (23% of the total) votes.
- Raymon Anthony Doane received 11,606 (3.1% of the total) votes. 
- Diana Degette won the election with 272,892 (73.8% of the total) votes.

## Summary of Election-Audit Script
This script can be used in future elections across different regions with few modifications needed. 

For example, this script could be used in presidential elections if some modifications were made to attribute a number of electoral votes to each state. This could be done using a second dictionary, matching a state name with a number of pre-determined electoral votes. From there, the for-loops could add in a reference to the second dictionary to count the ongoing tally of electoral votes. 
     
Another instance where this script could be modified would be in states such as Virginia, where cities exist independent of counties. The script would need to be modified with clearer titles. For example, the county_results variable could be redefined as locality_results. These updates would also be needed in the CSV document. 


