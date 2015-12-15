#The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.


import csv

class Football:
  
  def __init__(self,data):
    reader = csv.reader(open(data, 'r'))
    keys = reader.next()
    self.parsed_data={key:[] for key in keys}
    for row in reader:
      for k in range(len(row)):
        self.parsed_data[keys[k]].append(row[k])
    #
    self.parsed_data[keys[0]] = np.array(self.parsed_data[keys[0]])
    for k in range(1,len(keys)):
      self.parsed_data[keys[k]] = np.array(self.parsed_data[keys[k]]).astype("int")
  
  def get_min_score_difference(self):
    return min(self.parsed_data["Goals"]-self.parsed_data["Goals Allowed"])
  
  def get_team(self):
    mask = self.parsed_data["Goals"]-self.parsed_data["Goals Allowed"] == self.get_min_score_difference()
    return self.parsed_data["Team"][mask][0]

g=Football("football.csv")

print 'Team with the minimum difference between "Goals" and "Goals Allowed":', g.get_team()
# print g.get_min_score_difference()
  

  
