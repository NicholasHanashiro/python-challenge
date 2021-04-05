import os
import csv
#import numpy as np

budget_data = os.path.join('..','Resources', 'budget_data.csv')

# for loop to count months through every year
# x =  0, and then add ot it every line
# subtract next month from curerent month, and add it to a variable, and then divide by length of list
# find greatest in list
# find greatest decres



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

maximum = ""
minimum = ""


with open (budget_data) as budget_data:
	csv_reader = csv.reader(budget_data, delimiter = ",")

	header = next(csv_reader)
	for i in csv_reader:

#		net_totals.append(i[1])
#		for i in net_totals:
#			net_totals[i] = int(net_totals[i])
#			i = i+1

		profit_changes_str.append(i[1])
		net_totals.append(i[1])
		net_totals = [int(item) for item in net_totals]
		total_months = total_months + 1

	for i in range(len(net_totals)):

		try:
			current_month = int(net_totals[i])
			next_month = int(net_totals[i+1])
			month_change = next_month - current_month
			profit_changes.append(month_change)

#			for i in net_totals:
#				if i > maximum:
#					maximum = i
#
#				if i < minimum:
#					minimum = i

		except IndexError:
			break

	#print(profit_changes)
#	print(net_totals)
#	for i in net_totals:
#		print(type(i))

	#print (len(profit_changes))
	




	#print(maximum)
	#print(minimum)

	print ("Total Months: " + str(total_months - 1))
	print ("Total: " + str(sum(net_totals)))
	total_profit_changes = sum(profit_changes)
	avg_profit_changes = total_profit_changes/len(profit_changes)
	print("Average Change: " + str(avg_profit_changes))
	print ("Greatest Increase in Profits: " + str(max(profit_changes)))
	print ("Greatest Decrease in Profits: " + str(min(profit_changes)))
	#print (type(net_totals))

	#print(profit_changes)


#avg_change = profit_changes/length

#	length = len(budget_data - 2)

#	cs.reader[1]

#    minVal, maxVal = [], []
#    for i in data:
#        minVal.append(i[1])
#        maxVal.append(i[2])

#print min(minVal)
#print max(maxVal)