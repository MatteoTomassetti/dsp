#!/usr/bin/env python3

import csv
import numpy as np

# code copied from advanced_python_regex.py
# --- START ---
# reading the data
datafile = "faculty.csv"
reader = csv.reader(open(datafile, 'r'))
keys = reader.__next__()
data={key:[] for key in keys}
for row in reader:
  for k in range(len(row)):
    data[keys[k]].append(row[k])

# converting every field into a numpy array
for k in range(len(keys)):
  data[keys[k]] = np.array(data[keys[k]])

all_titles = []
for title in data[" title"]:
  title = title.replace(" is"," of")
  idx = title.find(" of") # find the index of the first occurence of " of" in the title string
  all_titles.append(title[:idx])

all_emails = data[" email"]


#Q6.  Create a dictionary in the below format:
# ```
# faculty_dict = { 'Ellenberg': [\
#               ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'],\
#               ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']
#                             ],
#               'Li': [\
#               ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'],\
#               ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'],\
#               ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']
#                             ]
#             }
# ```
# Print the first 3 key and value pairs of the dictionary:

# find the name and surname of the faculty members

the_names = [dummy.split(" ")[0] for dummy in data["name"]]
the_surnames = [dummy.split(" ")[-1] for dummy in data["name"]]

# reformatting the degree field following the example in the instructions
# we select the string from [1:] because there's a white space at the beginning of each degree
# we want PhD to be formatted as Ph.D. (maybe the same for ScD although it is not clear)

all_degrees = []
for dummy in data[" degree"]:
  idx = 0
  if(dummy[0]==" "): idx = 1
  all_degrees.append(dummy.replace(".","")[idx:])

all_degrees = [dummy.replace("PhD","Ph.D.") for dummy in all_degrees]
all_degrees = [dummy.replace("ScD","Sc.D.") for dummy in all_degrees]

professor_dict = {(the_names[i]): [all_degrees[i],all_titles[i],all_emails[i]] for i in range(len(the_names))}

for i in range(3):
  the_key = list(professor_dict.keys())[i]
  print (the_key, professor_dict[the_key])

# Q7.  The previous dictionary does not have the best design for keys.  Create a new dictionary with keys as:
#```
#professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'],\
#                ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'],\
#                ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'],\
#                ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'],\
#                ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']
#            }
#```


professor_dict = {(the_names[i],the_surnames[i]): [all_degrees[i],all_titles[i],all_emails[i]] for i in range(len(the_names))}

for i in range(3):
  the_key = list(professor_dict.keys())[i]
  print (the_key, professor_dict[the_key])


#Q8.  It looks like the current dictionary is printing by first name.  Sort by last name and print the first 3 key and value pairs.  
# I disagree with what it's stated in the question. The `professor_dict` dictionary prints by first name
# only if we do `sorted(professor_dict)`
# anyway, let's sort this bad boy by last name and print the first 3 keys and values

keys_sorted_by_surname = sorted(professor_dict.keys(),key = lambda x:x[1])

for i in range(3):
  print (keys_sorted_by_surname[i],professor_dict[keys_sorted_by_surname[i]])


