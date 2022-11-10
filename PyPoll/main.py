# Bring in Modules to standardize paths across different OS and read CSVs
import os
import csv

# Declare variables
total_number_votes_cast = 0
candidates_dictionary = {}  # python dictionary

# Pointer to the csv file
csvpath = os.path.join('Resources','election_data.csv')

# open and loop through csv file
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    # get the csv header out of the way
    csvheader = next(csvreader)
    # print(f'csv header: {csvheader}')

    # loop through every row
    for row in csvreader:

        # counter for total number of rows
        total_number_votes_cast += 1

        # grab candidate name from 3rd column (for every row)
        current_candidate = row[2]
    
        # add a new candidate to dictionary or update its value
        if current_candidate in candidates_dictionary:
            candidates_dictionary[current_candidate] = candidates_dictionary[current_candidate] + 1 
            # the above is adding key, value +1 (effectively updating the value for key increasing by one as counter)
        else:
            candidates_dictionary[current_candidate] = 1  # adding key, value

# For Testing only ...
# for key, value in candidates_dictionary.items():
#     print(f'Candidate name: {key} , Votes Count: {value}')

#########  RESULTS  ###############

print(f"Election Results")
print("----------------------------")
print(f'Total Votes: {total_number_votes_cast}')
print("----------------------------")

for key, value in candidates_dictionary.items():
    print(f'{key}:  {round(value/total_number_votes_cast * 100, 3)}% ({value})')

print("----------------------------")

max_value = max(candidates_dictionary, key=candidates_dictionary.get)

print(f"Winner: {max_value}")
print("----------------------------")


#########  CREATE OUTPUT FILE  #########

output_file = os.path.join('analysis','PyPoll_election_results.txt')

with open(output_file, 'w') as text_file:
    csvwriter = csv.writer(text_file)
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow([f'Total Votes: {total_number_votes_cast}'])
    csvwriter.writerow(["----------------------------"])

    for key, value in candidates_dictionary.items():
        csvwriter.writerow([f"{key}:  {round(value/total_number_votes_cast * 100, 3)}% ({value})"])

    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow([f"Winner: {max_value}"])
    csvwriter.writerow(["----------------------------"])





