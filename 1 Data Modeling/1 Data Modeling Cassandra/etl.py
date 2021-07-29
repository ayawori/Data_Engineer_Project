# Import Python packages 
import pandas as pd
import cassandra
import re
import os
import glob
import numpy as np
import json
import csv


#Creating list of filepaths to process original event csv
print(f"Current working directory: {os.getcwd()}")

filepath = os.getcwd()+ '/event_data'

for root, dirs, files in os.walk(filepath):
	file_path_list = glob.glob(os.path.join(root,'*'))

#Processing the files to create the data file csv that will be used for Cassandra tables

full_data_rows_list = []

for f in file_path_list:
	with open(f,'r',encoding='utf8',newline='') as csvfile:
		csvReader = csv.reader(csvfile)
		next(csvReader)

		for line in csvReader:
			full_data_rows_list.append(line)

print(f"Total rows: {len(full_data_rows_list)}")
print(f"Sample data:\n{full_data_rows_list[:5]}")

#create a smaller event data csv file that will use insert to Cassandra table
csv.register_dialect('myDialect', quoting=csv.QUOTE_ALL, skipinitialspace=True)

with open('event_datafile_new.csv','w',encoding='utf8',newline='') as f:
	writer = csv.writer(f,dialect='myDialect')
	writer.writerow(['artist','fileName','gender','itemInSession','lastName','length',\
					'level','location','sessionId','song','userId'])

	for row in full_data_rows_list:
		if(row[0]==''):
			continue
		writer.writerow((row[0], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[12], row[13], row[16]))

# checking the number of rows in new event csv file
with open('event_datafile_new.csv', 'r', encoding = 'utf8') as f:
    print(sum(1 for line in f))