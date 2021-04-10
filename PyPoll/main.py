# importing needed libaries
import os
import csv

# Getting to the file path with my needed csv. One directory backwards and then into resources
PyPoll = os.path.join('..','Resources', 'PyPoll_Resources_election_data.csv')

# Declaring all my needed variables and lists
total_votes = 0
khan_count = 0
correy_count = 0
tooley_count = 0
li_count = 0
names = []
list_of_names = []
diff_names_count = 0
khan_percent = 0
correy_percent = 0
tooley_percent = 0
li_percent = 0

# reading my csv file
with open (PyPoll) as PyPoll:
	csv_reader = csv.reader(PyPoll, delimiter = ",")
# skips the header
	header = next(csv_reader)
	for i in csv_reader:
# make a list of every single name in column 3 of the csv
		names.append(i[2])
# counts total votes
		total_votes = total_votes + 1

	for name in names:
		# to make a list of different names
		if name not in list_of_names:
			list_of_names.append(name)
		#	Used for debugging purposes
		#	diff_names_count = diff_names_count + 1
		
		# counting all Khans, correys, lis, and tooleys in list_of names
		if name == "Khan":
			khan_count = khan_count + 1
		if name == "Correy":
			correy_count = correy_count + 1
		if name == "Li":
			li_count = li_count + 1
		if name == "O'Tooley":
			tooley_count = tooley_count + 1


# creating percentages
khan_percent = 100*(round(khan_count/total_votes, 2))
correy_percent = 100*(round(correy_count/total_votes, 2))
tooley_percent = 100*(round(tooley_count/total_votes, 2))
li_percent = 100*(round(li_count/total_votes, 2))

#Printing requested information
print("Election Results")
print("Total Votes: " + str(total_votes))
print("Candidates" + str(list_of_names))
#print(diff_names_count)
print("Khan: " + str(khan_percent) + "% " + str(khan_count))
print("Correy: " + str(correy_percent) + "% " + str(correy_count))
print("Li: " + str(li_percent) + "% " + str(li_count))
print("O'Tooley: " + str(tooley_percent) + "% " + str(tooley_count))

# If statment to choose Winner
if khan_count > correy_count and khan_count > li_count and khan_count > tooley_count:
	print("Winner: Khan")
if correy_count > khan_count and correy_count > li_count and correy_count > tooley_count:
	print("Winner: Correy")
if li_count > khan_count and li_count > correy_count and li_count > tooley_count:
	print("Winnder: Li")
if tooley_count > khan_count and tooley_count > correy_count and tooley_count > li_count:
	print("Winner: O'Tooley")
else:
	print("Winner: No one")	

file = open("PyPoll_Analysis.txt", "w")
file.write("Election Results")
file.write("\n")
file.write("Total Votes: " + str(total_votes))
file.write("\n")
file.write("Candidates" + str(list_of_names))
file.write("\n")
file.write("Khan: " + str(khan_percent) + "% " + str(khan_count))
file.write("\n")
file.write("Correy: " + str(correy_percent) + "% " + str(correy_count))
file.write("\n")
file.write("Li: " + str(li_percent) + "% " + str(li_count))
file.write("\n")
file.write("O'Tooley: " + str(tooley_percent) + "% " + str(tooley_count))

# closing the text file
file.close()