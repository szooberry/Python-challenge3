import os

import csv

#Define path to budget_data csv
election_csv_input = os.path.join('..', 'Assignment 3', 'challenge3-python', 'Resources', 'election_data.csv')

#Read election_data file
with open(election_csv_input, encoding='utf') as electionfile:
    csvreader = csv.reader(electionfile, delimiter=',')
    next(electionfile, None) #To not count the header in calculations

#Define variables for total votes
#Initialize a list of frequency of votes for each candidate
#Initialize a dictionary to store the tally of votes for each candidate
    totalvotes = 0
    listofcandidates = []
    candidate_vote_count = {}

#Calculate the total votes from the csv 
#Separate a list containing the frequency of votes by candidate name
    for row in csvreader:
        totalvotes = totalvotes + 1
        listofcandidates.append(str(row[2]))

#Using the frequency list, tally the number of votes for each candidate
    for candidate in listofcandidates:
        if candidate in candidate_vote_count:
            candidate_vote_count[candidate] += 1
        else:
            candidate_vote_count[candidate] = 1

    print(f'Election Results')
    print(f'------------------------------------------')
    print(f'Total Votes: {totalvotes}')
    print(f'------------------------------------------')
#Print the total number of votes for each candidate in the initialized dictionary
    for candidates, votes in candidate_vote_count.items():
        vote_percentage = round((votes/totalvotes)*100, 2)
        if vote_percentage > 50:
            winner = str(candidates)
        print(f'{candidates}: {vote_percentage}% ({votes})')
      
    print(f'------------------------------------------')
    print(f'Winner: {winner}')
    
        

        
