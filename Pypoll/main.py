import os

import csv

#Define path to budget_data csv
election_csv_input = os.path.join('..', 'Assignment 3', 'Python-challenge3', 'Resources', 'election_data.csv')

#Read election_data file
with open(election_csv_input, encoding='utf') as electionfile:
    csvreader = csv.reader(electionfile, delimiter=',')
    csv_header = next(csvreader) #To not count the header in calculations but store the value

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

#Print election results heading and total votes
    print(f'Election Results')
    print(f'------------------------------------------')
    print(f'Total Votes: {totalvotes}')
    print(f'------------------------------------------')

# Print the total number of votes for each candidate in the initialized dictionary
    for candidates, votes in candidate_vote_count.items():
        vote_percentage = round((votes/totalvotes)*100, 3)
        if vote_percentage > 50:
            winner = str(candidates)
        print(f'{candidates}: {vote_percentage}% ({votes})')

#Print Winner
    print(f'------------------------------------------')
    print(f'Winner: {winner}')

#Define output path of txt file
election_txt_output = os.path.join('..', 'Assignment 3', 'Python-challenge3', 'Analysis', 'election_data_analysis.txt')

#Write txt file with analysis
with open(election_txt_output, 'w') as pypoll_txt:
    pypoll_txt.write("Election Results")
    pypoll_txt.write('\n') #Creates a line break in the txt file to make it easier to read analysis
    pypoll_txt.write("-------------------------------------------------")
    pypoll_txt.write('\n')
    pypoll_txt.write(f'Total Votes: {totalvotes}')
    pypoll_txt.write('\n')
    pypoll_txt.write("-------------------------------------------------")
    for candidates, votes in candidate_vote_count.items():
        vote_percentage = round((votes/totalvotes)*100, 3)
        if vote_percentage > 50:
            winner = str(candidates)
        pypoll_txt.write('\n')
        pypoll_txt.write(f'{candidates}: {vote_percentage}% ({votes})')
    pypoll_txt.write('\n')   
    pypoll_txt.write(f'------------------------------------------')
    pypoll_txt.write('\n')
    pypoll_txt.write(f'Winner: {winner}')

        
