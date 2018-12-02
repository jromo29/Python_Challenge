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

    #print(voter_id[0:10])
    #print(county[0:10])
    #print(candidate[0:10])

    unique_names = set(candidate[1:])

    unique_candidate=(list(unique_names))
    #print(unique_candidate)

    total_votes = len(voter_id)-1
    #print(total_votes)

    #candidate_totals={}
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
        #candidate_totals.update({u_name:stats})



        #print(round(perc_total_vote,2))

    #print(candidate_totals)

    print(unique_candidate)
    print(votes)
    print(perc)
    stats_zip = zip(unique_candidate,votes,perc)
    sorted(stats_zip, key=lambda x: x[1])
    zip(*unique_candidate,votes,perc)
    #print(stats_zip)
    for a,b,c in stats_zip: #zip(unique_candidate,votes,perc):
        print(a,b,c)


    name_count = len(unique_candidate)

    print(name_count)
    #stats = zip(unique_candidate,perc,votes)
    #print(stats[1])
    # print(votes)
    winner = max(votes)
    # print(winner)

    winner_pos = 0
    for v_num in votes:
        if v_num == winner:
            winner_pos = votes.index(v_num)

    #stats = {}


        #stats.update(name:[[perc],[votes]])

    #stats = {unique_candidate:[perc,votes]}
    #print (stats)

    # print (f"Winner :",unique_candidate[winner_pos])
    print("Election Results")
    print("------------------------")
    print(f"Total Votes: ",total_votes)
    print("------------------------")

    #print (votes[1])
    length = len(unique_candidate)
    for n in range(length):
        #print("{}".format(votes[n]))
        print("{0}: {1:.2%} ({2})".format(unique_candidate[n],perc[n],votes[n]))

    print("------------------------")
    print(f'Winner: ',unique_candidate[winner_pos])
    print("------------------------")
    #for n in unique_candidate:
        #index=(unique_candidate.index(n))
        #print("{0}".format(index))
        #print(unique_candidate[x],perc[x],votes[x])
        #print("{0} : {1.000}% {2}".format(unique_candidate[x]:perc[x]:votes[x]))

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
