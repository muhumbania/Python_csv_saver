import csv
import serial
import time

# field names
fields = ['Name', 'Branch', 'Year', 'CGPA']

# set up the serial line
ser = serial.Serial('COM5', 9600)
time.sleep(2)

# Read and record the data
data =[]                       # empty list to store the data
for i in range(50):
    b = ser.readline()         # read a byte string
    string_n = b.decode()  # decode byte string into Unicode  
    string = string_n.rstrip() # remove \n and \r
    flt = float(string)        # convert string to float
    print(flt)
    data.append(flt)           # add to the end of data list
    time.sleep(0.1)            # wait (sleep) 0.1 seconds

ser.close()


# show the data

for line in data:
    print(line)

# data rows of csv file
rows = [['Nikhil', 'COE', '2', '9.0'],
		['Sanchit', 'COE', '2', '9.1'],
		['Aditya', 'IT', '2', '9.3'],
		['Sagar', 'SE', '1', '9.5'],
		['Prateek', 'MCE', '3', '7.8'],
		['Sahil', 'EP', '2', '9.1']]

# name of csv file
filename = "university_records.csv"

# writing to csv file
with open(filename, 'w') as csvfile:
	# creating a csv writer object
	csvwriter = csv.writer(csvfile)

	# writing the fields
	csvwriter.writerow(fields)

	# writing the data rows
	csvwriter.writerows(rows)
