# Bring in Modules to standardize paths across different OS and read CSVs
import os
import csv

# Pointer to the csv file
csvpath = os.path.join('Resources','budget_data.csv')

# Declare variables
total_number_months = 0
net_total_profit_losses = 0

current_month_pl = 0
previous_month_pl = 0

profit_loss_changes = 0
month_over_month_changes = []  # python list

greatest_increase_profits_amount = 0
greatest_decrease_profits_amount = 0

# open and loop through csv file
with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(f'This is the reader object: {csvreader}')

    # get the csv header out of the way
    csvheader = next(csvreader)
    # print(f'CSV Header: {csvheader} ')

    # grab first row; first record
    first_row = next(csvreader) 

    # initialize variables for looping
    previous_month_pl = int(first_row[1])   #capture first row P&L
    total_number_months += 1                #counter of months
    net_total_profit_losses += int(first_row[1]) #start sum of profits

    # loop through every row
    for row in csvreader:
        
        # continue aggregations per row
        total_number_months += 1
        net_total_profit_losses += int(row[1])

        # set current month variable to column 2 of csv
        current_month_pl = int(row[1])

        # calculate changes in profit/losses month over month
        profit_loss_changes = current_month_pl - previous_month_pl

        # add month over month profit and loss changes to a list object
        month_over_month_changes.append(profit_loss_changes)

        # grab greatest increase in profits and month 
        if profit_loss_changes >= greatest_increase_profits_amount:
            greatest_increase_profits_amount = profit_loss_changes
            greatest_increase_profits_month = row[0]
        
        # greatest decrease in profits capture
        if profit_loss_changes <= greatest_decrease_profits_amount:
            greatest_decrease_profits_amount = profit_loss_changes
            greatest_decrease_profits_month = row[0]

        # save current month as previous for next go around
        previous_month_pl = current_month_pl


# calculate the average of the "profit and loss changes" list
average_pl_changes = round(sum(month_over_month_changes) / len(month_over_month_changes),2)

        
##########  RESULTS ########################

print(f'Financial Analysis')
print("----------------------------------")
print(f'Total Months: {total_number_months}')
print(f'Total: ${net_total_profit_losses}')
print(f'Average Change: ${average_pl_changes} ')
print(f'Greatest Increase in Profits: {greatest_increase_profits_month} (${greatest_increase_profits_amount}) ')
print(f'Greatest Decrease in Profits: {greatest_decrease_profits_month} (${greatest_decrease_profits_amount}) ')
 

####### CREATING OUTPUT FILE  #############

output_file = os.path.join('analysis','PyBank_financial_analysis.txt')

with open(output_file, 'w') as csvfile:
    csvwriter =  csv.writer(csvfile)
    csvwriter.writerow (["Financial Analysis"])
    csvwriter.writerow(["----------------------------------"])
    csvwriter.writerow(["Total Months: " + str(total_number_months)])
    csvwriter.writerow([f"Total: ${net_total_profit_losses}"])
    csvwriter.writerow([f"Average Change: ${average_pl_changes}"])
    csvwriter.writerow([f"Greatest Increase in Profits: {greatest_increase_profits_month} (${greatest_increase_profits_amount})"])
    csvwriter.writerow([f"Greatest Decrease in Profits: {greatest_decrease_profits_month} (${greatest_decrease_profits_amount})"])




