#!/usr/bin/env python3

import csv
import numpy as np

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
  
# Q1. Find how many different degrees there are, and their frequencies: Ex: PhD, ScD, MD, MPH, BSEd, MS, JD, etc.

# some people have multiple degrees, so we have to split the string containing the degree for every individual
# we also remove the dots from the degree type because we don't want PhD and Ph.D. we identified as two different degrees
# we also filter out empty string

all_degrees = []
for dummy in data[" degree"]:
  all_degrees.extend([the_degree.replace(".","") for the_degree in filter(None,dummy.split(" "))])

from collections import Counter
for degree, frequency in Counter(all_degrees).most_common():
  print (degree, frequency)

# Q2. Find how many different titles there are, and their frequencies:  Ex:  Assistant Professor, Professor
# We want to remove the part of string after "of ..."
# one string has "is" instead of "of", so we have fixed that

all_titles = []
for title in data[" title"]:
  title = title.replace(" is"," of")
  idx = title.find(" of") # find the index of the first occurence of " of" in the title string
  all_titles.append(title[:idx])

for title, frequency in Counter(all_titles).most_common():
  print (title, frequency)

# Q3. Search for email addresses and put them in a list.  Print the list of email addresses.
all_emails = data[" email"]
print (all_emails.tolist())

# Q4. Find how many different email domains there are (Ex:  mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.).  Print the list of unique email domains.

all_domains = []
for email in all_emails:
  idx = email.find("@") # we want to save only the domain of each email
  all_domains.append(email[idx+1:])

print (np.unique(np.array(all_domains)))

  
