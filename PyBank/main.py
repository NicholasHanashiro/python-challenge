# importing needed libaries
import os
import csv


# Getting to the file path with my needed csv. One directory backwards and then into resources
budget_data = os.path.join('..','Resources', 'budget_data.csv')

# Declaring all my needed arrays and variables
net_totals = []
profit_changes_str = []
profit_changes = []
avg_change = []
total_months = 1
current_month = 0
next_month = 0
month_change = []
total_profit_changes = 0
avg_profit_changes = 0

# reading the csv file through the path i specified earlier
with open (budget_data) as budget_data:
	csv_reader = csv.reader(budget_data, delimiter = ",")

	header = next(csv_reader)
	for i in csv_reader:

		# Adding to my profit changes list
		profit_changes_str.append(i[1])
		# adding to my net totals list
		net_totals.append(i[1])
		# making sure to change the data type of my list from string to int
		net_totals = [int(item) for item in net_totals]
		# counting all the months
		total_months = total_months + 1

	for i in range(len(net_totals)):

		try:
			# setting current month to the first item in net totals
			current_month = int(net_totals[i])
			# Setting next month to the item one after the current month
			next_month = int(net_totals[i+1])
			# getting the difference
			month_change = next_month - current_month
			# adding the difference to a list
			profit_changes.append(month_change)
		# code always broke at the end from an index error
		except IndexError:
			break


	# printing all requested information to the terminal
	print ("Total Months: " + str(total_months - 1))
	print ("Total: " + str(sum(net_totals)))

	# now that these variables have values I can use them to solve for others
	total_profit_changes = sum(profit_changes)
	avg_profit_changes = total_profit_changes/len(profit_changes)
	
	# printing the rest of the requested info to the terminal
	print("Average Change: " + str(avg_profit_changes))
	print ("Greatest Increase in Profits: " + str(max(profit_changes)))
	print ("Greatest Decrease in Profits: " + str(min(profit_changes)))


	# Creating text file
	file = open("PyBank_Financial_Analysis.txt", "w")
	# writing to the text file
	file.write("Total Months: " + str(total_months - 1))
	# new Line
	file.write("\n")
	file.write("Total: " + str(sum(net_totals)))
	file.write("\n")
	file.write("Average Change: " + str(avg_profit_changes))
	file.write("\n")
	file.write("Greatest Increase in Profits: " + str(max(profit_changes)))
	file.write("\n")
	file.write("Greatest Decrease in Profits: " + str(min(profit_changes)))

	# closing the text file
	file.close()