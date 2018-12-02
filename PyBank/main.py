import os
import csv

#Path to retrieve data file
budget_data_csv=os.path.join('..','Budget_Data.csv')

# Lists to store data
month = []
net_profit =[ ]

#Read file
with open(budget_data_csv,newline="") as csvfile:
    csvreader=csv.reader(csvfile,delimiter = ",")

    #Create New Lists
    for row in csvreader:
        month.append(row[0])
        net_profit.append(row[1])

    #Calculate Total Profit
    total_profit = 0
    for value in net_profit[1:]:
        total_profit = total_profit + float(value)

    #Calculate Monthly Gain/Loss
    profit_change = 0
    profit_delta = ["Monthly Gain/Loss",1]
    prev_value = net_profit[1]
    total_delta = 0

    #Count number of elements in list
    profit_count = len(net_profit)

    for value in net_profit[2:]:

        profit_change = float(value)-float(prev_value)
        prev_value = value

        #Create new list with change in profit
        profit_delta.append(profit_change)

        #Sum all the changes in profit
        total_delta += profit_change

    #Calculate average change in Gain/Loss
    avg_delta = total_delta / (profit_count-2)

    #Find the Max and Min Gain/Loass
    max_monthly_gain = max(profit_delta[1:])
    max_monthly_loss = min(profit_delta[1:])

    #Find index value for max and min positions in list
    max_pos = 0
    min_pos = 0

    for element in profit_delta[1:]:
        if element == max_monthly_gain:
            max_pos = profit_delta.index(element)

    for element in profit_delta[0:]:
        if element == max_monthly_loss:
            min_pos = profit_delta.index(element)

    #Print Result in Terminal
    print('Financial Analysis')
    print("-------------------")
    print(f"Total Months:", len(month) - 1)
    print(f"Total: $", total_profit)
    print(f"Average Change: $", round(avg_delta, 2))
    print(f"Greatest Increase in Profits:",month[max_pos], " $",profit_delta[max_pos])
    print(f"Greatest Decrease in Profits:", month[min_pos], " $", profit_delta[min_pos])


#Print Results to text file
file_name = 'PyBank Results.txt'

with open(file_name,'w') as file_object:

    file_object.write("Financial Analysis")
    file_object.write("\n-------------------------")
    file_object.write("\nTotal Months: " + str(len(month)-1))
    file_object.write("\nTotal: $" + str(total_profit))
    file_object.write("\nAverage Change: $" + str(round(avg_delta,2)))
    file_object.write("\nGreatest Increase in Profits: " + str(month[max_pos]) + " $"+str(profit_delta[max_pos]))
    file_object.write("\nGreatest Decrease in Profits: " + str(month[min_pos]) + " $"+str(profit_delta[min_pos]))

file_object.close()
