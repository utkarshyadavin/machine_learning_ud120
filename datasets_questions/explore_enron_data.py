#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))


# Total number of data poionts in the enron data 
print(len(enron_data))

# Total number of features 
print (len(enron_data.values()[0]))

 
 #Calculating the total number of person of interests

count = 0 

for i in range(len(enron_data)):
	a = enron_data.values()
	if a[i]['poi'] == True:
		count = count + 1 

print count 