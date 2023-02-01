# Importing path from path library 
from pathlib import Path
# Importing csv file 
import csv

# Creating the file to a csv file
fp = Path.cwd()/"csv_reports"/"overheads-day-90.csv"

# Read the csv file to append name of the overheads and the overhead's percentage from the csv.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    # Skip header
    next(reader) 

# Creating an empty list to store name of the overheads and the overhead's percentage 
    overheads = [] 
# Append name of the overheads and the overhead's percentage as a list back to each empty list
    for row in reader:
        overheads.append([row[0], row[1]])

# Creating a function called overheads_function()
def overheads_function():
    '''
    This function does not accepts any parameter 
    This function will identify the highest overhead and the percentage
    '''
    # Creating an empty list to store the percentage of overheads
    percentage_of_overheads= []
    # Creating an empty list to store the final statement 
    statement= []
    
    # Creating a for loop to loop the items in the overheads list as data
    for data in overheads:
    # Append the percentage of overheads into the percentage_of_overheads list
        percentage_of_overheads.append(float(data[1]))
    # Using max function to identify the highest overhead's percentage and assigning it to a variable called highest_overheads_percentage
        highest_overheads_percentage = max(percentage_of_overheads)
        
    # If the highest overheads percentage is the same as the percentage of the item in data, the name of the highest overheads will be identified 
        if float(data[1]) == highest_overheads_percentage:
    # A highest overheads statement will be appended into the statement list
           statement.append(f'[HIGHEST OVERHEADS] {data[0]}: {highest_overheads_percentage}%')
        
    # The function will return statement at the end of all the loops
    return statement 

# The function is assigned to a variable called summary
summary = overheads_function()

# Import Path method from Path Library
from pathlib import Path
# Creating a text file called cluser_report.txt using .touch() and stored in a variable called file_path
file_path = Path.cwd()/"summary_report.txt"
file_path.touch()


# Open the file in file_path using .open and "a" to append text in the text file
with file_path.open(mode="a", encoding= "UTF-8") as file:
    for item in summary:
        file.write(f'{item}\n')






    

