import os
import csv

#Path to retrieve data file
election_data_csv = os.path.join('..','election_data.csv')

# Lists to store data
voter_id = []
county = []
candidate = []

#Read file
with open(election_data_csv,newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ",")

    for row in csvreader:
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

    #identify unique candidate names
    unique_names = set(candidate[1:])

    #creat list with candidate names
    unique_candidate=(list(unique_names))

    #calculate total votes
    total_votes = len(voter_id)-1

    #Calcuate total votes for each candidate and percent of total votes
    votes = []
    perc = []

    for u_name in unique_candidate:

        vote_count = 0
        for name in candidate:
            if u_name == name:
                vote_count += 1

        perc_total_vote = vote_count / total_votes
        perc.append(perc_total_vote)
        votes.append(vote_count)

    #calculate winner
    winner = max(votes)
    winner_pos = 0

    for v_num in votes:
        if v_num == winner:
            winner_pos = votes.index(v_num)

    #Print Results
    print("Election Results")
    print("------------------------")
    print(f"Total Votes: ",total_votes)
    print("------------------------")

    length = len(unique_candidate)
    for n in range(length):
        #print("{}".format(votes[n]))
        print("{0}: {1:.2%} ({2})".format(unique_candidate[n],perc[n],votes[n]))

    print("------------------------")
    print(f'Winner: ',unique_candidate[winner_pos])
    print("------------------------")

    # Print Results to text file
    file_name = 'PyPoll Results.txt'

    with open(file_name, 'w') as file_object:

        file_object.write("Election Results")
        file_object.write("\n-------------------------")
        file_object.write("\nTotal Votes: " + str(total_votes))
        file_object.write("\n-------------------------")

        for n in range(0,length):
            file_object.write("\n{0}: {1:.2%} ({2})".format(unique_candidate[n],perc[n],votes[n]))

        file_object.write("\n-------------------------")
        file_object.write("\nWinner: " + str(unique_candidate[winner_pos]))
        file_object.write("\n-------------------------")

    file_object.close()
