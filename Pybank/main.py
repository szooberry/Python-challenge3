import os

import csv

#Define path to budget_data csv
budget_csv_input = os.path.join('..', 'Assignment 3', 'Python-challenge3', 'Resources', 'budget_data.csv')

#Read budget_data file
with open(budget_csv_input, encoding='utf') as budgetfile:
    csvreader = csv.reader(budgetfile, delimiter=',')
    csv_header = next(csvreader) #To not count the header in calculations but store the value

# Define variables for the for loop
    totalmonths = 0
    net_profit_loss = 0
    last_value = 0
    diff_net_profit = 0
    changes_in_net_profit = []
    changes_in_net_profit_months = []
    

# For loops for total month, net profit/loss, changes in profit/loss over entire period, greatest increase and greatest decrease
    for row in csvreader:

#Calculates total months and net profit/loss
        totalmonths = totalmonths + 1
        net_profit_loss = net_profit_loss + int(row[1])
       

#Creates a list of changes in net profit using the for loop        
        diff_net_profit = int(row[1]) - int(last_value)
        changes_in_net_profit.append(diff_net_profit)
        last_value = row[1]

        changes_in_net_profit_months.append(row[0])


# Removes first month and first month value from the list of changes in net profit, then caculates the average and rounds to 2 decimal places
    del changes_in_net_profit[0]
    average_change_in_profit = round(sum(changes_in_net_profit)/len(changes_in_net_profit), 2)

    changes_in_net_profit_months.remove(changes_in_net_profit_months[0])

# Zips together the months to the profit/loss change during that month for greatest increase/decrease calculation
    changes_zip = zip(changes_in_net_profit_months, changes_in_net_profit)

# Assigns variable for greatest increase and decrease in profit
    greatest_increase = 0
    greatest_decrease = 0

# For loop to calculate the greatest increase/decrease based on the changes calculated
    for change in changes_zip:
         if greatest_increase < int(change[1]):
             greatest_increase = int(change[1])
             greatest_increase_month = change[0]
        
         if greatest_decrease > int(change[1]):
             greatest_decrease = int(change[1])
             greatest_decrease_month = change[0]

# Prints all cacluations as financial analysis to the terminal
    print("Financial Analysis")

    print("-------------------------------------------------")

    print(f'Total Months: {totalmonths}')
    print(f'Net: ${net_profit_loss}')
    print(f'Average Change: ${average_change_in_profit}') 
    print(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})')
    print(f'Greatest Increase in Profits: {greatest_decrease_month} (${greatest_decrease})')    

# Define path for txt file output
budget_txt_output = os.path.join('..', 'Assignment 3', 'Python-challenge3', 'Analysis', 'budget_data_analysis.txt')

#Write txt file with analysis
with open(budget_txt_output, 'w') as pybank_txt:
    pybank_txt.write("Financial Analysis")
    pybank_txt.write('\n') #Creates a line break in the txt file to make it easier to read analysis
    pybank_txt.write("-------------------------------------------------")
    pybank_txt.write('\n')
    pybank_txt.write(f'Total Months: {totalmonths}')
    pybank_txt.write('\n')
    pybank_txt.write(f'Net: ${net_profit_loss}')
    pybank_txt.write('\n')
    pybank_txt.write(f'Average Change: ${average_change_in_profit}') 
    pybank_txt.write('\n')
    pybank_txt.write(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})')
    pybank_txt.write('\n')
    pybank_txt.write(f'Greatest Increase in Profits: {greatest_decrease_month} (${greatest_decrease})')
