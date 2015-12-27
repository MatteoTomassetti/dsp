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

all_emails = data[" email"]

# --- END ---

# Q5. Write email addresses from Part I to csv file

filename = "emails.csv"
with open(filename, "w") as f:
    writer = csv.writer(f, lineterminator='\n')
    for email in all_emails:
        writer.writerow([email]) 



